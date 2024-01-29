# Initialize variables for the total sum and the count of numbers entered
total_sum = 0
count = 0

# Implement a while loop that continues as long as the total sum is less than 100
while total_sum < 100:
    # Prompt the user to enter a number or a space to exit
    user_input = input("Enter a number or press space ( ) to exit: ")
    
    # Check if the user entered a space and if so, break out of the loop
    if user_input == " ":
        break
    
    # If the user enters a number, add it to the total sum and increment the count
    try:
        number = float(user_input)
        total_sum += number
        count += 1
    except ValueError:
        # If the user does not enter a valid number, notify the user and continue
        print("Please enter a valid number or press space ( ) to exit.")

# Once the loop is exited, display the total sum and the count of numbers entered
print("The total sum is:", total_sum)
print("The count of numbers entered is:", count)
