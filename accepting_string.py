#accepting the string
import re
pat=re.compile("abc*",re.IGNORECASE)
str-input("enter the string")
if re.match(pat,str):
    print("the string is accepted")
else:
    print("the sting is not excepted")
