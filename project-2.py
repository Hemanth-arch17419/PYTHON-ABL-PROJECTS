#Employee Payroll
name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
overtime = float(input("Enter overtime pay: "))

gross = basic + allowance + overtime

if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 50000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.15

net = gross - deduction

print("Employee:", name)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)