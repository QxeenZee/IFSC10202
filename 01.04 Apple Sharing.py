#Prompt for number of students and apples
students = int(input("Number of Students: "))
apples = int(input("Number of Apples: "))

#Calculate apples per student
apples_per_student = apples // students

#Calculate remaining apples
remaining_apples = apples % students

#Print results
print ("Apples per student: ", apples_per_student)
print ("Remaining apples: ", remaining_apples)
