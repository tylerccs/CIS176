# This is the main file for Programming Exercise 5 for CIS176 by Tyler Cooper

# initalize input variables
class_a = int(input("Enter the number of Class-A seats sold: "))
class_b = int(input("Enter the number of Class-B seats sold: "))
class_c = int(input("Enter the number of Class-C seats sold: "))


# create the function for the calculation
def calculate(class_a, class_b, class_c):
    income_a = class_a * 20
    income_b = class_b * 15
    income_c = class_c * 10

    total_income = income_a + income_b + income_c

    print(f"Class-A income is: ${income_a}")
    print(f"Class-B income is: ${income_b}")
    print(f"Class-C income is: ${income_c}")

    print(f"Total income is: ${total_income}")


# call the function

calculate(class_a, class_b, class_c)
