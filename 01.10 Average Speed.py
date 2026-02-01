#Get the length of race in kilometers, minutes, and seconds
kilometers = int(input("Enter Length of Race in Kilomenters: "))
minutes = int(input("Enter Minutes: "))
seconds = int(input("Enter Seconds: "))

#Calculate miles in kilometer
miles = kilometers / 1.61

#Convert time into hours
total_seconds = (minutes * 60) + seconds
hours = total_seconds / 3600

#Calculate average speed in miles per hours
average_speed = miles / hours

#Print Results
print(average_speed)