import re
pattern = r"[aeiou]"
if re.match(pattern,"aaa"):
    print("Matched")
else:
    print("Didn't match")