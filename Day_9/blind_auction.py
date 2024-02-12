import os
def clear():
    os.system('cls')

details = []    

print("Welcome to the secret auction program.")

def intro():
    global name
    global bid
    global should_continue
    name = input("What is your name? : ")
    bid = int(input("What's your bid? : $"))
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    user(name,bid)

def user(naam,daam):
    details.append({
            "name":naam,
            "bid":daam
        })

intro()

while should_continue == "yes":
    clear()
    intro()

def get_bid(amount):
    return amount['bid']

max_bid = max(details, key = get_bid )

print(f"The winner is {max_bid['name']} with a bid of ${max_bid['bid']}")
# print(details)

"""
 Came to the above logic of get_bid function and and max function using this stackoverflow solution and then chatgpt since didn't understand lambda
 https://stackoverflow.com/questions/5320871/how-to-find-the-min-max-value-of-a-common-key-in-a-list-of-dicts & https://chat.openai.com/share/0bc5135a-8dc6-423d-b1a7-aff534023147
"""

"""
Angela's solution is also very simple and easy do check and make a note
https://www.udemy.com/course/100-days-of-code/learn/lecture/19279420#questions/13418268
"""