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
"""

"""
def add_all(*args): #To use multiple arguments
    summary = 0
    for num in args:
        summary+= num
    return summary

values = [1,2,3,4,5]
other_values = [5,6,7,8,9]

print(add_all(*values, *other_values))# to use that function we need to have asterixes as well

def introduce(**kwargs): #kwargs we use for argumets with names; kwargs is a dictionary
    for key, values in kwargs.items():
        print(key)
        print(values)

introduce(name="John", age =30, city = "New York")
"""
"""
def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True
        
    return old_dict, is_modified

product= {"id": 1, "name": "Laptop", "price": 99.99}

structure = modify_dict(old_dict = product, in_stock=True)

print(structure)

structure_2 = modify_dict(old_dict = product, name ="Laptop")
print(structure_2)
"""

###JSON - Java Script Object Notation
"""
import json

book = {
    "title": "1984",
    "author": "George Orwell",
    "isbn": "978-876-456-876",
    "uuid": "a0eythbck-9cb0b-4tfr-bb6d-6bb9bd3wsugi",
}

json_string = json.dumps(book)

print(json_string)
print(type(json_string))

json_string_2 = '{"title": "1984", "author": "George Orwell", "isbn": "978-876-456-876", "uuid": "a0eythbck-9cb0b-4tfr-bb6d-6bb9bd3wsugi"}'

book_2 = json.loads(json_string_2)
print(book_2)
print(type(book_2))
"""

"""
#Modules to call in Pythone
print(globals().keys())

my_int = 1
import json

print(globals().keys()) #after we added my_int and json previously they appeared in the possibilities below
"""
""" To make a request each second to get a price for Bitcoin
import requests
import time

url = 'https://api.binance.com/api/v3/ticker/price'

bitcoin_prices = []

for i in range(30):
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price = float(response.json()['price'])
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices)) #max bitcoin price
print(min(bitcoin_prices)) #min bitcoin price
"""

"""
url = 'https://api.binance.com/api/v3/ticker/price'
response = requests.get(url, params={'symbol': 'BTCUSDT'})

price_object = response.json()

price = float(price_object['price'])

print(price)
""" 
#  задание
#  1. Отправьте на https://api.binance.com/api/v3/ticker/price запрос БЕЗ аргумента params.
#  2. Изучите структуру ответа, сравните её с ответом в запросе без params.
#  3. Напишите код, который найдёт курс Etherium'а к доллару (ETHUSDT) в полученной из запроса структуре.

"""
import requests

url = "https://api.binance.com/api/v3/ticker/price"
response = requests.get(url)

data = response.json()

for r in data:
    if r["symbol"] == "ETHUSDT":
        price_object = r
        break

price = float(price_object['price'])

print(f"ETH/USDT price: {price}")
"""

#List comprehensions
"""
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

#we can only use this code 
squares2 = [x**2 for x in range(10)]
print(squares2)
"""
"""
even_squares = []

for x in range(10):
    if x % 2 == 0:
        even_squares.append(x ** 2)
print(even_squares)


even_squares_2 = [ x **2 for x in range(10) if x % 2 ==0]
print(even_squares_2)
"""
"""
labelled_numbers = []

for num in range(6):
    if num % 2 ==0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd")

print(labelled_numbers)

labelled_numbers_2 = ["even" if num % 2 == 0 else "odd" for num in range(6)]

print(labelled_numbers_2)
"""

"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = []

for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)

print(transpose_matrix)

transpose_matrix_2 = [[row[i] for row in matrix] for i in range(len(matrix))]

print(transpose_matrix_2)
"""

#Class set
#my_set = {1, 2, 3, 4, 5}

#Function sort
"""
fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits)
sorted_fruits_2 = sorted(fruits, reverse = True)

print(sorted_fruits)
print(sorted_fruits_2)

def sort_by_len(element: str) -> int:
    return len(element)

sorted_fruits_3=sorted(fruits, key=sort_by_len)

print(sorted_fruits_3)

people = [
    {"name" : "Alice", "age": 25},
    {"name" : "Bob", "age": 25},
    {"name" : "Charlie", "age": 37},
    {"name" : "Connor", "age": 32},
]

def sort_by_age(person: dict) -> int:
    return person["age"]

sorted_by_age = sorted(people, key = sort_by_age)

print(sorted_by_age)

def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element["age"], element["name"]

sorted_people = sorted(people, key = sort_by_age_name)
print(sorted_people)
"""

#Function filter
"""
def is_even(n: int) -> bool:
    return n % 2 ==0


numbers = [1, 2,3, 4, 5, 6,7, 8]

filtered_numbers = list(filter(is_even, numbers))

print(filtered_numbers)

people = [
    {"name" : "Alice", "age": 25},
    {"name" : "Bob", "age": 17},
    {"name" : "Charlie", "age": 37},
    {"name" : "Connor", "age": 32},
]

def is_adult(person: dict) -> bool:
    return person["age"] >= 18

filtered_people = list(filter(is_adult, people))
print(filtered_people)
"""

#Lambda function
"""
def sort_by_len(element:str) -> int:
    return len(element)

sort_by_len_lambda = lambda element: len (element)

fruits = ["banana", "apple", "cherry", "date"]

longest_word =max(fruits, key=lambda element: len(element))
sorted_words = sorted(fruits, key = lambda element: len(element))
print(longest_word)
print(sorted_words)
"""

#exceptions
"""
def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)

try:
    print(find_average(numbers=[]))
except ZeroDivisionError as error:#error shows exactly what error we face
    print(f"The list is empty: {error}") 
"""

#Class, OOP Objective Orientaated Programming
#str - is a class
# my_string = "Hello, world" is an examplar (object)
"""
class MyClass:# we created new class
    pass

my_class = MyClass()# we created a new examplar
"""

"""
class Ork:
    def __init__(self, level: int) -> None: #__ is dander function
        self.level = level
        self.health_points = 100 * level
        self.attack_power = 10 * level

    def attack(self):
        print(f"Ork attackes with {self.attack_power} power")

    def __str__(self):
        return f"Ork (level: {self.level}, hp: {self.health_points})"

ork = Ork(level = 2)
print(ork.level)
print(ork.health_points)
print(ork.attack_power)

ork.attack()

class Elf:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = 50 * level
        self.attack_power = 15 * level

    def atack(self):
        print(f"Elf attackes with {self.attack_power} power")

    def __str__(self):
        return f"Elf (level: {self.level}, hp: {self.health_points})"
"""   
#We can use inheretance method to make our code less


# задание
# Скопируйте код из предыдущего урока.
# Имплементируйте следующий функционал:
# 1. После убийства персонажа, уровень того, кто убил, повышается на 1.
# 2. Максимальный уровень персонажа - 3.
# 3. При повышении уровня персонажа, происходит отхил, и персонажу прибавляется половина от максимального количества хп.
# 4. Уровень должен повышаться в функции fight
# После имплементации, и запуска функции fight, при вызове должно вывестись:
# Ork is alive Ork (level: 2, hp: 140)
# Elf is dead Elf (level: 1, hp: -4)



class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level
        
    def attack(self, *, target: "Character"):
        #print(
        #    f"{self.character_name} attacks {target.character_name} ({target.health_points} health points)"
        #    f"with {self.attack_power} power"
        #      )
        #target.health_points -= self.attack_power
        #print(f"After attack {target.character_name} hp has {target.health_points}")
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage: int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -=damage

    def is_alive(self) -> bool:
        return self.health_points > 0

    @property
    def defence(self) -> int:
        defence = self.base_defence * self.level
        return defence

    @property
    def max_health_points(self) -> int:
        return self.level * self.base_health_points

    def health_points_percent(self):
        return 100 * self.health_points /self.max_health_points
    

    def __str__(self) -> str:
        return f"{self.character_name} (level: {self.level}, hp: {self.health_points})"
    

class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"
    base_defence = 15

    @property
    def defence(self) -> int:
        defence = super().defence
        if self.health_points < 50:
            defence *= 3 
        
        return defence


#ork = Ork(level=1)
#ork.attack()
#print(ork)

class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"
    base_defence = 10

    def attack(self, *, target: "Character") -> None:
        attack_power = self.attack_power
        if target.health_points_percent() < 30:
            attack_power = self.attack_power * 3
        print(f"Elf attack_power = {attack_power}")
        target.got_damage(damage=attack_power)

    #def attack(self):
    #    print("This method is from class-inheritor")

#elf = Elf(level =2)
#elf.attack()

def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
    
    print(f"Character 1: {character_1}, is_alive: {character_1.is_alive()}")
    print(f"Character 2: {character_2}, is_alive: {character_2.is_alive()}")

ork = Ork(level=1)
elf = Elf(level=1)

fight(character_1 = ork, character_2 = elf)

#Polymorphism - the ability to redefine a language construct for each class
#Encapsulation - restricting access to the components of an object
#Inheritance - a child class contains the attributes and methods of the inherited class

