emp =[]

    
def add_student():
    name = input("what is your name:")
    marks = int(input("how much your marks:"))
    if marks < 0 or marks > 100:
        print("marks must be between 0 and 100")
        return
    student = Student(name, marks)
    emp.append(student)

class Student:
    def  __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show(self):
        print(self.name,self.marks)
    def check(self):
        if self.marks>=40:
                return "pass"
        else:
                return "fail"

    def grade(self):
        if self.marks>=90:
            return "grade a"
        elif self.marks>=75:
            return "grade b"
        
        elif self.marks>=40:
            return "grade c"
        else:
            return "grade d"
def showstudent():
    if emp==[]:
        print("No students yet")
        
    else:
        for s in emp:
            print(s.name,s.grade(),s.marks)
        

    
def search_student():
    name=input("serch for the name:")
    found=False
    for s in emp:
        if s.name.lower()==	name.lower():
            print(s.name,s.grade(),s.marks)
            found=True
            break
    if found==False:
        print("student not found")
def update_student():
    name=input("what is the name")
    found=False
    for s in emp:
        
        if s.name.lower()==name.lower():
            new_marks=int(input("what is the new marks:"))
            s.marks=new_marks
            print("marks updated")
            found=True
            break
    if found==False:
        print("student not found")
def delete_student():
    name=input("which student you want to delete:")
    found=False
    for s in emp:
        if s.name.lower()==name.lower():
            emp.remove(s)
            print("student deleted")
            found=True
            break
    if found==False:
        print("student not found")

def save_students():
    with open("students.txt","w") as f:
        
        for s in emp:
            f.write(s.name +"," + str(s.marks)+"\n")
def load_students():
    try:
         with open("students.txt","r") as f:
            for line in f:
                line=line.strip()
                parts=line.split(",")
                student=Student(parts[0],int(parts[1]))
                emp.append(student)
    except FileNotFoundError:
        pass
load_students()
def show_topper():
    if emp==[]:
        print("no student yet")
        return
    topper=emp[0]
    for s in emp:
        if s.marks>topper.marks:
            topper=s
    print(topper.name,topper.marks,topper.grade())

def show_average():
    if emp==[]:
        print("no student yet")
        return
    total=0
    for s in emp:
        total=total+s.marks
    avg=total/len(emp)
    print(avg)
def show_passed():
    if emp==[]:
        print("no student yet")
        return
    found=False
    for s in emp:
        if s.check()=="pass":
            print(s.name,s.marks)
            found=True
    if found==False:
        print("no body is passed")
        
        
    
    
    
        

            
    
        
    
        
    
            
        
def menu():
    while True:
        print("1. Add student")
        print("2. View all students")
        print("3. search_student")
        print("4. update_student")
        print("5. delete_student")
        print("6. save_student")
        print("7. show_topper")
        print("8. show_average")
        print("9. show_passed")
        print("10. exit")
        choice = input("Enter your choice: ")



        if choice == "1":
            add_student()
        elif choice == "2":
            showstudent()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice=="5":
            delete_student()
        elif choice=="6":
            save_students()
        elif choice=="7":
            show_topper()
        elif choice=="8":
            show_average()
        elif choice=="9":
            show_passed()
            
                
            
        elif choice=="10":
            print("exit")
            
            break
        else:
            print("Invalid choice")
menu()

        
