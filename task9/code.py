price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
if total >= 2000:
    discount = total * 0.10
elif total >= 1000:
    discount = total * 0.05
else:
    discount = 0
final_bill = total - discount
print("Total amount: Rs.", total)
print("Discount: Rs.", discount)
print("Final bill: Rs.", final_bill)

