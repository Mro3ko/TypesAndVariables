amount=input("What is the price? ")
amount=float(amount)
vat=round(0.23*amount,2)
price=amount+vat
print(f"The amount is {amount} and 23% VAT is {vat}, so in total product costs {price}")