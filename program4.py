fib=1
fibo=1
n= input()
n= input(n)
if n<2:
    fib_n=1
else:
    i=3
    while i<=n:
        i+=1
        fibtemp= fib + fibo
        fib= fibo
        fibo= fibtemp
        fib_n= fibo
        print(fib_n)
