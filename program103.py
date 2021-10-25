import re
pattern = r"[A-Z][a-z][0-9]"
if re.match(pattern,"Ab0"):
    print("Matched")
else:
    print("Didn't match")