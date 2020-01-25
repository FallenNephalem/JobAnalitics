import math
#from fuzzywuzzy import fuzz
#from fuzzywuzzy import process


def num_match(num1, num2):
	if num1>num2:
		return num1
	else:
		return num2

def ungreat_match(str1,str2):
	i=0
	lenth1 = len(str1)
	lenth2 = len(str2)
	mk = 0
	if str1 == str2:
		return True
	elif math.fabs(lenth1 - lenth2) > 3:
		return False
	else:
		for char in str1:
			if i<(num_match(lenth1, lenth2)-1):

				if char == str2[i]:
					#print('true')
					mk+=1
				#else:
					#print('fail')
			i+=1
		print(mk)

		if mk==num_match(lenth1, lenth2):
			return True
		else:
			return False
