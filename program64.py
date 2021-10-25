class student() :
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll : {self.roll} , GPA : {self.gpa} ")

rahim = student()
rahim.roll = 101
rahim.gpa = 4.50
rahim.display()

karim = student()
karim.roll = 102
karim.gpa = 5.00
karim.display()

rana = student()
rana.roll = 103
rana.gpa = 4.00
rana.display()