distance = float(input("Enter journey distance in km: "))
age = int(input("Enter passenger age: "))
print("1. Sleeper")
print("2. AC")
choice = int(input("Choose class: "))
if choice == 1:
    fare = distance * 1.5
elif choice == 2:
    fare = distance * 3
else:
    fare = 0
    print("Invalid class")
if fare > 0:
    if age >= 60:
        fare = fare * 0.90

    fare = fare + 50

    print("Final railway fare: Rs.", fare)
