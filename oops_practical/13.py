'''Bank Account Inheritance: Design a class hierarchy for different types of bank acounts , such as saving accounts, checking accounts and fixed diposit account. 
Inplement common operations like deposits, withdrawls, and balance inquiries'''

from datetime import datetime, timedelta
from typing import Optional

class BankAccount:
    """Base bank account with common operations."""
    _next_account_number = 1000000

    def __init__(self, holder_name: str, balance: float = 0.0):
        self.account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1

        self.holder_name = holder_name
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        """Deposit amount; returns new balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraw amount if funds available; returns new balance.
        Base class does not allow overdraft."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> float:
        return self.balance

    def transfer_to(self, target: "BankAccount", amount: float) -> None:
        """Transfer funds from this account to target account."""
        self.withdraw(amount)
        target.deposit(amount)

    def __str__(self):
        return f"Account[{self.account_number}] {self.holder_name}: ₹{self.balance:.2f}"


# ---------------- Savings Account ----------------
class SavingsAccount(BankAccount):
    """
    SavingsAccount supports interest accrual and minimum balance penalty.
    - annual_interest_rate: percent per year
    - min_balance: if balance falls below this, penalty is applied
    - min_balance_penalty: fixed fee applied when balance < min_balance
    """
    def __init__(self, holder_name: str, balance: float = 0.0,
                 annual_interest_rate: float = 4.0,
                 min_balance: float = 500.0,
                 min_balance_penalty: float = 100.0):
        super().__init__(holder_name, balance)
        self.annual_interest_rate = float(annual_interest_rate)
        self.min_balance = float(min_balance)
        self.min_balance_penalty = float(min_balance_penalty)

    def withdraw(self, amount: float) -> float:
        """Withdraw and apply min-balance penalty if necessary."""
        new_balance = super().withdraw(amount)  # may raise ValueError
        if new_balance < self.min_balance:
            # Apply penalty (if balance allowed to go below min)
            # If penalty makes balance negative, allow negative (or could disallow)
            self.balance -= self.min_balance_penalty
        return self.balance

    def accrue_interest(self, months: int = 1) -> float:
        """Accrue interest for given months and add to balance.
        Uses simple pro-rated interest: interest = balance * rate * months/12.
        Returns interest amount added."""
        if months <= 0:
            raise ValueError("Months must be positive.")
        interest = self.balance * (self.annual_interest_rate / 100.0) * (months / 12.0)
        self.balance += interest
        return interest


# ---------------- Checking Account ----------------
class CheckingAccount(BankAccount):
    """
    Checking account with optional overdraft facility.
    - overdraft_limit: how much negative balance is allowed
    - overdraft_fee: flat fee applied once per overdraft occurrence
    """
    def __init__(self, holder_name: str, balance: float = 0.0,
                 overdraft_limit: float = 0.0, overdraft_fee: float = 0.0):
        super().__init__(holder_name, balance)
        self.overdraft_limit = float(overdraft_limit)
        self.overdraft_fee = float(overdraft_fee)
        self._in_overdraft = False

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        potential_balance = self.balance - amount
        if potential_balance < -self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit.")

        self.balance = potential_balance

        # If we've entered overdraft and were not previously in overdraft, apply fee
        if self.balance < 0 and not self._in_overdraft and self.overdraft_fee > 0:
            self.balance -= self.overdraft_fee
            self._in_overdraft = True

        # Clear flag if back to non-negative
        if self.balance >= 0:
            self._in_overdraft = False

        return self.balance


# ---------------- Fixed Deposit Account ----------------
class FixedDepositAccount:
    """
    Fixed deposit (term deposit) — not a typical BankAccount subclass because
    FD commonly prevents withdrawals until maturity.
    - principal: initial deposit
    - term_months: integer months
    - annual_interest_rate: percent per year
    - start_date: datetime (defaults to now)
    - early_withdrawal_penalty_pct: percentage of interest (not principal) taken if withdrawn early
    """
    _next_fd_account = 9000000

    def __init__(self, holder_name: str, principal: float,
                 term_months: int, annual_interest_rate: float = 6.0,
                 start_date: Optional[datetime] = None,
                 early_withdrawal_penalty_pct: float = 50.0):
        if principal <= 0:
            raise ValueError("Principal must be positive.")
        if term_months <= 0:
            raise ValueError("Term must be positive months.")

        self.fd_account_number = FixedDepositAccount._next_fd_account
        FixedDepositAccount._next_fd_account += 1

        self.holder_name = holder_name
        self.principal = float(principal)
        self.term_months = int(term_months)
        self.annual_interest_rate = float(annual_interest_rate)
        self.start_date = start_date or datetime.now()
        self.early_withdrawal_penalty_pct = float(early_withdrawal_penalty_pct)
        self.is_closed = False  # True after withdrawal/payout

    def maturity_date(self) -> datetime:
        return self.start_date + timedelta(days=30 * self.term_months)

    def _interest_for_term(self, months: Optional[int] = None) -> float:
        """Simple interest pro-rated (principal * rate * months/12)."""
        months = months if months is not None else self.term_months
        return self.principal * (self.annual_interest_rate / 100.0) * (months / 12.0)

    def is_matured(self, as_of: Optional[datetime] = None) -> bool:
        as_of = as_of or datetime.now()
        return as_of >= self.maturity_date()

    def withdraw(self, as_of: Optional[datetime] = None) -> float:
        """
        Withdraw full FD (principal + interest). If before maturity, an early withdrawal
        penalty is applied to interest.
        Returns payout amount.
        """
        if self.is_closed:
            raise ValueError("This fixed deposit is already closed.")

        as_of = as_of or datetime.now()
        if self.is_matured(as_of):
            interest = self._interest_for_term()
            payout = self.principal + interest
        else:
            # partial months elapsed
            elapsed_days = (as_of - self.start_date).days
            elapsed_months = max(0, elapsed_days // 30)
            interest = self._interest_for_term(elapsed_months)
            penalty = (self.early_withdrawal_penalty_pct / 100.0) * interest
            payout = self.principal + interest - penalty

        # close FD
        self.is_closed = True
        return payout

    def __str__(self):
        return (f"FD[{self.fd_account_number}] {self.holder_name}: Principal=₹{self.principal:.2f}, "
                f"Term={self.term_months} months, Rate={self.annual_interest_rate:.2f}%")

# ---------------- Example usage / Quick demo ----------------
if __name__ == "__main__":
    print("=== Bank Accounts Demo ===\n")

    # Savings account demo
    sav = SavingsAccount("Raju", balance=2000.0, annual_interest_rate=4.5, min_balance=1000.0, min_balance_penalty=50.0)
    print("Created:", sav)
    print("Deposit 500 ->", sav.deposit(500))
    print("Accrue interest for 6 months -> interest added:", sav.accrue_interest(months=6))
    print("Balance after interest:", sav.get_balance())
    try:
        print("Withdraw 1800 ->", sav.withdraw(1800))
        print("Balance after withdrawal (may have penalty if below min):", sav.get_balance())
    except ValueError as e:
        print("Withdrawal failed:", e)
    print()

    # Checking account demo with overdraft
    chk = CheckingAccount("Shyam", balance=1000.0, overdraft_limit=500.0, overdraft_fee=100.0)
    print("Created:", chk)
    print("Withdraw 1200 (uses overdraft) ->", chk.withdraw(1200))
    print("Balance after overdraft and fee:", chk.get_balance())
    try:
        chk.withdraw(500)  # might exceed overdraft
    except ValueError as e:
        print("Further withdrawal failed:", e)
    print()

    # Transfer demo
    print("Transfer ₹200 from savings to checking")
    try:
        sav.transfer_to(chk, 200)
        print("Savings:", sav)
        print("Checking:", chk)
    except ValueError as e:
        print("Transfer failed:", e)
    print()

    # Fixed Deposit demo
    fd = FixedDepositAccount("Babubhai", principal=10000.0, term_months=12, annual_interest_rate=7.0, early_withdrawal_penalty_pct=40.0)
    print("Created FD:", fd)
    print("Maturity date:", fd.maturity_date().date())
    # Simulate early withdrawal after 4 months
    early_date = fd.start_date + timedelta(days=30 * 4)
    payout_early = fd.withdraw(as_of=early_date)
    print(f"Early withdrawal payout after 4 months: ₹{payout_early:.2f}")
