import re
pattern = r"a+"
if re.match(pattern,"aacoloujr"):
    print("Matched")
else:
    print("Didn't match")