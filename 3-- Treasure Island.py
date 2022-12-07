#Treasure island project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
lr = input("You are at a cross road! Do you want to go left or right?")
if lr == "left":
    sw = input(
        "You are at the middle of the lake! Do you want to swim or wait?")
    if sw == 'wait':
        wd =input(
                "Wow! You came to the middle of the island. Which door do you want to choose? red , blue or yellow?"
            )
        if wd == 'red':
            print("Oops! You got burnt by the fire. Game Over!!")
        elif wd == 'blue':
            print("Sorry! You got caught by the beasts. Game Over!!")
        elif wd == 'yellow':
            print("Congratulations! You win!!")
        else:
            print("Game Over!!")
    else:
        print("Oops!! You are attacked by a trought. Game Over!!")

else:
    print("You fell into a hole. Game Over!!")