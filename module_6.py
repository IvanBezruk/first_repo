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