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

#Write your code below this line 👇
#Users choice
import random 
options = [rock, paper, scissors]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice1 = int(user_choice)
output = options[user_choice1]
print(output)
#Computers random choice
computer_choice = random.choice(options)
print(computer_choice)
#Possible Outcomes
if output == computer_choice:
  print("It is a tie!")
if output == rock:
  if computer_choice == paper:
    print("You lose, Computer Wins!")
  elif computer_choice == scissors:
    print("Congrats, Human Wins!")
if output == paper:
  if computer_choice == rock:
    print("CongratsHuman Wins!")
  elif computer_choice == scissors:
    print("You lose, Computer Wins!")
if output == scissors:
  if computer_choice == rock:
    print("You lose, Computer Wins!")
  elif computer_choice == paper:
    print("Congrats, Human Wins")
