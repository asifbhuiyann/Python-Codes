import re
pattern = r"[0-9]"
if re.match(pattern,"aaa"):
    print("Matched")
else:
    print("Didn't match")