price=input("Enter price: ")
discound=input("Enter discount % ")
price=float(price)
discound=float(discound)
price2=(100-discound)/100*price
reduction=round(price-price2,2)
price2=round(price2,2)
print(f"Price with discount: {price2}")
print(f"Reduction: {reduction}")