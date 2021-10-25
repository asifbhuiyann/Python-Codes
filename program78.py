import re
pattern = r"colour"
text = "Red is my fav colour"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())