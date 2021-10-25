n = int(input("Enter the number:"))
sum = 0
a = 0
b = 1
for x in range (1,n+1,1) :
    sum = sum + x
    a = a + x*x
    b = b * x
print(sum)
print(a)
print(b)
