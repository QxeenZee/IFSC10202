def is_special_number(n):
    #Checks if a number is a special number.
    original_number = n
    num_digits = 0
    temp = n

    # Determine the number of digits
    while temp > 0:
        num_digits += 1
        temp //= 10

    # Calculate the sum of digits raised to the power of the number of digits
    sum_of_powers = 0
    temp = original_number
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10

    return sum_of_powers == original_number


def find_special_numbers(start, end):
    """Finds and prints special numbers within a given range."""
    print(f"Special Numbers between {start} and {end}")
    for number in range(start, end + 1):
        if is_special_number(number):
            print(number)


# Get user input for the range
try:
    start_range = int(input("Enter Start of Range: "))
    end_range = int(input("Enter End of Range: "))

    if start_range > end_range or start_range < 1 or end_range < 1:
        print("Invalid range. Please provide a valid range.")
    else:
        find_special_numbers(start_range, end_range)

except ValueError:
    print("Invalid input. Please enter integers for the range.")