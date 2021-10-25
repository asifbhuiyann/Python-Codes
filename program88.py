import re
pattern = r"a+b"
if re.match(pattern,"aacoloujr"):
    print("Matched")
else:
    print("Didn't match")