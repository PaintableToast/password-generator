import random
import string
import sys

def generatePassword(length, digits, punctuation):
    password = []
    for i in range(length):
        if(bool(digits) & bool(punctuation)):
            password.append(random.choice(string.digits + string.ascii_letters + string.punctuation))
        elif(bool(digits)):
            password.append(random.choice(string.digits + string.ascii_letters))
        elif(bool(punctuation)):
            password.append(random.choice(string.punctuation + string.ascii_letters))
        else:
            password.append(random.choice(string.ascii_letters))
    print(" ")
    print("Your New Password is:")
    return ''.join(password)
print("Enter the Length of your wish password")
length = input()
length = int(length)
print("Set Digits y / n")
digits = input()
digits == digits == 'y'
print("Set Punctuation y / n")
punctuation = input()
punctuation = punctuation == 'y'
print(generatePassword(length, digits, punctuation))