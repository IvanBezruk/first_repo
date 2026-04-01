#print("Hello", "world", sep=", ")

""""
print("Hello", "world", end=", ")
print("not here")
"""
"""
name, age = "Alice", 25
print(name, age, sep =", ")
"""
"""
variable = "1"
print(type(variable))
"""
"""
entrance = 5
aparts = 20
number_apartments = 4
user_input = int(input("Ente the apartment number: "))

print("Entrance number: ", (user_input-1)//aparts+1)
print("Floor number: ", (user_input -1) % aparts//4 + 1)
"""
"""
my_str = "  Hello, here I am   "
print(my_str.upper())
print(my_str.strip())
print(my_str.replace("am", "was").strip())
"""

""" Strings
name = "Alice"
age = 25

result = "My name is %s and my age is %d years old." %(name, age)
print(result)
"""

"""
#Lists
fruits = ["apple", "cherry", "banana"]
my_list = ["cocoa"]

fruits += my_list
fruit = fruits.pop()

print(fruits)

list1 = ["big", "small", "medium"]
list2 = ["make", "do", "right"]
list1.extend(list2)
list1.reverse()
list1[0], list1[3] = list1[3], list1[0]
print(list1)
"""


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
new_numbers = numbers[-2:-len(numbers):-1]
print(new_numbers)
"""

"""
greeting = "Hello, world!"
count_o = 0
for char in greeting:
    if char == "o":
        count_o += 1
        print(char)
print(count_o)
"""
"""
for num in numbers:
    if num %2==0:
        continue
    if num ==9:
        break
"""
"""
for i in range(len(numbers)):
    numbers[i]+=1

print(numbers)
"""
"""
greetings = "Hello, world!"

index = []
count = 0

for i in range (len(greetings)):
    if greetings[i] == "o":
        count+=1
        index.append(i)
print(count)
print(index)
"""

"""
first_number = list(range(10))
second_number = list(range(10))

for i in first_number:
    for ii in second_number:
        print(f"{i} * {ii} = {i*ii}")
"""
"""
DEFAULT_LEVEL_EXPERIENCE = 200

def is_level_up(current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >=DEFAULT_LEVEL_EXPERIENCE:
        level_up = True
    
    return level_up

print(is_level_up(150, 60))
print(is_level_up(10, 60))
"""


