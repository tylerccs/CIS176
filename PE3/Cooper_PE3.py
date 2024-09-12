# This is a program written by Tyler Cooper for CIS176 Programming Exercise 3

# The goal of this program is a game thats objective is to get to exactly one dollar
# it take a user input for pennies, nickels, dimes, and quarters and returns statements based on if you succeed or fail
import progressbar as pb


# This function takes the user input and calculates the total amount of money
def change_counting_game():
    print("Welcome to tsc's Change Counting Game!")
    print("In this robust minigame you must enter the number of coins to make exactly one dollar.")

    pennies = int(input("Enter the number of pennies: "))
    nickels = int(input("Enter the number of nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))
    
    # initialize the progress bar for the calculation
    bar = pb.ProgressBar(maxval=1).start()
    bar.update(0)
    
    total_cents = (pennies * 1) + (nickels * 5) + (dimes * 10) + (quarters * 25)
    total_dollars = total_cents / 100
    
    # update the progress bar
    bar.update(1)
    bar.finish()

    if total_dollars == 1.0:
        print("Congratulations! You've won the game. You're really good with numbers!")
    elif total_dollars < 1.0:
        print(f"Sorry, that's only ${total_dollars:.2f}. It's less than one dollar. But you can try again!")
    else:
        print(f"Sorry, that's ${total_dollars:.2f}. It's more than one dollar. Keep trying!")

if __name__ == "__main__":
    change_counting_game()