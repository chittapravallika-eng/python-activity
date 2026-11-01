
students = []
eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    marks = []

    for j in range(5):
        mark = int(input("Enter marks of subject " + str(j + 1) + ": "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    total = sum(marks)
    aggregate = total / 5

    student = (name, marks, aggregate, attendance, income)
    students.append(student)

    if (aggregate >= 75 and min(marks) >= 60
            and attendance >= 75 and income <= 250000):

        eligible.append((name, aggregate, attendance, income))

    else:
        print(name, "is NOT eligible for scholarship")

for i in range(len(eligible)):
    for j in range(i + 1, len(eligible)):

        name1, marks1, attend1, income1 = eligible[i]
        name2, marks2, attend2, income2 = eligible[j]

        if (marks2 > marks1 or
            (marks2 == marks1 and attend2 > attend1) or
            (marks2 == marks1 and attend2 == attend1
             and income2 < income1)):

            eligible[i], eligible[j] = eligible[j], eligible[i]

print("\n===== SCHOLARSHIP RESULTS =====")

if len(eligible) == 0:
    print("No students are eligible.")

else:
    for i in range(len(eligible)):
        name, aggregate, attendance, income = eligible[i]

        print("\nRank:", i + 1)
        print("Name:", name)
        print("Aggregate:", aggregate, "%")
        print("Attendance:", attendance, "%")
        print("Annual Income: Rs.", income)
        print("Status: Eligible")
