attended = int(input("Enter classes attended: "))
conducted = int(input("Enter total classes conducted: "))
required = float(input("Enter required attendance percentage: "))
if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details")
elif attended * 100 / conducted >= required:
    print("You are already eligible")
else:
    extra = 0

    while (attended + extra) * 100 / (conducted + extra) < required:
        extra = extra + 1

    print("Minimum consecutive classes to attend:", extra)
