import re
pattern = r"colour"
if re.search(pattern,"Red is a colour and i love red"):
    print("Matched")
else:
    print("Not Matched")
