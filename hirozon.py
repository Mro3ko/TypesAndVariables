import math
h=input("what's your height in meters:")
h=float(h)
d=3.57*math.sqrt(h)
d=round(d, 2)
print(f"the horison is {d}km away from you")
w=20
d2=3.57*math.sqrt(w)
d2=round(d2,2)
print(f"the horizon is {d2}km away from your hotel window")