import random 

die1 = random.randint(1,6)
die2 = random.randint(1,6)

total = die1 + die2

while total != 2:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    total = die1 + die2
    if total != 2:
     print("Nope")
    elif total == 2:
        print('Snake eyes!')



# for i in range(0,5):
#  die1 = random.randint(1,5)
#  die2 = random.randint(1,5)

#  total = die1 + die2
#  print(total)


# while True:
#   if total != 2:
#    print("Nope")
#    break
#   else:
#     print('Snake eyes!')