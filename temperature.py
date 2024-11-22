#podajemy temperaturę z klawiatury w °C
tC=int(input("Enter temperature in °C: "))
#przeliczamy na °F: F=C*9/5+32
tF=tC*9/5+32
#Zwracamy otrzymany wynik
print(f"It is {tF}°F")