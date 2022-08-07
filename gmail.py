# Email validation using regex
'''
valid email conditions
a-z
0-9
. _ (1 time)
@ (1 time)
. 2,3
'''
import re
condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email = input("Enter your email:")

if re.search(condition,email):
    print("Valid Email")
else:
    print("Invalid Email")