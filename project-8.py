#Fuel Consumption and Route Comparison
distance = float(input("Enter distance in km: "))
fuel_price = float(input("Enter fuel price per litre: "))

vehicles = ["Car", "Bike", "Bus"]
mileage = [15, 40, 8]
costs = []

for i in range(3):
    fuel = distance / mileage[i]
    cost = fuel * fuel_price
    costs.append(cost)

    print(vehicles[i])
    print("Fuel required =", round(fuel, 2))
    print("Travel cost =", round(cost, 2))

minimum = min(costs)
index = costs.index(minimum)

print("Cheapest vehicle =", vehicles[index])
print("Lowest cost =", round(minimum, 2))