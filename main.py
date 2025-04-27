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


answer = input('''\nYou're at a crossroad.\nWhere do you want to go? Type "left" or "right"\n''')
if answer == "left":
    answer = input('''\nYou've come to a lake.\nThere is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n''')
    if answer == "swim":
        print('\nYou get attacked by an angry trout.\nGame Over.')
    if answer == "wait":
        print('\nYou found the treasure!\nYou Win!')
        exit()
    else:
        print('\nYou fell into a hole. Game Over.\nTry to restart')
if answer == "right":
    answer = input('''\nYou arrive at the island unharmed.\n There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n''')
    if answer == "red":
        print("\nIt's a room full of fire.\nGame Over.")
    if answer == "yellow":
        print("\nYou enter a room of beasts.\nGame Over.")
    if answer == "blue":
        print("\nYou chose a door that doesn't exist.\nGame Over.")
    else:
        print('\nYou fell into a hole. Game Over.')
else:
    print('\nYou fell into a hole. Game Over.\nTry to restart')