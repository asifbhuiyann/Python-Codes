import re
pattern = r"[aeiou]"
if re.match(pattern,"A"):
    print("Matched")
else:
    print("Didn't match")