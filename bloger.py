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

"""
my_list = list(range(5))

while my_list:
    element = my_list.pop()
    print(f"element: {element}")

print(my_list)
"""

"""
while True:
    print("Inifinite loop")
"""
""" how to quit infinite loop
while True:
    answer = input("Enter a number:")
    if answer == "quit":
        break
    print(f"You entered: {answer}")
"""

""" Martingale's law
import random

HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]

def flip_coin():
    return random.choice(COIN_VALUES)

def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        #print("==========") # To see different cycles of game
        steps_to_loose +=1
        current_funds -= current_bet
        #print(f"{current_funds=}, {current_bet=}")
        flipped_coin_value = flip_coin()
        
        if flipped_coin_value ==HEADS:
            win = current_bet * 2
            #print(f"{win=}")
            current_funds += win
            current_bet = min_bet
        else:
            #print("loose")
            current_bet *=2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds
    return steps_to_loose

def simulate_martingale_for_n_players(
        *, 
        starting_funds: int, 
        min_bet: int, 
        max_bet: int, 
        n_games: int
        ) -> float:
    total_steps_to_loose = 0
    for i in range(n_games):
        step_to_loose = play_martingale(
            starting_funds= starting_funds, 
            min_bet=min_bet, 
            max_bet = max_bet
            )
        total_steps_to_loose +=step_to_loose

    return total_steps_to_loose / n_games



print(simulate_martingale_for_n_players(
    starting_funds = 100000, 
    min_bet =1, 
    max_bet =100000, 
    n_games = 10
    )
)
"""
"""
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

"""
#for key, value in person.items():
#    print(key)
#    print(value)
"""

additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

person.update(additional_person_info) #person = person | additional_person_info

print(person)
"""

# задание
# Есть список словарей со студентами `students`. В каждом объекте есть имя и фамилия студента,
# а также список оценок (целых чисел). Нужно написать функцию get_best_students, которая берёт студентов и находит того,
# у кого средний балл наибольший. Возвращает функция список студентов с лучшим баллом. У некоторых студентов в оценках
# есть None: их среднюю оценку мы считаем равной 0.


students = [
    {"name": "John", "surname": "Doe", "grades": [5, 5, 4, 4]},
    {"name": "Jane", "surname": "Doe", "grades": [4, 3, 4, 3, 5]},
    {"name": "Bill", "surname": "Gates", "grades": [5, 5, 5, 3]},
    {"name": "Steve", "surname": "Jobs", "grades": [3, 5, 4, 3, 3, 5]},
    {"name": "Guido", "surname": "Van Rossum", "grades": [5, 3, 5, 4, 5, 5, 3, 5]},
    {"name": "Elon", "surname": "Musk", "grades": None}]


def get_best_students(*, students: list[dict])-> list[dict]:
    best_students =[]
    top_average_grade = 0
    for student in students:
        grade = student["grades"]
        if grade is None:
            average_grade = 0
        else:
            average_grade = sum(grade)/len(grade)
        if top_average_grade < average_grade:
            top_average_grade = average_grade
            best_students = [student]
        elif top_average_grade == average_grade:
            best_students.append(student)
    return best_students

print(get_best_students(students=students))