"""
class SimpleDict:
    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self._data[key] = value

sd = SimpleDict()
sd['name'] = 'Alice'
print(sd['name'])
print(sd['age'])
"""

"""
class BoundedList:
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val
        self._data = []

    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, value):
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"Value {value} must be between {self.min_val} and {self.max_val}")
        if index >= len(self._data):
            self._data.append(value)
        else:
            self._data[index] = value

    def __str__(self):
        return str(self._data)
    
temps = BoundedList(18, 26)
for i, t in enumerate([20, 22, 25, 27]):
    try:
        temps[i] = t
    except ValueError as e:
        print(e)

print(temps)
"""

"""
class Features:
    def __init__(self, name, values):
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("All values must be int or float")
            self.name = name
            self.values = values
            self.mean = sum(values)/len(values) if values else 0.0

    def __repr__(self):
        return f"Feature(name={self.name!r}, values={self.values})"

    def __str__(self):
        return f"Feature {self.name} - n={len(self.values)}, mean = {self.mean}"
    
    def __getitem__(self, index):
        return self.values[index]
    
    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            raise TypeError("value must be int or float")
        self.values[index] = value
        self.mean = sum(self.values) / len(self.values)

# Test it:
sales = Features("sales", [10, 20, 30])
print(sales[1])     
sales[1] = 25
print(sales[1])        
print(sales)
"""
"""
class Feature:
    def __init__(self, name, values):
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("All values must be int or float")
            self.name = name
            self.values = values
            self.mean = sum(values) / len(values) if values else 0.0

    def __add__(self, other):
        if not isinstance(other, Feature):
            return NotImplemented
        if len(self.values) != len(other.values):
            raise ValueError("Features must have the same length")
            
        new_values = [a+b for a, b in zip(self.values, other.values)]
        return Feature(f"{self.name}_plus_{other.name}", new_values)
        
    def __repr__(self):
        return f"Feature(name={self.name!r}, values = {self.values})"
        
    def __str__(self):
        return f"Feature {self.name} - n={len(self.values)}, mean = {self.mean}"
        

# Example usage:
f1 = Feature("A", [1, 2, 3])
f2 = Feature("B", [10, 20, 30])
f3 = f1 + f2
print(f3)  # Feature A_plus_B — n=3, mean=22.0
"""
"""
class Feature:
    def __init__(self, name, values):
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("All values must be int or float")
        self.name = name
        self.values = values
        self.mean = sum(values) / len(values) if values else 0.0

    def __add__(self, other):
        if not isinstance(other, Feature):
            return NotImplemented
        if len(self.values) != len(other.values):
            raise ValueError("Features must have the same length")
        new_values = [a + b for a, b in zip(self.values, other.values)]
        return Feature(f"{self.name}_plus_{other.name}", new_values)

    def __repr__(self):
        return f"Feature(name={self.name!r}, values={self.values})"

    def __str__(self):
        return f"Feature {self.name} — n={len(self.values)}, mean={self.mean}"

# Example usage:
f1 = Feature("A", [1, 2, 3])
f2 = Feature("B", [10, 20, 30])
f3 = f1 + f2
print(f3) 
"""

"""
from functools import total_ordering

@total_ordering
class Feature:
    def __init__(self, name, values):
        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError("All values must be int or float")
            
            self.name = name
            self.values = values
            self.mean = sum(values) / len(values) if values else 0.0

    def __repr__(self):
        return f"Feature(name={self.name!r}, values = {self.values})"
    
    def __str__(self):
        return f"Features {self.name} - n={len(self.values)}, mean = {self.mean}"
    
    def __eq__(Self, other):
        if not isinstance(other, Feature):
            return NotImplemented
        return (self.mean, self.name) ==(other.mean, other.name)
    
    def __lt__(self, other):
        if not isinstance(other, Feature):
            return NotImplemented
        return (self.mean, self.name) < (other.mean, other.name)
"""

"""
from functools import total_ordering

@total_ordering
class Feature:
    def __init__(self, name, values):
        for v in values:
            if not isinstance( v, (int, float)):
                raise ValueError("All values must be in int or float")
            
        self.name = name
        self.values = values
        self.mean = sum(values) / len(values) if values else 0.0

    def __repr__(self):
        return f"Feature (name={self.name!r}, values = {self.values})"
        

    def __eq__(self, other):
        if not isinstance(other, Feature):
            return NotImplemented
        return (self.mean, self.name) == (other.mean, other.name)

        
    def __lt__(self, other):
        if not isinstance(other, Feature):
            return NotImplemented
        return (self.mean, self.name) < (other.mean, other.name)
    
# Test it:
a = Feature("sales", [10, 20, 30])     # mean = 20
b = Feature("marketing", [5, 15, 25])  # mean = 15
c = Feature("revenue", [20, 20, 20])   # mean = 20

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"a == c: {a == c}")  # False (same mean, different names)
print(f"Sorted: {sorted([a, b, c])}")  # Should order by mean, then name
"""

"""
class Feature:
    def __init__(self, name, values):
        #validate values
        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError("All values must be int or float")
            self._name = name
            self._values = list(values)

    
    @property
    def values(self):
        return self._values
    
    @values.setter
    def values(self, new_values):
        for v in new_values:
            if not isinstance(v, (int, float)):
                raise TypeError("All values must ne int or float")
        self._values = list(new_values)

    @property
    def mean(self):
        return sum(self._values) / len(self._values) if self.values else 0.0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("name cannot be empty")
        self._name = new_name
"""

class Feature:
    def __init__(self, name, values):
        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError("All values must be int or float")
        self.name = name
        self.values = list(values)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("name cannot be empty")
        self._name = new_name

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, new_values):
        for v in new_values:
            if not isinstance(v, (int, float)):
                raise ValueError("All values must be in int or float")
        self._values = list(new_values)


    @property
    def mean(self):
        return sum(self._values) / len(self._values) if self._values else 0.0
    
    def __getitem__(self, index):
        return self._values[index]
    
    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must ne int or float")
        self._values[index] = value

# Test 1: Basic creation and mean
f = Feature("sales", [10, 20, 30])
print(f"Name: {f.name}")        # Expected: Name: sales
print(f"Values: {f.values}")    # Expected: Values: [10, 20, 30]
print(f"Mean: {f.mean}")        # Expected: Mean: 20.0

# Test 2: Indexing
print(f"f[1]: {f[1]}")          # Expected: f[1]: 20
f[1] = 25
print(f"After f[1] = 25:")
print(f"Values: {f.values}")    # Expected: Values: [10, 25, 30]
print(f"Mean: {f.mean}")        # Expected: Mean: 21.666666666666668

# Test 3: Property setters
f.name = "q1_sales"
print(f"New name: {f.name}")    # Expected: New name: q1_sales

f.values = [5, 15, 25]
print(f"New values: {f.values}") # Expected: New values: [5, 15, 25]
print(f"New mean: {f.mean}")     # Expected: New mean: 15.0

# Test 4: Validation errors (should raise exceptions)
try:
    f.name = ""  # Should raise ValueError
except ValueError as e:
    print(f"Name validation: {e}")  # Expected: Name validation: name cannot be empty

try:
    f.values = [1, 2, "invalid"]  # Should raise ValueError
except ValueError as e:
    print(f"Values validation: {e}")  # Expected: Values validation: All values must be in int or float

try:
    f[0] = "invalid"  # Should raise TypeError
except TypeError as e:
    print(f"Index validation: {e}")  # Expected: Index validation: Value must ne int or float    