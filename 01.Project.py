#Get the length of time in seconds
time_in_seconds = int(input("Enter Length of Time in Seconds: "))

#Define constants
seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour
seconds_in_year = 365 * seconds_in_day

#Caluate years, days, hours, minutes, and seconds
#Years
years = time_in_seconds // seconds_in_year
remaining_seconds = time_in_seconds % seconds_in_year

#Days
days = remaining_seconds // seconds_in_day
remaining_seconds -= days * seconds_in_day

#Hours
hours = remaining_seconds // seconds_in_hour
remaining_seconds -= hours * seconds_in_hour

#Minutes
minutes = remaining_seconds // seconds_in_minute
remaining_seconds -= minutes * seconds_in_minute

#Seconds
seconds = remaining_seconds

#Print results
print("Years: ",years)
print("Days: ",days)
print("Hours: ",hours)
print("Minutes: ",minutes)
print("Seconds: ",seconds)