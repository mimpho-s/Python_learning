import random

#Randomly assing a house to the user
houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
house = random.choice(houses)

print(house)

#Intial Score/Points for the houses
Gryffindor_points = 0
Hufflepuff_points = 0
Ravenclaw_points = 0
Slytherin_points = 0


Q1 = int(input('Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n'))

if Q1 == 1:
    Gryffindor_points = 1 
    Ravenclaw_points = 1
elif Q1 == 2:
    Hufflepuff_points = 1
    Slytherin_points = 1
else:
    print('Wrong input!')

Q2 = int(input("When I'm dead, I want people to remember me as:\n 1) The Good\n 2) The great\n 3) The wise\n 4) The 2bold\n" ))

if Q2 == 1:
    Hufflepuff_points += 2
elif Q2 == 2:
    Slytherin_points += 2
elif Q2 == 3:
    Ravenclaw_points += 2
elif Q2 == 4:
    Gryffindor_points += 2
else:
    print("Wrong input!")

Q3 = int(input("Which kind of instrument most pleases your ear?\n 1) The violin\n 2) The trumphet\n 3) The piano\n 4) The drum\n"))

if Q3 == 1:
    Slytherin_points += 4
elif Q3  == 2:
    Hufflepuff_points += 4
elif Q3 == 3:
    Ravenclaw_points += 4
elif Q3 == 4:
    Gryffindor_points += 4
else:
    print('Wrong input!')

#To determine the winner
