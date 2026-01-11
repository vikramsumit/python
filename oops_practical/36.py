# Create an abstract class "LibraryItem" with abstract methods for common library operations like check_out(), return_item(), and due_date(). Derive concrete classes for various item types, such as "Book," "DVD," and "Magazine," and implement these methods accordingly.

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
        self.is_checked_out = False
        self.checked_out_date = None

    @abstractmethod
    def check_out(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

    @abstractmethod
    def due_date(self):
        pass

class Book(LibraryItem):
    TIME_PERIOD = 14  # days

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.checked_out_date = datetime.now()
            print(f'Book "{self.title}" checked out.')
        else:
            print(f'Book "{self.title}" is already checked out.')

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            self.checked_out_date = None
            print(f'Book "{self.title}" returned.')
        else:
            print(f'Book "{self.title}" was not checked out.')

    def due_date(self):
        if self.is_checked_out:
            return self.checked_out_date + timedelta(days=self.TIME_PERIOD)
        return None

class DVD(LibraryItem):
    TIME_PERIOD = 7  # days

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.checked_out_date = datetime.now()
            print(f'DVD "{self.title}" checked out.')
        else:
            print(f'DVD "{self.title}" is already checked out.')

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            self.checked_out_date = None
            print(f'DVD "{self.title}" returned.')
        else:
            print(f'DVD "{self.title}" was not checked out.')

    def due_date(self):
        if self.is_checked_out:
            return self.checked_out_date + timedelta(days=self.TIME_PERIOD)
        return None

class Magazine(LibraryItem):
    TIME_PERIOD = 5  # days

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            self.checked_out_date = datetime.now()
            print(f'Magazine "{self.title}" checked out.')
        else:
            print(f'Magazine "{self.title}" is already checked out.')

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            self.checked_out_date = None
            print(f'Magazine "{self.title}" returned.')
        else:
            print(f'Magazine "{self.title}" was not checked out.')

    def due_date(self):
        if self.is_checked_out:
            return self.checked_out_date + timedelta(days=self.TIME_PERIOD)
        return None

items = [
    Book("Python Programming"),
    DVD("Inception"),
    Magazine("National Geographic")
]

for item in items:
    item.check_out()
    print(f'Due date for "{item.title}": {item.due_date()}')
    print()

items[0].return_item()
