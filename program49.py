from _collections import deque
bank = deque(["Asif","Sunny","Karim"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
if not bank :
    print("Not a single person is available")