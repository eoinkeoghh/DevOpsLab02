# Basic program to compute the average of a set of numbers
numbers = []

# Get input from the user
count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Compute the average
average = sum(numbers) / count

# Display the result
print(f"The average of the numbers is: {average}")

