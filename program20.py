marks=int(input("Please enter the marks of the Student:\n"))

if marks>=93 and marks<= 100:
    print("A")

elif marks >= 88 and marks <= 921:
    print("A-")

elif marks >= 85 and marks <= 87:
    print("B+")

elif marks >= 82 and marks <= 84:
     print("B-")

elif marks >= 79 and marks <= 81:
     print("C+")
else:
    print("Better luck for next time")