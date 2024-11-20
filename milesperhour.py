speed_kmh=input("what's your speed in km/h?")
speed_kmh=float(speed_kmh)
speed_ms=speed_kmh*1000/3600
speed_ms=round(speed_ms,2)
print("it's: ",speed_ms,"m/s")