import random
print("Dice roll simulator")
for x in range(1,6):
    dice_roll= random.randint(1,6)
    print(dice_roll, end=" ")
