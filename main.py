print("welcome to the greatest pizza place in the world!!")
#welcome statement^
HST = 0.13
MATERIAL = 0.5
RENT = 1
LABOUR = 0.75
# constant variable
diameter = float(input("\"what is the diameter of the pizza you want (in)"))
#gets diameter from the user
subtotal = LABOUR + RENT + (MATERIAL * diameter)
tax = subtotal * HST
#calculating the subtotal and tax
total = subtotal + tax
#final cost
print("your total is: $",(total))
total = round(total, 2)
print("Your total is: $")
#final statement