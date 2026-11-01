consultation = float(input("Enter consultation charge: "))
tests = float(input("Enter test charges: "))
treatment = float(input("Enter treatment charges: "))
total = consultation + tests + treatment
if total >= 5000:
    discount = total * 0.10
else:
    discount = 0
final_bill = total - discount
print("Total bill: Rs.", total)
print("Discount: Rs.", discount)
print("Final bill: Rs.", final_bill)
if final_bill >= 5000:
    print("Classification: High bill")
else:
    print("Classification: Regular bill")

