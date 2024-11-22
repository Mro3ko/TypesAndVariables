import random
dice_roll=random.randint(1,6)
a=int(input("Try to guess a number from 1 to 6: "))
result=a==dice_roll
print(f"You win: {result}")