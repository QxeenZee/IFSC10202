def print_pattern(height):
    #Prints the specified pattern with a given height.
    
    # Ascending part of the pattern
    for i in range(1, height + 1):
        print("* " * i)

    # Descending part of the pattern
    for i in range(height - 1, 0, -1):
        print("* " * i)


# Get user input for height
try:
    height = int(input("Enter maximum height: "))
    if height <= 0:
        print("Please enter a positive integer for the height.")
    else:
        print_pattern(height)
except ValueError:
    print("Invalid input. Please enter an integer.")