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

# Calculate total cost of 4 years of tuition
total_cost = 0
for year in range(1, years + 1):
    total_cost += tuition * (1 + increase_rate) ** (year - 1)
print(f"Total cost of 4 years of tuition is ${total_cost:,.2f}")
# End of program
# Output:
# Year 1 tuition is $4,000.00
# Year 2 tuition is $4,200.00
# Year 3 tuition is $4,410.00
# Year 4 tuition is $4,630.50
# Total cost of 4 years of tuition is $17,240.50
# Process finished with exit code 0
