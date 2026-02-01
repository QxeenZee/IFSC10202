#First Timestamp
first_hours = int(input("Enter Hours: "))
first_minutes = int(input("Enter Minutes: "))
first_seconds = int(input("Enter Seconds: "))

#Second Timestamp
second_hours = int(input("Enter Hours: "))
second_minutes = int(input("Enter Minutes: "))
second_seconds = int(input("Enter Seconds: "))

#Convert timestamps into seconds
first_total_seconds = (first_hours * 3600) + (first_minutes * 60) + first_seconds
second_total_seconds = (second_hours * 3600) + (second_minutes * 60) + second_seconds

