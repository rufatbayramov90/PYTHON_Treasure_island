box = ('''
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
closeBox =('''

       --           --
         \  _---_  /
          \/     \/
           |() ()|  Game
            \ + /   Over
           / HHH /
          /  \_/  /
        --          --
    `""""-""""""""""""""""""""""""""-""""`
''')


print("Welcome to Treasure Island")
print("Your mission is to find the treasure") 

choose = input("Where do you want to go? Left or Right").lower()
if choose == "left":
    choose_one = input('You have come to a lake."wait" to wait for a boaT."swim" to swim aceoss').lower()
    if choose_one == "wait":
        choose_two = input('What color do you choose? yellow , red or blue').lower()
        if choose_two == "red":
            print(f"It's a room full of fire.GAME OVER {closeBox}")
        elif choose_two ==" yellow":
            print(f"You chose a door that doesn't exist. Game Over  {closeBox}")
        elif choose_two == "blue":
            print(f"You Win!!! {box}")
        else:
            print(f"You chose a door that doesn't exist. GAME OVER   {closeBox}")
    else:
       print(f"You should have waited. GAME OVER {closeBox}") 
else:
    print(f"You did not choose the correct option.GAME OVER   {closeBox}")
    

 