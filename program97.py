import re
pattern = r"[a-z]"
if re.match(pattern,"aaa"):
    print("Matched")
else:
    print("Didn't match")