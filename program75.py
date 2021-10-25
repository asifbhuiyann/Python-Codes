import re
pattern = r"colour"
if re.match(pattern,"Red is a colour and i love red"):
    print("Matched")
else:
    print("Not Matched")
