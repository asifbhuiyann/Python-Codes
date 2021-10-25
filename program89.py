import re
pattern = r"ice(-)?cream"
if re.match(pattern,"icecream"):
    print("Matched")
else:
    print("Didn't match")