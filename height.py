cm=int(input("Enter your height in cm: "))
feet=cm//30.48
inches=(cm%30.48)//2.54
feet=int(feet)
inches=int(inches)
print(f'I am {cm}cm tall, i.e. {feet} ft {inches} in.')