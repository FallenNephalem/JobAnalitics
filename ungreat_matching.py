import math
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
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

			if char == str2[i]:
				print('true')
				mk+=1
			else:
				print('fail')
			i+=1
		if mk < (lenth1-3) & (mk < lenth2-3):
			return True
		else:
			return False
