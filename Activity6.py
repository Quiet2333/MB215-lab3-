##Python Program for Demonstrating Different Uses of for Loops

# For loop with range to print even numbers from 2 to 20
print("Even numbers from 2 to 20:")
for number in range(2, 21, 2):  # starts at 2, ends before 21, steps by 2
    print(number, end=" ")
print()  # for a new line

# Nested for loop to create a multiplication table for numbers 1 to 3
print("\nMultiplication table for numbers 1 to 3:")
for i in range(1, 4):  # outer loop for numbers 1 to 3
    for j in range(1, 11):  # inner loop for range 1 to 10
        print(f"{i} * {j} = {i*j}", end="\t")  # tab-separated multiplication entries
    print()  # new line after each row of the table

# For loop to reverse a string. Note : Use ‘Reserved’ keyword
# Assuming 'Reserved' is a typo and should be 'reversed'
print("\nReversing the string 'Hello':")
for char in reversed('Hello'):  # 'reversed' is the correct keyword, not 'Reserved'
    print(char, end=" ")
print()  # for a new line
