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

class Features:
    def __init__(self, name, values):
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("All values must be int or float")
            self.name = name
            self.values = values
            self.mean = sum(self.values)/len(self.values) if values else 0.0

    def __repr__(self):
        return f"Feature(name={self.name!r}, values={self.values})"

    def __str__(self):
        return f"Feature {self.name} - n={len(self.values)}, mean = {self.mean}"
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value

# Test it:
sales = Features("sales", [10, 20, 30])
print(sales[1])     
sales[1] = 25        
print(sales)