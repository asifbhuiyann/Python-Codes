import re
pattern = r"^colo..r$"
if re.match(pattern,"coloujr"):
    print("Matched")
else:
    print("Didn't match