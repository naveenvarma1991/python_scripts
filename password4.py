#!/usr/bin/python

import re
password = True
special_str = "[$#@]"
value = []
items = raw_input("Enter Valid Inputs With Comma : ").split(',')
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        break
      
    else:
        print("Valid Password", p)
        p=False
        break

if p:
    print("Not a Valid Password" , p)
  
 
