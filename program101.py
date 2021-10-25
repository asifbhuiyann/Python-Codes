import re
pattern = r"[0-9]"
if re.match(pattern,"a0165aa"):
    print("Matched")
else:
    print("Didn't match")