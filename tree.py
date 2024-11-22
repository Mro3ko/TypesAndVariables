#c=pi*d-->d=c/pi
import math
c=float(input("Enter tree circumference: "))
d=round(c/math.pi,2)
d=d>50
print(f"Tree can be cut down: {d}")