#Examination Result
marks = []
subjects = ["Python", "Maths", "English", "Physics", "Chemistry"]

for subject in subjects:
    mark = int(input("Enter marks in " + subject + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage)

if min(marks) >= 35:
    print("Result: Pass")

    if percentage >= 75:
        print("Grade: Distinction")
    elif percentage >= 60:
        print("Grade: First Class")
    else:
        print("Grade: Pass Class")
else:
    print("Result: Fail")