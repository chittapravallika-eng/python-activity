n = int(input("Enter number of students: "))
students = []

for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter aggregate percentage: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family annual income: "))

    if marks >= 75 and attendance >= 75 and income <= 200000:
        students.append((name, marks))

students.sort(key=lambda x: x[1], reverse=True)

print("Eligible Scholarship Students:")
for student in students:
    print(student[0], student[1])

