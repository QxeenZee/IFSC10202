#Get the number of students in each class
classroom_a = int(input("Enter Classroom A: "))
classroom_b = int(input("Enter Classroom B: "))
classroom_c = int(input("Enter Classroom C: "))

#Calculate desk needed from each class
desk_a = classroom_a // 2 + (classroom_a % 2)
desk_b = classroom_b // 2 + (classroom_b % 2)
desk_c = classroom_c // 2 + (classroom_c % 2)

#Calculate total number of desk
total_desks = desk_a + desk_b + desk_c

#Print the results
print(total_desks)