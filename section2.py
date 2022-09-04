import re


def	cellNumber(value):
	number =re.sub('/[^a-z]{0,11}$/',"",value)
	cleanNumber="".join(c for c in number if c.isdecimal())
	if cleanNumber[0] != '0':
		new_number = list(cleanNumber)
		new_number.insert(0,0)
		new_number="".join(c for c in number if c.isdecimal())
		if len(new_number) == 10:
			return print("cell number is valid:"+new_number)
		else:
			return print("cell number is not valid:"+new_number)


	
value =input("please enter your cell number")
cellNumber(value)
