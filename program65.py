class student() :
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll} , GPA : {self.gpa} ")

rahim = student(101,5.00)
rahim.display()

karim = student(102,3.50)
karim.display()

rana = student(103,4.50)
rana.display()