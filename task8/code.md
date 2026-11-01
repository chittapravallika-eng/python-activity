# Mobile Data Plan Recommendation Using Python

## 1. Problem Statement

Write a Python program to recommend the best mobile data plan based on a customer's monthly data usage in GB.

The program should:

- Accept monthly data usage in GB.
- Define three mobile data plans with different prices.
- Recommend Plan A (Rs. 199) if usage is up to 10 GB.
- Recommend Plan B (Rs. 299) if usage is above 10 GB and up to 20 GB.
- Recommend Plan C (Rs. 399) if usage is above 20 GB.
- Display the recommended plan and its cost.

## 2. Algorithm

1. Start the program.
2. Enter monthly data usage in GB.
3. Initialize Plan A cost as Rs. 199.
4. Initialize Plan B cost as Rs. 299.
5. Initialize Plan C cost as Rs. 399.
6. Check whether usage is less than or equal to 10 GB.
7. If yes, recommend Plan A and display its cost.
8. Otherwise, check whether usage is less than or equal to 20 GB.
9. If yes, recommend Plan B and display its cost.
10. Otherwise, recommend Plan C and display its cost.
11. Stop the program.

## 3. Pseudocode


START

INPUT usage

plan_a = 199
plan_b = 299
plan_c = 399

IF usage <= 10 THEN

    DISPLAY "Best plan: Plan A"
    DISPLAY "Cost:", plan_a

ELSE IF usage <= 20 THEN

    DISPLAY "Best plan: Plan B"
    DISPLAY "Cost:", plan_b

ELSE

    DISPLAY "Best plan: Plan C"
    DISPLAY "Cost:", plan_c

END IF

STOP


## 4. Flowchart
```mermaid

flowchart TD
    A([START]) --> B[/Enter monthly data usage in GB/]
    B --> C{Usage <= 10?}
    C -->|Yes| D[Select Plan A]
    D --> E[/Display Plan A and Rs. 199/]
    C -->|No| F{Usage <= 20?}
    F -->|Yes| G[Select Plan B]
    G --> H[/Display Plan B and Rs. 299/]
    F -->|No| I[Select Plan C]
    I --> J[/Display Plan C and Rs. 399/]
    E --> K([STOP])
    H --> K
    J --> K
```
## 5. Sample Input
Enter monthly data usage in GB: 15
## 6. Sample Output
Best plan: Plan B
Cost: Rs. 299
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/495a2d83-5464-49e8-8cb5-6fe52f270654" />

