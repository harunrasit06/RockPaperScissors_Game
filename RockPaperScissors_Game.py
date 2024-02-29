import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lost = '''
    _____
---'   __)_
      (____)______
       ___________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
print("Welcome to the Rock, Paper, Scissors Game!")
answer = input("Will you play? Type 'y' or 'n': ")
while answer == "y": 
  user_choice = int(
      input(
          "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
      ))
  computer_choice = random.randint(0, 2)
  if (user_choice == 0 and computer_choice == 2):
      print(f"You chose: rock \n{rock}\n")
      print(f"Computer chose: scissors \n{scissors}\n")
      print("You win!")
  if (user_choice == 0 and computer_choice == 0):
      print(f"You chose: rock \n{rock}\n")
      print(f"Computer chose: rock \n{rock}\n")
      print("Anybody win, Again")
  if (user_choice == 0 and computer_choice == 1):
      print(f"You chose: rock \n{rock}\n")
      print(f"Computer chose: paper \n{paper}\n")
      print(f"You lost! \n{lost}\n")
  
  if (user_choice == 1 and computer_choice == 0):
      print(f"You chose: paper \n{paper}\n")
      print(f"Computer chose: rock \n{rock}\n")
      print("You win!")
  if (user_choice == 1 and computer_choice == 1):
      print(f"You chose: paper \n{paper}\n")
      print(f"Computer chose: paper \n{paper}\n")
      print("Anybody win, Again")
  if (user_choice == 1 and computer_choice == 2):
      print(f"You chose: paper \n{paper}\n")
      print(f"Computer chose: scissors \n{scissors}\n")
      print(f"You lost! \n{lost}\n")
  
  if (user_choice == 2 and computer_choice == 1):
      print(f"You chose: scissors \n{scissors}\n")
      print(f"Computer chose: paper \n{paper}\n")
      print("You win!")
  if (user_choice == 2 and computer_choice == 2):
      print(f"You chose: scissors \n{scissors}\n")
      print(f"Computer chose: scissors \n{scissors}\n")
      print("Anybody win, Again")
  if (user_choice == 2 and computer_choice == 0):
      print(f"You chose: scissors \n{scissors}\n")
      print(f"Computer chose: rock \n{rock}\n")
      print(f"You lost! \n{lost}\n")
  answer = input("Will you play? Type 'y' or 'n': ")
  if answer == "n":
    break


