#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_letter = nr_letters + nr_symbols + nr_numbers

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

"""
choice() returns a single random element, while sample() and choices() return a list of multiple random elements. 
sample() is for random sampling without replacement, whereas choices() is for random sampling with replacement.
By without replacement means that the elements can't be used/selected more than once and vice versa

"""

# letters[1] + numbers[4] +symbols[2]
# rand_letter = []
# rand_symbols = []
# rand_numbers = []

# for i in range(nr_letters):
#     rand_letter = str(print(letters[i],end=""))
#     # rand_letter = random.choices(letters)
#     print(rand_letter)
# for i in range(nr_symbols):
#     rand_symbols = str(print(symbols[i],end=""))
#     # rand_symbols = random.choices(symbols)
#     print(rand_symbols)
# for i in range(nr_numbers):
#     rand_numbers = str(print(numbers[i],end=""))
#     # rand_numbers = random.choices(numbers)
#     print(rand_numbers)
    
# print(rand_letter+rand_symbols+rand_numbers)


rand_letter = random.choices(letters,k=nr_letters)
rand_symbol = random.choices(symbols,k=nr_symbols)
rand_number = random.choices(numbers,k=nr_numbers)
# print(rand_letter, rand_symbol) #['U', 'R', 'w', 'Z', 'G', 'b', 'R', 'C', 'M', 'E', 'c', 'l'] ['l', 'x', 'I']
password_sum = rand_letter+rand_symbol+rand_number
# print(password_sum)

ez_password = ""

for x in password_sum:
    ez_password += x
    
print(ez_password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

rand_password = random.sample(password_sum,k = total_letter)

hd_password = "".join(rand_password)
print(hd_password)



