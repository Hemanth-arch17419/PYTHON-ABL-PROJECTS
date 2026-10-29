#Student Performance Analysis
name = input("Enter student name: ")

marks = []

for i in range(3):
    mark = int(input("Enter exam marks: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("Student:", name)
print("Marks:", marks)
print("Average:", average)

if marks[2] > marks[0]:
    print("Performance improved")
elif marks[2] < marks[0]:
    print("Performance decreased")
else:
    print("Performance unchanged")

if average >= 75:
    print("Excellent")
elif average >= 40:
    print("Good")
else:
    print("Needs improvement")