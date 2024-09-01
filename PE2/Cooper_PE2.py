# This is a program created by Tyler Cooper for CIS176 Programming Exercise 2

#define the get_total function
def get_total():
    statesalestax = 0.05
    countysalestax = 0.025
    
    # Get the purchase amount from the user
    purchaseamount = float(input("Enter the purchase amount: "))
    
    # Calculate the state tax, county tax, total tax, and total sale
    statetaxamount = purchaseamount * statesalestax
    countytaxamount = purchaseamount * countysalestax
    totaltax = statetaxamount + countytaxamount
    totalsale = purchaseamount + totaltax
    
    # Display the results
    print("Purchase amount: $", purchaseamount)
    print("State sales tax: $", statetaxamount)
    print("County sales tax: $", countytaxamount)
    print("Total sales tax: $", totaltax)
    print("Total sale: $", totalsale)
    
get_total()