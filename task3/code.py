expenses = [100, 200, 150]
rate = float(input("Enter exchange rate in rupees: "))
budget = float(input("Enter budget in rupees: "))
total_foreign = sum(expenses)
total_rupees = total_foreign * rate
print("Total foreign expenses:", total_foreign)
print("Total expenses in rupees: Rs.", total_rupees)
if total_rupees <= budget:
    print("Budget status: Within budget")
else:
    print("Budget status: Over budget")

print("Largest expense:", max(expenses))

