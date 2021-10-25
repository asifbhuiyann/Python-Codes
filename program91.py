import re
pattern = r"a{1,2}$"
if re.match(pattern,"aa"):
    print("Matched")
else:
    print("Didn't match")