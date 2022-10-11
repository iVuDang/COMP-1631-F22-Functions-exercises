''' 
Purpose: 
 * My solution attempts to exercises for COMP 1631-002 F22 - Functions exercises. 

Citations:
 * Problems provided by prof. Patrick Perri, Mount Royal University.  
'''

# Input , processing, and output - 8 problems
'''
1/8. Sales Prediction
A company has determined that its annual profit is typically 23 percent of total sales. 
Write a program that asks the user to enter the projected amount of total sales, then displays the profit that will be made from that amount.
'''

def findProfit(totalSales):
  annualProfit = 0.23 * totalSales
  annualProfitStr = f'Estimated profit is ${annualProfit}'
  print(annualProfitStr)

def main():

  theTotalSales = float(input("Enter totals sales:")) #use the'' in front to indicate final variable
  findProfit(theTotalSales)

main()



'''
2/8. Land Calculation
One acre of land is equivalent to 43,560 square feet. 
Write a program that asks the user to enter the total square feet 
in a tract of land and calculates the number of acres in the tract.
'''

def calcAcres(squareFeet):
    ACRES = 43560
    sqftInAcres = squareFeet / ACRES
    acresStr = f'The number of acres in the tract are {sqftInAcres}'

    print(acresStr)


def main():
    theSqftInAcres = float(
        input("Enter the total square feet of the tract of land:"))

    calcAcres(theSqftInAcres)

main()


# Functions - 7 problems

'''
4/7. Total Purchase
A customer in a store is purchasing five items. Write a program that asks for the price of each item, 

then displays the subtotal of the sale, 
the amount of sales tax, 
and the total. 

Assume the sales tax is 5 percent.

'''

# PART A - function to perform desired output
def totalPurchase(price1, price2, price3, price4, price5):
  TAX = 0.05

  subTotal = price1 + price2 + price3 + price4 + price5
  salesTax = subTotal * TAX
  totalWithTax = subTotal * (1 + TAX)

  receiptStr = f' Subtotal: ${subTotal}\n Sales tax: ${salesTax}\n Total with taxes: ${totalWithTax}'

  print(receiptStr)

# PART B - main function to take input from user, and call prev function

def main():
  thePrice1 = float(input("Price of first item?:"))
  thePrice2 = float(input("Price of second item?:"))
  thePrice3 = float(input("Price of third item?:")) 
  thePrice4 = float(input("Price of fourth item?:"))
  thePrice5 = float(input("Price of fifth item?:"))

  totalPurchase(thePrice1, thePrice2, thePrice3, thePrice4, thePrice5)             
main()



'''
5/7. Feet to Inches

One foot equals 12 inches. 

Write a function named feet_to_inches that accepts a number of feet as an argument and returns the number of inches in that many feet. 

Use the function in a program that prompts the user to enter a number of feet then displays the number of inches in that many feet.
'''

# PART A - The function for an output
def feet_to_inches(ft):
  INCHESPERFEET = 12

  feet = ft * INCHESPERFEET

  print(feet)


# PART B - main function to take input and call on previous functions 
def main():
  theFeet = float(input("Enter number of feet:"))

  feet_to_inches(theFeet)


main()



'''
6/7. Falling Distance

When an object is falling because of gravity, the following formula can be used to determine the distance the object falls in a specific time period:

 distance = (1/2) * (g)(t)**2 

The variables in the formula are as follows: 
d is the distance in meters, 
g is 9.8, and 
t is the amount of time, in seconds, that the object has been falling.

Write a function named falling_distance that accepts an object’s falling time (in seconds) as an argument. 

The function should return the distance, in meters, that the object has fallen during that time interval.

'''

# PART A - function for output

def falling_distance(seconds):
  GRAVITY = 9.8 # meters per second
  secondsSquared = seconds**2
  
  distanceMeters = (GRAVITY * secondsSquared)/2

  print(distanceMeters)


# PART B - main function to take user input and call previous functions

def main():

  theSeconds = float(input("Enter falling time in seconds:"))

  falling_distance(theSeconds)


main()



'''
7/7. Future Value

Suppose you have a certain amount of money in a savings account that earns compound monthly interest, and you want to calculate the amount that you will have after a specific number of months. The formula is as follows:

F = P * (1 + i)**t

The terms in the formula are:
•  F is the future value of the account after the specified time period.
•  P is the present value of the account.
•  i is the monthly interest rate.
•  t is the number of months.

Write a program that prompts the user to enter the account’s present value, monthly interest rate, and the number of months that the money will be left in the account. 

The program should pass these values to a function that returns the future value of the account, after the specified number of months. 

The program should display the account’s future value.
'''


# PART 1 - function to output
def calcFV(PV, Rate, Nper):
  rateOne = (1 + Rate)
  rateSquareN = rateOne ** Nper

  fvCalc = PV * rateSquareN

  print(fvCalc)

# PART 2 - main function to take user input and 
def main():
  thePV = float(input("Enter the account's present value:"))
  theRate = float(input("Enter the monthly interest rate:"))
  theNper = float(input("Enter number of months the money will stay in the account:"))

  calcFV(thePV, theRate, theNper)


main()

  



