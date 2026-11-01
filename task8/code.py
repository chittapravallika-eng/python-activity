usage = int(input("Enter monthly data usage in GB: "))
plan_a = 199
plan_b = 299
plan_c = 399
if usage <= 10:
    print("Best plan: Plan A")
    print("Cost: Rs.", plan_a)
elif usage <= 20:
    print("Best plan: Plan B")
    print("Cost: Rs.", plan_b)
else:
    print("Best plan: Plan C")
    print("Cost: Rs.", plan_c)
