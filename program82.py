import re
pattern = r"^colo.r"
if re.match(pattern,"colour"):
    print("Matched")
else:
    print("Didn't match")