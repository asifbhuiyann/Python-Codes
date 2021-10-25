import re
pattern = r"[A-Z]"
if re.match(pattern,"aaa"):
    print("Matched")
else:
    print("Didn't match")