name = input("Enter employee name: ")
basic_pay = float(input("Enter basic pay: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))
gross_salary = basic_pay + allowances + overtime + incentives
if gross_salary <= 20000:
    deduction = 0
elif gross_salary <= 40000:
    deduction = gross_salary * 0.05
else:
    deduction = gross_salary * 0.10
net_salary = gross_salary - deduction
print("Employee Name:", name)
print("Basic Pay: Rs.", basic_pay)
print("Allowances: Rs.", allowances)
print("Overtime Pay: Rs.", overtime)
print("Incentives: Rs.", incentives)

print("Gross Salary: Rs.", gross_salary)
print("Total Deduction: Rs.", deduction)
print("Net Salary: Rs.", net_salary)

