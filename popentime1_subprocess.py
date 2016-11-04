#!usr/bin/python3

import subprocess
p = subprocess.Popen("python3 sleep.py", stdout=subprocess.PIPE, shell=True)
(output, error) = p.communicate()
print("Today is", output)

