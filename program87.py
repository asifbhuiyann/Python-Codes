import re
pattern = r"a+b"
if re.match(pattern,"abcoloujr"):
    print("Matched")
else:
    print("Didn't match")