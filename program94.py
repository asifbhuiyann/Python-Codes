import re
pattern = r"[aeiou]"
if re.match(pattern,"b"):
    print("Matched")
else:
    print("Didn't match")