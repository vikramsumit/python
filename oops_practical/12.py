# bank_accounts.py
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta
import calendar
from typing import List, Dict, Optional
import math

# ---------------------------
# Utility helpers
# ---------------------------
def add_months(dt: datetime, months: int) -> datetime:
    """Return a datetime increased by `months` (keeps day as close as possible)."""
    total_months = dt.year * 12 + (dt.month - 1) + months
    year = total_months // 12
    month = total_months % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return datetime(year, month, day, dt.hour, dt.minute, dt.second, dt.microsecond)

def months_between(start: datetime, end: datetime) -> int:
    """Return whole months elapsed from start to end (end >= start assumed)."""
    return max(0, (end.year - start.year) * 12 + (end.month - start.month) - (1 if end.day < start.day else 0))

# ---------------------------
# Base class
# ---------------------------
class BankAccount:
    _next_account_no = 1001

    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_no = BankAccount._next_account_no
        BankAccount._next_account_no += 1

        self.owner = owner
        self._balance = float(initial_balance)
        self.created_at = datetime.now()
        self.transactions: List[Dict] = []
        if initial_balance > 0:
            self._record_txn("DEPOSIT", initial_balance)

    # internal
    def _record_txn(self, kind: str, amount: float, note: str = ""):
        self.transactions.append({
            "timestamp": datetime.now(),
            "type": kind,
            "amount": float(amount),
            "balance": float(self._balance),
            "note": note
        })

    # basic operations
    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self._record_txn("DEPOSIT", amount)
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        self._record_txn("WITHDRAW", -amount)
        return self._balance

    def get_balance(self) -> float:
        return float(self._balance)

    def print_statement(self):
        print(f"---- Account Statement: {self.account_no} ({self.owner}) ----")
        for tx in self.transactions:
            ts = tx["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{ts} | {tx['type']:7} | {tx['amount']:10.2f} | bal: {tx['balance']:10.2f} | {tx['note']}")
        print(f"Current balance: ₹{self._balance:.2f}")
        print("-----------------------------------------------------")

# ---------------------------
# Savings Account
# ---------------------------
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, initial_balance: float = 0.0,
                 annual_interest_rate: float = 3.5, min_balance: float = 0.0,
                 monthly_withdrawal_limit: Optional[int] = None):
        """
        annual_interest_rate: percent (e.g., 3.5 for 3.5% p.a.)
        min_balance: minimum balance required after withdrawals
        monthly_withdrawal_limit: None means unlimited, otherwise integer limit
        """
        super().__init__(owner, initial_balance)
        self.annual_interest_rate = float(annual_interest_rate)
        self.min_balance = float(min_balance)
        self.monthly_withdrawal_limit = monthly_withdrawal_limit
        self._withdrawals_this_month = 0
        self._last_withdrawal_month = datetime.now().month

    def _maybe_reset_withdrawals(self):
        now = datetime.now()
        if now.month != self._last_withdrawal_month:
            self._withdrawals_this_month = 0
            self._last_withdrawal_month = now.month

    def withdraw(self, amount: float) -> float:
        self._maybe_reset_withdrawals()
        if self.monthly_withdrawal_limit is not None and self._withdrawals_this_month >= self.monthly_withdrawal_limit:
            raise ValueError("Monthly withdrawal limit reached.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if (self._balance - amount) < self.min_balance:
            raise ValueError("Cannot withdraw: would go below minimum balance.")
        self._balance -= amount
        self._withdrawals_this_month += 1
        self._record_txn("WITHDRAW", -amount, note=f"savings withdrawal (month withdrawals: {self._withdrawals_this_month})")
        return self._balance

    def apply_interest(self, months: int = 1) -> float:
        """
        Apply interest for the given whole number of months.
        Interest is compounded monthly.
        """
        if months <= 0:
            return self._balance
        monthly_rate = self.annual_interest_rate / 100.0 / 12.0
        old_balance = self._balance
        self._balance *= (1 + monthly_rate) ** months
        interest_earned = self._balance - old_balance
        if interest_earned > 0:
            self._record_txn("INTEREST", interest_earned, note=f"applied for {months} month(s)")
        return interest_earned

# ---------------------------
# Fixed Deposit Account (FD)
# ---------------------------
class FixedDepositAccount(BankAccount):
    def __init__(self, owner: str, principal: float, term_months: int, annual_interest_rate: float,
                 compounding: str = "monthly", early_withdrawal_penalty_percent: float = 1.0):
        """
        Fixed deposit account:
        - principal: initial one-time deposit
        - term_months: duration in months
        - annual_interest_rate: percent (e.g. 6.5)
        - compounding: 'monthly' or 'annual' or 'none' (we support monthly or none)
        - early_withdrawal_penalty_percent: percent penalty on the current amount if withdrawn before maturity
        """
        if principal <= 0:
            raise ValueError("Principal must be positive.")
        super().__init__(owner, initial_balance=principal)
        self.principal = float(principal)
        self.term_months = int(term_months)
        self.annual_interest_rate = float(annual_interest_rate)
        self.compounding = compounding
        self.start_date = datetime.now()
        self.maturity_date = add_months(self.start_date, self.term_months)
        self.early_withdrawal_penalty_percent = float(early_withdrawal_penalty_percent)
        # For FD we treat base _balance as principal; interest is computed separately
        # Disallow normal deposit/withdraw flow (override deposit)
        self._record_txn("FD_OPEN", principal, note=f"term {term_months} months @ {annual_interest_rate}% p.a.")

    def deposit(self, amount: float):
        raise NotImplementedError("Cannot deposit into an existing fixed deposit. Create a new FD instead.")

    def _current_value(self, as_of: Optional[datetime] = None) -> float:
        """Return current value (principal + accrued interest) as of 'as_of' (default now)."""
        as_of = as_of or datetime.now()
        if as_of < self.start_date:
            return self.principal
        months_elapsed = months_between(self.start_date, as_of)
        if self.compounding == "monthly":
            r = self.annual_interest_rate / 100.0
            # monthly compounding
            return self.principal * (1 + r / 12.0) ** months_elapsed
        else:
            # simple interest proportional to months (fallback)
            return self.principal * (1 + (self.annual_interest_rate / 100.0) * (months_elapsed / 12.0))

    def is_matured(self, as_of: Optional[datetime] = None) -> bool:
        as_of = as_of or datetime.now()
        return as_of >= self.maturity_date

    def get_balance(self, as_of: Optional[datetime] = None) -> float:
        """Override: balance is the current_value (principal + accrued interest)"""
        return float(self._current_value(as_of))

    def withdraw(self, amount: float = None, as_of: Optional[datetime] = None) -> float:
        """
        Withdraw from FD.
        - If matured: allow withdrawal up to current value (partial allowed).
        - If not matured: allow early withdrawal of full or partial amount but apply penalty.
        Returns balance remaining after withdrawal or 0 if fully withdrawn.
        """
        as_of = as_of or datetime.now()
        current_value = self._current_value(as_of)
        if amount is None:
            amount = current_value  # full withdrawal
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > current_value + 1e-9:
            raise ValueError("Requested amount exceeds current FD value.")

        if self.is_matured(as_of):
            # matured: simply withdraw from current value; keep principal book as zero
            new_value = current_value - amount
            self._balance = new_value  # track remaining (if partial withdrawal)
            self._record_txn("FD_WITHDRAW", -amount, note="matured withdrawal")
            return self._balance
        else:
            # early withdrawal penalty: apply penalty percent to the withdrawn amount or to full current value.
            # We implement penalty as percent of the withdrawn amount.
            penalty = (self.early_withdrawal_penalty_percent / 100.0) * amount
            net = amount - penalty
            # After early withdrawal, FD usually breaks or reduces principal. For simplicity:
            remaining_value = current_value - amount
            # We'll set internal balance to remaining_value (if any); otherwise 0.
            self._balance = remaining_value
            self._record_txn("FD_EARLY_WITHDRAW", -net, note=f"early withdrawal (penalty: ₹{penalty:.2f})")
            # return net paid out to customer
            return net

    def close_at_maturity(self) -> float:
        """
        Close FD at maturity and return maturity amount. After closing, balance becomes 0.
        """
        if not self.is_matured():
            raise ValueError("Cannot close FD before maturity without using early withdrawal.")
        amount = self._current_value(self.maturity_date)
        self._record_txn("FD_MATURE", amount, note="matured and closed")
        self._balance = 0.0
        return amount

# ---------------------------
# Usage examples
# ---------------------------
if __name__ == "__main__":
    print("=== Savings Account Demo ===")
    s = SavingsAccount("Alice", initial_balance=10000.0, annual_interest_rate=4.0, min_balance=500.0, monthly_withdrawal_limit=3)
    print("Balance:", s.get_balance())
    s.deposit(2000.0)
    print("After deposit:", s.get_balance())
    try:
        s.withdraw(300.0)
        s.withdraw(100.0)
        s.withdraw(50.0)
        # Fourth withdrawal this month should fail
        s.withdraw(25.0)
    except Exception as e:
        print("Expected error on withdrawal:", e)
    # Apply 2 months interest
    interest = s.apply_interest(months=2)
    print(f"Interest applied for 2 months: ₹{interest:.2f}")
    s.print_statement()

    print("\n=== Fixed Deposit Demo ===")
    fd = FixedDepositAccount("Bob", principal=50000.0, term_months=12, annual_interest_rate=6.0, early_withdrawal_penalty_percent=1.5)
    print("FD start:", fd.start_date.strftime("%Y-%m-%d"))
    print("FD maturity:", fd.maturity_date.strftime("%Y-%m-%d"))
    print("FD current (now) value:", f"₹{fd.get_balance():.2f}")
    # Simulate checking value after 6 months:
    six_months_after = add_months(fd.start_date, 6)
    print("Value after 6 months:", f"₹{fd.get_balance(as_of=six_months_after):.2f}")
    # Early partial withdrawal of 10,000 at 6 months:
    payout = fd.withdraw(amount=10000.0, as_of=six_months_after)
    print(f"Early withdrawal payout (after penalty): ₹{payout:.2f}")
    fd.print_statement()
    # Fast-forward to maturity and close:
    matured_date = fd.maturity_date
    print("FD matured?:", fd.is_matured(as_of=matured_date))
    amount_on_maturity = fd._current_value(as_of=matured_date)
    print(f"Amount at maturity (if not fully withdrawn earlier): ₹{amount_on_maturity:.2f}")
    try:
        payout_full = fd.close_at_maturity()
        print("Closed FD payout:", f"₹{payout_full:.2f}")
    except Exception as e:
        print("Closing FD error:", e)
    fd.print_statement()