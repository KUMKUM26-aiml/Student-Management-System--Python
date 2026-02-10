#Student Management System
class College:
    def __init__(self, filename):
        self.filename = filename

    def add_student(self):
        name = input("Enter name: ")
        roll = input("Enter roll no: ")
        marks = input("Enter marks: ")

        with open(self.filename, "a") as f:
            f.write(f"{name},{roll},{marks}\n")

        print("Student added successfully!")

    def show_students(self):
        try:
            with open(self.filename, "r") as f:
             print("\nStudent Records:")
             for line in f:
                line = line.strip()
                if not line:
                    continue   # skip empty lines

                parts = line.split(",")
                if len(parts) != 3:
                    print("Corrupted record:", line)
                    continue

                name, roll, marks = parts
                print(f"Name: {name}, Roll: {roll}, Marks: {marks}")

        except FileNotFoundError:
            print("File not found. No records yet.")
    
    def search_student(self):
        name_to_search = input("Enter name to search: ")
        found = False
        try:
            with open(self.filename, "r") as f:
             for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    continue

                name, roll, marks = parts
                if name == name_to_search:
                    print(f"Found → Name: {name}, Roll: {roll}, Marks: {marks}")
                    found = True
                    break
            if not found:
                print("Student not found")
        except FileNotFoundError:
         print("File not found.")
        

    def delete_student(self):
        roll_no_tosearch=input("enter roll number to search")
        found=False
        try:
            with open(self.filename, "r") as f:
             lines = f.readlines()

            with open(self.filename, "w") as f:
              for line in lines:
                line = line.strip()
                if not line:
                    continue

                name, roll, marks = line.split(",")

                if roll == roll_no_tosearch:
                    found = True   # skip this line (delete it)
                else:
                    f.write(line + "\n")

            if found:
                print("student deleted succesfully")
            else:
                print("roll number not found")

        
        except FileNotFoundError:
            print("file not found")

    def update_marks(self):
        roll_no_tosearch=input("enter roll number to search ")
        update_marks=int(input("enter marks u wanna update "))
        found=False
        try:
            with open(self.filename, "r") as f:
                lines = f.readlines()

            with open(self.filename, "w") as f:
             for line in lines:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    continue

                name, roll, marks = parts

                if roll == roll_no_tosearch:
                    f.write(f"{name},{roll},{update_marks}\n")
                    found = True
                else:
                    f.write(f"{name},{roll},{marks}\n")
                

            if found:
               print("Marks updated successfully")
            else:
                print("roll number not found")
        
        except FileNotFoundError:
            print("file not found")


    def grade_check(self):
        students = []
        total_marks = 0
        total_students = 0
        highest = None
        lowest = None

        try:
          with open(self.filename, "r") as f:
              for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")
                if len(parts) != 3:
                    continue

                name, roll, marks = parts

                try:
                    marks = int(marks)
                except:
                    continue

                if marks < 0 or marks > 100:
                    continue

                students.append([name, roll, marks])
                total_students += 1
                total_marks += marks

                if highest is None or marks > highest:
                    highest = marks
                if lowest is None or marks < lowest:
                    lowest = marks
            
          if total_students == 0:
            print("No valid student records found")
            return
          
          average = total_marks / total_students
          print("Total students:", total_students)
          print("Average:", average)
          
          print("\nAll Toppers:")
          for name, roll, marks in students:
            if marks == highest:
               print(f"{name} ({roll}) = {marks}")
               print("\nAll Lowest Scorers:")
            for name, roll, marks in students:
             if marks == lowest:
                print(f"{name} ({roll}) = {marks}")

            print("\nGrades:")
            for name, roll, marks in students:
                if marks >= 90:
                    grade = "A"
                    print(f"{name} ({roll}) = {grade}")
                elif marks >= 80:
                    grade = "B"
                    print(f"{name} ({roll}) = {grade}")
                elif marks >= 70:
                   grade = "C"
                   print(f"{name} ({roll}) = {grade}")
                elif marks >= 60:
                   grade = "D"
                   print(f"{name} ({roll}) = {grade}")
                else:
                  grade = "FAIL"
                  print(f"{name} ({roll}) = {grade}")
            

        except FileNotFoundError:
           print("File not found")



    def menu(self):
        while True:
            print("\n1. Add Student")
            print("2. Show Students")
            print("3. Search Student")
            print("4. delete student")
            print("5.update marks ")
            print("6.grade checking ")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.show_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.delete_student()
            elif choice=="5":
                self.update_marks()
            elif choice=="6":
                self.grade_check()
            elif choice=="7":
                exit
            else:
                print("Invalid choice")


filename = input("Enter filename: ")
c = College(filename)
c.menu()
