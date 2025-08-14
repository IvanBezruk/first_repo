"""
from collections import UserDict

contacts = [
    {"name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792", "favorite": False},
    {"name": "Chaim Lewis", "email": "dui.in@egetlacus.ca", "phone": "(294) 840-6685", "favorite": False},
    {"name": "Kennedy Lane", "email": "mattis.Cras@nonenimMauris.net", "phone": "(542) 451-7038", "favorite": True},
]

class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"


customers = [Customer(c) for c in contacts]

print("---------------------------")
for customer in customers:
    print(customer.phone_info())

print("---------------------------")
for customer in customers:
    print(customer.email_info())

"""    
"""
from collections import UserList

class MyList(UserList):
    def add_if_not_exist(self, item):
        if item not in self.data:
            self.data.append(item)

my_list = MyList([1, 2, 3])
print("Original list:", my_list)

my_list.add_if_not_exist(3)
my_list.add_if_not_exist(4)
my_list.add_if_not_exist(5)

print("Sum:", sum(my_list))

"""
"""
from collections import UserList

class UniqueList(UserList):
    def __init__(self, data=None):
        super().__init__(data)
        self.duplicates = 0
    
    def append(self, item):
        if item not in self.data:
            self.data.append(item)
        else:
            self.duplicates += 1
    
    def extend(self, items):
        for item in items:
            if item not in self.data:
                self.data.append(item)
            else:
                self.duplicates += 1
    
    def get_duplicates_attempted(self):
        return self.duplicates

unique_list = UniqueList([1, 2, 3])
print("Initial:", unique_list)

unique_list.append(2)  # Should be blocked (duplicate)
unique_list.append(4)  # Should be added
unique_list.extend([3, 5, 2, 6])  # Only 5 and 6 should be added

print("Final:", unique_list)
print("Duplicates blocked:", unique_list.get_duplicates_attempted())
"""

"""
from collections import UserString

class MyString(UserString):
    def is_palindrome(self):
        return self.data == self.data[::-1]
    
my_string = MyString("radar")
print("String:", my_string)
print("Is palindrome?", my_string.is_palindrome())

another_string = MyString("hello")
print("String:", another_string)
print("Is palindrome?:", another_string.is_palindrome())


from collections import UserString

class TruncatedString(UserString):
    MAX_LEN = 7
    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString("hello world!")
ts.truncate()
print(ts)
"""

"""
from collections import UserString

class BoundedString(UserString):
    MAX_LEN = 10
    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

    def is_palindrome(self, ignore_case=True, ignore_spaces=True):
        if ignore_case: 
            self.data.lower()
        
        if ignore_spaces == True:
                return self.data.replace(" ", "")
        return self.data == self.data[::-1]
    
bs1 = BoundedString("Never odd or even")
print("Original:", bs1)
print("Is palindrome (default):", bs1.is_palindrome())
bs1.truncate()
print("Truncated:", bs1)

bs2 = BoundedString("RaceCar")
print("Case-insensitive:", bs2.is_palindrome(ignore_case=True, ignore_spaces=False))
print("Case-sensitive:", bs2.is_palindrome(ignore_case=False, ignore_spaces=False))

bs3 = BoundedString("hello world!")
bs3.truncate()
print("Truncated hello:", bs3)
"""

"""
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    

from dataclasses import dataclass

@dataclass
class Article:
    title: str
    author: str
    views: int = 0


from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height
    

# Part A: Create and print Person instances
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
print(person1)
print(person2)

# Part B: Create and print Article instances
article1 = Article("Python Tips", "John Doe")  # uses default views=0
article2 = Article("Advanced OOP", "Jane Smith", 150)
print(article1)
print(article2)

# Part C: Create rectangles and print areas
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Area 1: {rect1.area()}")
print(f"Area 2: {rect2.area()}")
print(f"Area 3: {rect3.area()}")
"""

"""
from dataclasses import dataclass

@dataclass
class Person(dataclass):
    name: str
    age: int

class Article:
    title: str
    author: str
    views: int = 0

class Rectangle:
    width: int
    height: int
    
    def area(self) -> int:
        return self.width * self.height
    

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
print(person1)
print(person2)
"""

from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

today = Day.MONDAY
print(today)
print(today.name)
print(today.value)

day_from_value = Day(1)
print(day_from_value)

if today == Day.MONDAY:
    print("Today is Monday.")

from enum import Enum, auto

class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()

class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status
    
    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Order '{self.name}' updated to {self.status.name}.")

    def display_status(self):
        print(f"Order '{self.name}' status: {self.status.name}")

# Code usage:
order1 = Order("Laptop", OrderStatus.NEW)
order2 = Order("Book", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()