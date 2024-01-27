# Global variable
global_variable = 10


def modify_global_variable():
    # Use the global keyword to indicate that we are referring to the global variable
    global global_variable

    # Modify the global variable
    global_variable += 5


# Call the function to modify the global variable
modify_global_variable()

# Print the modified global variable
print("Modified Global Variable:", global_variable)
