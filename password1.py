#!/usr/bin/python

import re


special_str = "$#@"
accepted = []

passwords = raw_input("Enter comma-separated passwords: ").split(',')

for password in passwords:

	lower = 0
	upper = 0
	digits = 0
	special = 0

	for char in password:

		if char.islower():
			lower += 1
		elif char.isupper():
			upper += 1
		elif char.isdigit():
			digits += 1
		elif special_str.find(char) != -1:
			special += 1

	if lower >= 1 and upper >= 1 and digits >= 1 and special >= 1 and len(password) in range(6,13):
		accepted.append(password)

print ",".join(accepted)

