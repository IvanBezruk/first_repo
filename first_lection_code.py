"""
name = "Yo"
age = 45

message = f"My name is {name}. I am {age/3}"

print(message)

message_2 = "My name is %s. I am %d years old" %(name, age)
print(message_2)

print(id(name))
print(id(age))

entertainment = input ("Enter your name:")
print(f'Your favourite routine is {entertainment}')

"""

"""
appartment_number = int(input("Enter number of apartment:"))

#Constants
FLOORS = 5
APARTMENTS_PER_FLOOR = 4

apartments_per_entrance = FLOORS * APARTMENTS_PER_FLOOR
entrance_number = (appartment_number - 1) // apartments_per_entrance + 1
floor_number = ((appartment_number -1) % apartments_per_entrance // APARTMENTS_PER_FLOOR +1)
print(f'Entrance number {entrance_number}, Floor number{floor_number}')

"""
"""
my_list = [1, 4, 78, 6, 235, 235, 347, -421, -25, 0]

my_list.append(16)
print(my_list)

print(my_list[5])
my_list.insert(3, -100)

print(my_list.index(347))
my_list.insert(my_list.index(347), 100000)
print(my_list)

my_list[my_list.index(6)] = None
print(my_list)

my_list[10] = None
print(my_list)
"""

"""
new_list = [[3,5,7],[10,49,84],13,89,21,158]
new_list.sort()
print(new_list)
"""

new_list = [[3,5,7],[10,49,84],13,89,21,158]
print(new_list[0])

my_set = {5,1, "test", "yo"}
print(my_set)

my_set.add("No")
print(my_set)

my_set.remove(1)
print(my_set)

