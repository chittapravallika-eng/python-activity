products = ["Books", "Pens", "Notebooks"]
opening = [100, 200, 150]
received = [50, 100, 50]
dispatched = [80, 120, 100]
for i in range(len(products)):
    closing = opening[i] + received[i] - dispatched[i]
    print("\nProduct:", products[i])
    print("Opening stock:", opening[i])
    print("Received:", received[i])
    print("Dispatched:", dispatched[i])
    print("Closing stock:", closing)

    if closing < 50:
        print("Replenishment required")
    else:
        print("Stock sufficient")
