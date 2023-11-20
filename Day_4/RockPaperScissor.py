import random

rock = '''

Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice in range(3):
    if list[user_choice] == rock:
        print(f"{rock}")
    elif list[user_choice] == paper:
        print(f"{paper}")
    else:
        print(f"{scissors}")
    
    rand_choice = random.choice(list)
    print(f"Computer Choose:\n{rand_choice}")

    computer_choice = list.index(rand_choice)
    # print(computer_choice)# yaahan pe index ki value aarhi
    
    if user_choice == computer_choice:
        print("That's a tie")
    elif user_choice == 0:
        if computer_choice == 1:
            print("!!Computer Wins!!")
        elif computer_choice == 2:
            print("!!User Wins!!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("!!User Wins!!")
        elif computer_choice == 2:
            print("!!Computer Wins!!")
    elif user_choice == 2:
        if computer_choice == 0:
            print("!!Computer Wins!!")
        elif computer_choice == 1:
            print("!!User Wins!!")       
else:
    print("Wrong Input SAAARRRRR!!!!")