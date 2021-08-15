#Password Generator Project
import random

lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many lower case letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))
lower_letters = int(nr_letters/2)
password_basic = []
counter = 0

for x in range(0,nr_letters):
  if(x%2==0):
    password_basic.append(upperCase[random.randint(0,(len(upperCase)-1))])
  else:
    password_basic.append(lowerCase[random.randint(0,(len(lowerCase)-1))])

for x in range(0,nr_symbols):
  password_basic.append(symbols[random.randint(0,(len(symbols)-1))])
for x in range(0,nr_numbers):
  password_basic.append(numbers[random.randint(0,(len(numbers)-1))])

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(f"Password basic form is: {password_basic}")

# password_final = []
# for x in range(0, len(password_basic)-1):
#   password_final.append(password_basic.pop(random.randint(0,len(password_basic)-1)))

random.shuffle(password_basic)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print(f"Password final form is: {password_basic}")
for c in password_basic:
  print(c, end="")
print("")