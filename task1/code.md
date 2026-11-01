# Railway Fare Calculator Using Python

## 1. Problem Statement

Write a Python program to calculate railway ticket fare based on journey distance, passenger age, and selected travel class (Sleeper or AC). Provide a 10% concession for passengers aged 60 years or above and add Rs. 50 as reservation charges. Display the final railway fare. If an invalid class is selected, display an error message.

## 2. Algorithm

1. Start the program.
2. Enter the journey distance in kilometres.
3. Enter the passenger's age.
4. Display the travel class options:

   -
   1. Sleeper
   1)
   2. AC
5. Enter the class choice.
6. If the choice is 1, calculate fare as distance × 1.5.
7. If the choice is 2, calculate fare as distance × 3.
8. Otherwise, display "Invalid class".
9. Check whether the fare is greater than zero.
10. If the passenger's age is 60 or above, apply a 10% concession.
11. Add Rs. 50 as reservation charges.
12. Display the final railway fare.
13. Stop the program.

## 3. Flowchart (Mermaid)

Here is the flowchart in a simple format that you can copy and draw in your assignment.

## Railway Fare Calculator – Flowchart


You can use this flowchart directly as a reference for drawing it neatly in your record book.
## 4. Sample Input


Enter journey distance in km: 200
Enter passenger age: 65
1. Sleeper
2. AC
Choose class: 1

## 5. Sample Output


Final railway fare: Rs. 320.0


## 6. Calculation

 Distance = 200 km
 Age = 65 years
 Class = Sleeper
 Basic fare = 200 × 1.5 = Rs. 300
 10% concession = Rs. 30
 Fare after concession = Rs. 270
 Reservation charge = Rs. 50

Final Railway Fare = Rs. 320.0
