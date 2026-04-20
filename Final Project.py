class Employee:
    def __init__(self, empNum, first, last, address, city, state, zipCode):
        self.EmployeeNumber = int(empNum)
        self.FirstName = first
        self.LastName = last
        self.Address = address
        self.City = city
        self.State = state
        self.Zip = zipCode


class EmployeeList:
    def __init__(self, filename):
        self.EmployeeList = []
        self.Filename = filename

    def ReadEmployeeFile(self):
        try:
            with open(self.Filename, "r") as file:
                for line in file:
                    parts = [p.strip() for p in line.strip().split(",")]
                    if len(parts) == 7:
                        emp = Employee(*parts)
                        self.EmployeeList.append(emp)
        except FileNotFoundError:
            print("File not found. Starting with empty list.")

    def WriteEmployeeFile(self):
        with open(self.Filename, "w") as file:
            for emp in self.EmployeeList:
                file.write(f"{emp.EmployeeNumber},{emp.FirstName},{emp.LastName},"
                           f"{emp.Address},{emp.City},{emp.State},{emp.Zip}\n")
        print("Changes saved.")

    def DisplayEmployeeList(self):
        print(f"{'Employee':<12}{'First':<15}{'Last':<15}{'Address':<15}{'City':<15}{'State':<10}{'Zip':<10}")
        print("-" * 90)
        for emp in self.EmployeeList:
            print(f"{emp.EmployeeNumber:<12}{emp.FirstName:<15}{emp.LastName:<15}"
                  f"{emp.Address:<15}{emp.City:<15}{emp.State:<10}{emp.Zip:<10}")

    def FindEmployee(self, empNum):
        for i in range(len(self.EmployeeList)):
            if self.EmployeeList[i].EmployeeNumber == int(empNum):
                return i
        return -1

    def NextEmployeeNumber(self):
        if len(self.EmployeeList) == 0:
            return 1
        return self.EmployeeList[-1].EmployeeNumber + 1

    def AddEmployee(self, first, last, address, city, state, zipCode):
        empNum = self.NextEmployeeNumber()
        emp = Employee(empNum, first, last, address, city, state, zipCode)
        self.EmployeeList.append(emp)
        print("Employee Added")

    def DeleteEmployee(self, empNum):
        index = self.FindEmployee(empNum)
        if index == -1:
            print("Employee not found")
        else:
            del self.EmployeeList[index]
            print("Employee Deleted")

    def UpdateEmployee(self, empNum):
        index = self.FindEmployee(empNum)
        if index == -1:
            print("Employee not found")
            return

        emp = self.EmployeeList[index]

        while True:
            print("\n(F)irst Name\n(L)ast Name\n(A)ddress\n(C)ity\n(S)tate\n(Z)ip\n(B)ack")
            choice = input("Enter Selection: ").upper()

            if choice == "F":
                emp.FirstName = input("Enter First Name: ")
            elif choice == "L":
                emp.LastName = input("Enter Last Name: ")
            elif choice == "A":
                emp.Address = input("Enter Address: ")
            elif choice == "C":
                emp.City = input("Enter City: ")
            elif choice == "S":
                state = input("Enter State (2 uppercase letters): ")
                if len(state) == 2 and state.isupper():
                    emp.State = state
                else:
                    print("Invalid State")
            elif choice == "Z":
                zipCode = input("Enter Zip (5 digits): ")
                if zipCode.isdigit() and len(zipCode) == 5:
                    emp.Zip = zipCode
                else:
                    print("Invalid Zip")
            elif choice == "B":
                break


# ================= MAIN PROGRAM =================

employees = EmployeeList("Final Project Employees.txt")
employees.ReadEmployeeFile()

while True:
    print("\n(A)dd\n(D)elete\n(C)hange\n(P)rint\n(S)ave\n(Q)uit")
    choice = input("Enter Selection: ").upper()

    if choice == "A":
        first = input("Enter First Name: ")
        last = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")

        state = input("Enter State (2 uppercase letters): ")
        if not (len(state) == 2 and state.isupper()):
            print("Invalid State")
            continue

        zipCode = input("Enter Zip (5 digits): ")
        if not (zipCode.isdigit() and len(zipCode) == 5):
            print("Invalid Zip")
            continue

        employees.AddEmployee(first, last, address, city, state, zipCode)

    elif choice == "D":
        empNum = input("Enter Employee Number: ")
        employees.DeleteEmployee(empNum)

    elif choice == "C":
        empNum = input("Enter Employee Number: ")
        employees.UpdateEmployee(empNum)

    elif choice == "P":
        employees.DisplayEmployeeList()

    elif choice == "S":
        employees.WriteEmployeeFile()

    elif choice == "Q":
        print("Good-bye")
        break

    else:
        print("Invalid choice")