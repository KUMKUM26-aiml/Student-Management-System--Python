#Student Management System
import pandas as pd 
import matplotlib.pyplot as plt

filename=input("enter filename : ")
try:
   df=pd.read_csv(filename)
except FileNotFoundError:
   df=pd.DataFrame(columns=['name','roll','marks'])
   df.to_csv(filename,index=False)


class College:
    def __init__(self):
        global df
        self.df=df

    def save(self):
       self.df.to_csv(filename,index=False)
        
    def add_student(self,name,roll,marks):
       name = input("Enter name: ")
       roll = int(input("Enter roll: "))
       marks = int(input("Enter marks: "))
       
       new_row = pd.DataFrame([[name, roll, marks]],
                               columns=["name", "roll", "marks"])
       
       self.df = pd.concat([self.df, new_row], ignore_index=True)
       self.save()
       print("Student added successfully!")


    def show_students(self):
       print(self.df)
    
    def search_student(self):
        name=input("enter name to search ")
        result = self.df[self.df["name"] == name]
        print(result if not result.empty else "Student not found")

    def delete_student(self):
        roll_no=int(input("enter roll no to delete"))
        self.df = self.df[self.df["roll"] != roll_no]
        self.save()
        print("student deleted if existed")

        

    def update_marks(self):
       roll_no=int(input("enter roll no to update marks"))
       new_marks=int(input("enter new marks to update "))
       self.df.loc[self.df["roll"] == roll_no, "marks"] = new_marks
       self.save()
       print("marks updated")
  


    def grade_check(self):
        if self.df.empty:
            print("no data")
            return
        
        print("Highest  marks: ",self.df['marks'].max())
        print("Average marks: ",self.df['marks'].mean())
        print("Lowest marks: ",self.df['marks'].min())


        self.df['grade']=pd.cut(
            self.df['marks'],
            bins=[0,60,70,80,90,100],
            labels=["Fail",'D',"C",'B',"A"]
        )

        print("\nGrades: ")
        print(self.df[['name','roll','marks','grade']])

    def show_graps(self):
        if self.df.empty:
            print("no data")
            return
        

        #bar chart of marks
        plt.figure()
        plt.bar(self.df['name'],self.df['marks'])
        plt.xlabel("students")
        plt.ylabel("marks")
        plt.title("marks of student")
        plt.tight_layout()
        plt.show()


        #histogram of marks
        plt.figure()
        self.df['marks'].plot(kind='hist',bins=5)
        plt.xlabel("marks")
        plt.ylabel("number of students")
        plt.title("distribution of marks")
        plt.tight_layout()
        plt.show()


    def menu(self):
        while True:
            print("\n1. Add Student")
            print("2. Show Students")
            print("3. Search Student")
            print("4. delete student")
            print("5.update marks ")
            print("6.grade checking ")
            print("7.show graphs")
            print("8. Exit")

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
                self.show_graps()
            elif choice=="8":
                break
            else:
                print("Invalid choice")


c=College()
c.menu()