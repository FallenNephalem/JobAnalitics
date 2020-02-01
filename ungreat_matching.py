import math
#from fuzzywuzzy import fuzz
#from fuzzywuzzy import process
alfabet = [['q','Q'],['w','W'],['e','E'],['r','R'],
['t','T'],['y','Y'],['u','U'],['i','I'],['o','O'],
['p','P'],['a','A'],['s','S'],['d','D'],['f','F'],
['g''G'],['h','H'],['j','J'],['k','K'],['l','L'],
['z','Z'],['x','X'],['c','C'],['v','V'],['b','B'],
['n','N'],['m','M']]


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

def one_register(str1):
	i=0
	while i<len(str1):
		j=0
		while j<26:
			print(alfabet[15][1])
			if str1[i] == alfabet[j][1]:
				str1[i] = alfabet[j][0]
			j+=1
			print("j"+str(j))
		i+=1
		print("i"+str(i))


def ungreat_match(str1,str2):
	i=0
	lenth1 = len(str1)
	lenth2 = len(str2)
	#print(str2)
	mk = 0
	min_num = num_match_min(lenth1, lenth2)
	str1 = one_register(str1)
	str2 = one_register(str2)
	if str1 == str2:
		keys = [str1, 'True']
		return keys
	elif math.fabs(lenth1 - lenth2) > 3:
		test = 1
		keys = ['mismatching skills', 'False', test]
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
		if (mk >=  (min_num*0.7)):
			if min_num == lenth1:
				keys = [str1, 'True']
			elif min_num == lenth2:
				keys = [str2, 'True']
			return keys
		else:
			test = 2
			keys = ['mismatching skills', 'False',test]
			return keys
