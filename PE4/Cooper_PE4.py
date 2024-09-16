# This is the code for PE4 by Tyler Cooper for CIS176

# Initial tuition and constants
initial_tuition = 4000
increase_rate = 0.05
years = 4

# Loop to calculate and print tuition for each year
tuition = initial_tuition
for year in range(1, years + 1):
    print(f"Year {year} tuition is ${tuition:,.2f}")
    tuition *= (1 + increase_rate)  # Apply the 5% increase each year
