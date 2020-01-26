import math
#from fuzzywuzzy import fuzz
#from fuzzywuzzy import process


def num_match_max(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2

def num_match_min(num1, num2):
	if num1 > num2:
		return num2
	else:
		return num1

def ungreat_match(str1,str2):
	i=0
	lenth1 = len(str1)
	lenth2 = len(str2)
	#print(str2)
	mk = 0
	min_num = num_match_min(lenth1, lenth2)
	if str1 == str2:
		keys = [str1, 'True']
		return keys
	elif math.fabs(lenth1 - lenth2) > 3:
		keys = ['mismatching skills', 'False']
		return keys
	else:
		for char in str1:
			if i < min_num:

				if char == str2[i]:
					#print('true')
					mk+=1
				#else:
					#print('fail')
			i+=1
		#print(mk)
		#print(min_num)
		if mk == min_num:
			if min_num == lenth1:
				keys = [str1, 'True']
			elif min_num == lenth2:
				keys = [str2, 'True']
			return keys
		else:
			keys = ['mismatching skills', 'False']
			return keys
