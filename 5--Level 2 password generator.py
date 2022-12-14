import random
import string
letters = list(string.ascii_letters)
characters = ["!","#","$","%","&","*","+","(",")"]
digits= list(string.digits)
print("Welcome to the password generator!!")
letter_key = int(input("How many letters you want on your password? "))
characters_key = int(input("How many character you want on your password? "))

digit_key = int(input("How many digits you want on your password? "))

# pwletter = []
#
# for i in range(letter_key):
#     pwletter.append(random.choice(letters))
# # print(pwletter)
# first="".join(pwletter)
# pwdigit = []
#
# for j in range(digit_key):
#     pwdigit.append(random.choice(digits))
#
# # print(pwdigit)
# second="".join(pwdigit)
#
# pwcharacter = []
#
# for k in range(characters_key):
#     pwcharacter.append(random.choice(characters))
#
# # print(pwcharacter)
#
# third = "".join(pwcharacter)
#
# password = first+second+third
# print(password)
#
# ###working with list and finally shuffling the list
password = []
for charletter in range(1,letter_key+1):
    password.append(random.choice(letters))
# print(password)

for chardigit in range(1,digit_key+1):
    password.append(random.choice(digits))
# print(password)

for charsymbol in range (1,characters_key+1):
    password.append(random.choice(characters))

# print(password)
random.shuffle(password)
# print(password)

for each in password:
    new_password = "".join(password)


print(f"The final password is: {new_password}")