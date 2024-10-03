def print_multiplication_table():
    """
    Prints the multiplication table from 1 to 9.
    Each row represents the multiplication of a number with all numbers from 1 to 9.
    """
    for i in range(1, 10):  # Iterate through numbers 1 to 9 for the multiplication table
        # Create a list for the current row of the multiplication table
        row = [f'{i}x{j} = {i*j:2d}' for j in range(1, 10)]  # Calculate and format each multiplication
        # Print the current row by joining the elements with two spaces
        print('  '.join(row))

# Call the function to print the multiplication table
print_multiplication_table()