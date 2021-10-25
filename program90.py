import re
pattern = r"ice(-)?cream"
if re.match(pattern,"ice----cream"):
    print("Matched")
else:
    print("Didn't match")