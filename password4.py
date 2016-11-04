#!/usr/bin/python

import re

special_str = "[$#@]"
value = []
items =[x for x in raw_input().split(',')]
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
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
  
 
