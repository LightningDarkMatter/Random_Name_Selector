import random

name_string = input("Give me everyone's names, seperated by a coma: ")
names = name_string.split(",")

pick = random.choice(names)

print("The random name is: " + pick)
