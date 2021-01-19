import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "@#$%!&*"

print("Welcome to the password generator")

upper = input("Do you want uppercase letters? Y/N ")
lower = input("Lowercase? Y/N ")
nums = input("Numbers? Y/N ")
syms = input("Symbols? Y/N ")
length_input = int(input("What's the length of the password? "))
amount_input = int(input("How many passwords do you want? "))

inputs = [upper, lower, nums, syms]
control = []

for x in inputs:
    if x == "Y" or x == "y":
        x = True
        control.append(x)
    elif x == "N" or x == "n":
        x = False
        control.append(x)
    else:
        print("error")
        break

all = ""

if control[0]:
    all += uppercase_letters
if control[1]:
    all += lowercase_letters
if control[2]:
    all += digits
if control[3]:
    all += symbols

length = length_input
amount = amount_input

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
