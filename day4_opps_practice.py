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
    def bonous(self):
        self.marks=self.marks+10
        if self.marks>=100:
            return 100
        else:
            return self.marks
    def grade(self):
        if self.marks>=90:
            return "garade a"
        elif self.marks>=75:
            return "gradeb"
        elif self.marks>=40:
            return "gradec"
        else:
            return "graded"
    
        
        
        
        
s1=Student("piyush",99)

s1.show()
print(s1.check())
s2=Student("tony",8)
s2.show()
print(s2.check())
s3=Student("parul",40)
s4=Student("ronit",25)
s3.show()
print(s3.check())
s4.show()
print(s4.check())
print(s1.grade())
