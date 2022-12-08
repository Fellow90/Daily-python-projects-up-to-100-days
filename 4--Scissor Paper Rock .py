


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

RPS = [rock, paper, scissors]
user_choose = int(
    input("Please select 0 for rock, 1 for paper and 2 for scissor: "))
print(f"Your choice is: {RPS[user_choose]}")
computer_choose = random.randint(0, len(RPS) - 1)
print(f"Computer's choice is: {RPS[computer_choose]}")
if user_choose < computer_choose:
    if computer_choose - user_choose == 2:
        print("Congratulations!! You won", user_choose, "and", computer_choose)
    else:
        print("Sorry !! The computer won", user_choose, "and", computer_choose)
elif computer_choose == user_choose:
    print("Sorry !! It is a draw of", user_choose, "&", computer_choose)
elif user_choose - computer_choose == 2:
    print("Sorry !! The computer won", user_choose, "and", computer_choose)
else:
    print("Congratulations!! You won", user_choose, "and", computer_choose)
