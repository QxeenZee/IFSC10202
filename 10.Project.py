# Step 1 - Create a class called "Student"
class Student:

    # Step 2 - Define the initializer
    def __init__(self, firstname, lastname, tnumber, scores):

        # Step 3 - Create attributes
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores

    # Calculates the running average (non-blank)
    def RunningAverage(self):
        total = 0
        count = 0

        for grade in self.Grades:
            if grade != "":
                total += float(grade)
                count += 1

        if count == 0:
            return 0
        else:
            return total / count

    # Calculates the semester average (blank = 0)
    def TotalAverage(self):
        total = 0

        for grade in self.Grades:
            if grade == "":
                total += 0
            else:
                total += float(grade)

        if len(self.Grades) == 0:
            return 0
        else:
            return total / len(self.Grades)

    # Returns letter grade
    def LetterGrade(self):
        avg = self.TotalAverage()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


# HEADER
print("       First         Last           ID      Running     Semester       Letter")
print("        Name         Name       Number      Average      Average        Grade")
print("------------ ------------ ------------ ------------ ------------ ------------")

# READ FILE
file = open("10.Project Student Scores.txt", "r")

for line in file:
    line = line.strip()
    parts = line.split(",")

    firstname = parts[0]
    lastname = parts[1]
    tnumber = parts[2]
    scores = parts[3:]

    student = Student(firstname, lastname, tnumber, scores)

    print(f"{student.FirstName:>12} {student.LastName:>12} {student.TNumber:>12} "
          f"{student.RunningAverage():>12.2f} {student.TotalAverage():>12.2f} {student.LetterGrade():>12}")

file.close()