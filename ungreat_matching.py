import math
def ungreat_match(str1,str2):
	i=0
	lenth1 = len(str1)
	lenth2 = len(str2)
	mk = 0
	if str1 == str2:
		return True
	elif math.abs(lenth1 - lenth2) > 3:
		return False
	else:
		for char in str1:
			if char == str2[i]:
				mk+=1
			i+=1
