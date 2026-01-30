#Prompt user for a number
number = int(input("Enter a number: "))

#Calculate next number
calculate_next_number = number + 1

#Calculate previous number
calculate_prev_number = number - 1

#Print results
print ("The next number for the number " + str(number) + " is " + str(calculate_next_number) + "." )
print ("The previous number for the number " + str(number) + " is " + str(calculate_prev_number) + "." )