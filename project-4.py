#Campus Event Financial Planning
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
food = float(input("Enter food cost: "))
transport = float(input("Enter transport cost: "))
sponsorship = float(input("Enter sponsorship: "))

participants = int(input("Enter participants: "))
fee = float(input("Enter registration fee: "))

cost = venue + equipment + food + transport
income = participants * fee + sponsorship
balance = income - cost

print("Total Cost =", cost)
print("Total Income =", income)
print("Balance =", balance)

if balance >= 0:
    print("Event is profitable")
else:
    print("Event has a loss")