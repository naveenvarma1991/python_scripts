#!/usr/bin/env python3

#!/usr/bin/python3

import os

path = " "

ret = os.getcwd()
print  (ret )

os.chdir ('/home')

ret = os.getcwd()

print(ret)


os.chdir('/home/naveen')
import subprocess
subprocess.call(['ls','-1'])

