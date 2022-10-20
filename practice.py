from math import copysign
from lib2to3.pytree import convert
from re import X
import string


# user_name = input('Please, enter your name: ')
# # print('Hello, ' + user_name)
# initial = user_name[0]
# print(initial)

# user_age = input('How old are you? ')
# print('You are ' + user_age + ' years old! Nice :)')

# day = int(input())
# month = input()

# print('Cinnamon roll day is celebrated on', month, day)

# dog_breeds = ['shiba', 'akita', 'labrador', 'maltansee']
# print(dog_breeds)
# print(len(dog_breeds))
# Yoko = dog_breeds[-4]
# print(Yoko)
# Gucio = dog_breeds[- 1]
# print(Gucio)

# string_list = list('kinda weird')
# print(string_list)
# print(len(string_list))

# empty_list1 = []
# empty_list2 = list()

# the average amount of money per month
# monthly_money = int(input("How much money do you spend per month ($): "))

# the number of miles per unit of money
# n_miles = 2

# earned miles
# miles_per_month = monthly_money * n_miles

# the distance between London and Paris
# distance = 215

# how many months do you need to get
# a free trip from London to Paris and back
# n_months = (distance * 2 / miles_per_month)

# print(n_months)

# counter = 1
# step = abs(int(input('How many steps?')))
# counter += step
# print(counter)

# duration = int(input())
# daily_food = int(input())
# flight_cost = int(input())
# hotel_night_price = int(input())

# total_cost = (flight_cost * 2) + (duration * daily_food) + \
#     (hotel_night_price * (duration - 1))
# print(total_cost)

# n = abs(int(input('How many squirrels?')))
# k = abs(int(input('How many nuts?')))

# nuts_left = (k % n)
# print(nuts_left)

# h_1 = abs(int(input()))
# m_1 = abs(int(input()))
# s_1 = abs(int(input()))
# h_2 = abs(int(input()))
# m_2 = abs(int(input()))
# s_2 = abs(int(input()))

# time_1 = (s_1 + (m_1 * 60) + (h_1 * 3600))
# time_2 = (s_2 + (m_2 * 60) + (h_2 * 3600))

# time_difference = (time_2 - time_1)
# print(time_difference)

# a = int(input())
# print(a < 10 or a > 250)

# A = int(input())
# B = int(input())

# result = (A % B)
# print(result == 1)

# biscuits = int(input("How many biscuits do you want?"))

# if biscuits > 10:
#     print("Wow, that's a lot!")

# print("Do you want some tea with it?")

# number = abs(int(input()))
# word = input()

# # write a condition for plurals
# if number != 1:
#     print(number, word + "s")
# if number == 1:
#     print(number, word)

# ini_atoms = int(input())
# end_atoms = int(input())

# half_life = 0

# while ini_atoms > end_atoms:
#     ini_atoms = (ini_atoms / 2)
#     half_life += 1

# days = half_life * 12
# print(days)

# N = int(input())
# NI = 1

# while N > 1:
#     NI = NI * N
#     N -= 1

# print(NI)

# N = abs(int(input()))
# NI = 0
# x = 0

# while NI != 55:
#     S = N + NI
#     x += 1
#     NI = abs(int(input()))

# A = round(S / x)

# print(x)
# print(S)
# print(A)

# x = 25
# while x > 0:
#     print(x)
#     x += 3

# number = "77777"
# # print(len(number))

# integer = int(number)
# float_number = float(number)

# my_sum = sum((integer, float_number))
# # print(my_sum)
# print(round(my_sum))

# # finding the minimum and the maximum
# integer = 3
# float_number = 5.4
# my_sum = sum((integer, float_number))

# print(min(integer, float_number))
# print(type(max(integer, float_number, my_sum)))

# help(len)

# print(type(print))

# def multiply(x, y):
#     return x * y


# a = multiply(3, 5)
# b = multiply(55, 2)

# print(a + b)

# def welcome():
#     print("Hello")


# def lazy_function(param):
#     pass

# def send_postcard(address, message):
#     print("Send message to: ", address)
#     print("With the message: ", message)


# send_postcard("Białozora 39, Wwa", "Nie jestem przekonana, czy to zadziała...")


# def c_to_f(temp_c):
#     temp_f = temp_c * 9 / 5 + 32
#     return round(temp_f, 2)


# water_bp = c_to_f(100)


# print(water_bp)

# def closest_higher_mod_5(x):
#     remainder
#     return min(y)

# def mi_to_km(miles):
#     return miles * 1.609

# print(mi_to_km(100))

# def captain_adder(name):
#     print("captain", name)

# name = "Basia"
# print(captain_adder(name))

# def is_even(number):
#     return number % 2 == 0

# print(is_even(8))

# import math

# # your code here


# def new_math_factorial(x):
#     print("Don't cheat!")


# math.factorial = new_math_factorial

# # don't delete this line, please
# math.factorial(23)

# today = input()
# if today == "holiday":
#     print("Lucky you!")
# else:
#     print("Soon, my friend, soon :,)")

# rain = False
# print("It's such a rainy day..." if rain is True else "Sun is also good")

# a = int(input())
# b = int(input())

# print(a if a >= b else b)
# print(b if b <= a else a)

# i = 1
# for i in range(1,6):
#     if i == 1:
#         print(i, 'little bear')
#     else:
#         print(i, 'little bears')
#     print('Wondering what to do')
#     print('Along came another')
#     print('Then there were', i+1, '!')


# from string import digits

# print(digits)

# from random import choice

# print(choice(['1', '2', '3']))

# # place `import` statement at top of the program
# x = float(input())
# y = float(input())

# print(copysign(x, y))

# # don't modify this code or the variables may not be available
# x, y = map(float, input().split(' '))

# # place `import` statement at top of the program
# from random import seed
# from random import randint

# # don't modify this code or variable `n` may not be available
# n = int(input())

# # put your code here
# seed(n)
# print(randint(-100, 100))

# oceans = ['Atlantic', 'Pacific', 'Indian', 'Southern', 'Arctic']
# for ocean in oceans:
# #     print(ocean)

# for char in 'magic':
#     print(char)

# for _ in range(1, 15, 3):
#     print(_)

# word = input()
# for char in word:
#     print(char)

# times = int(input("How many times should I say hello?"))
# for n in range(times):
#     print("Hello")

# names = ["Basia", "Yoko", "Rafał", "Pasztet"]
# surnames = ["Random", "Większy random", "Największy random"]

# for name in names:
#     for surname in surnames:
#         print(name, surname)

# tel_num = input()

# num_name = ["zero", "one", "two", "three", "four",
#             "five", "six", "seven", "eight", "nine"]

# for i in tel_num:
#     print(num_name[int(i)])

# a = [1, 2, 3]
# b = [1, 2, 3]

# # print(a == b)

# # print(id(a))
# # print(id(b))

# print(a is b)
# print(a == b)
# # print(a is not b)

# a = 10000
# b = 10000

# print(a is b)


# def say_hi(name=None):
#     if name is None:
#         print("Hello!")
#     else:
#         print("Hello " + name)

# say_hi()
# say_hi("Nick")

# def object_with_beautiful_identity(i):
#     for i in range(10_000):
#         # Change the next line
#         if id(i) % 1000 == 888:
#             return i
#         else:
#             return "nope"

# print(object_with_beautiful_identity(8888))

# def print_book_info(title, author=None, year=None):
#     #  Write your code here
#     if year is None:
#         if author is None:
#             print('"' + title + '"')
#         else:
#             print('"' + title + '"' + " was written by " + author)
#     else:
#         if author is None:
#             print('"' + title + '"' + " was written in " + year)
#         else:
#             print('"' + title + '"' + " was written by " + author + " in " + year)

# print_book_info("Harry Potter", None, "2022")

string = "hello"
new_string = string
string = "world"

print(string, id(string))            # world 4336233136
print(new_string, id(new_string))    # hello 4336233024