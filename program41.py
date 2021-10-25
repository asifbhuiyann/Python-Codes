numberofwords = 0
numberofletters = 0
numberofdigits = 0
text = input("Enter the text : \n")
for x in text :
    x = x.lower()
    if x>='a' and x<='z' :
        numberofletters = numberofletters + 1
    elif x>='0' and x<='9' :
        numberofdigits = numberofdigits + 1
    elif x == ' ' :
        numberofwords = numberofwords +1
print("Number of letters are",numberofletters)
print("Number of digits are", numberofdigits)
print("Number of words are", numberofwords)



