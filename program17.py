num1 = int(input("Enter number 1:\n"))
num2 = int(input("Enter number 2:\n"))
num3 = int(input("Enter number 3:\n"))

if num1 > num2 and num1 > num3:
    print("Maximum number is: ",num1)
elif num2 > num1 and num2 > num3:
    print("Maximum number is: ",num2)
else:
    print("Maximum number is: ",num3)

    print("Program Eliminated.")

