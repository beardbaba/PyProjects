import os
def clear():
    os.system('cls')

details = []    
# other == "no"

print("Welcome to the secret auction program.")

name = input("What is your name? : ")
bid = int(input("What's your bid? : $"))
# another = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

def user(naam,daam):
        details.append({
            "name":naam,
            "bid":daam
        })

# if other == yes:
#     clear()

# clear()


user(name,bid)

print(f"The winner is {details[0]['name']} with a bid of ${details[0]['bid']}")
print(details)