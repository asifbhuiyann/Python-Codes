import re
pattern = r"[A-Z]"
if re.match(pattern,"Aaaa"):
    print("Matched")
else:
    print("Didn't match")