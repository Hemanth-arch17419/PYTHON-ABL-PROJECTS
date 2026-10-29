#Electricity Billing
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 150 + (units - 100) * 2.5
elif units <= 300:
    bill = 400 + (units - 200) * 4
else:
    bill = 800 + (units - 300) * 6

bill = bill + 50
print("Electricity Bill =", bill)