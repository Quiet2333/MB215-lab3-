# Step 1: Declare two Boolean variables
bool_true = True
bool_false = False

# Step 2: Demonstrate logical operations (AND, OR, NOT)
# Logical AND
print("Logical AND (True and False):", bool_true and bool_false)

# Logical OR
print("Logical OR (True or False):", bool_true or bool_false)

# Logical NOT
print("Logical NOT (not True):", not bool_true)
print("Logical NOT (not False):", not bool_false)

# Step 3: Use a Boolean variable in a conditional statement
# Conditional statement with logical operation
if bool_true and not bool_false:
    print("Both conditions are met: bool_true is True and bool_false is False.")
else:
    print("The conditions are not met.")
