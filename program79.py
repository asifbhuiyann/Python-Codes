import re
pattern = r"colour"
text1 = "Red is my fav colour but i love blue colour also."
text2 = re.sub(pattern,"color",text1)
text3 = re.sub(pattern,"color",text1,count=1)
print(text2)
print(text3)