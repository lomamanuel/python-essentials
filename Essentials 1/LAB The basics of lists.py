#There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
#Your task is to:
#write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
#write a line of code that removes the last element from the list (Step 2)
#write a line of code that prints the length of the existing list (Step 3).


hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2]=int(input("Insert a number: "))

# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)