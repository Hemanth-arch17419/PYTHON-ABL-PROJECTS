#Food Waste Monitoring
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]

total_prepared = 0
total_served = 0

for day in days:
    print("\n", day)

    prepared = int(input("Enter meals prepared: "))
    served = int(input("Enter meals served: "))

    leftover = prepared - served
    total_prepared += prepared
    total_served += served

    if prepared > 0:
        waste = leftover / prepared * 100
    else:
        waste = 0

    print("Leftover meals =", leftover)
    print("Waste percentage =", round(waste, 2), "%")

    if waste > 10:
        print("High food waste")
    else:
        print("Food waste is acceptable")

print("\nWeekly Summary")
print("Total Prepared =", total_prepared)
print("Total Served =", total_served)
print("Total Leftover =", total_prepared - total_served)