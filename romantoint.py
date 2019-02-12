def value(rfz): 
	if (rfz == 'I'): 
		return 1
	if (rfz == 'V'): 
		return 5
	if (rfz == 'X'): 
		return 10
	if (rfz == 'L'): 
		return 50
	if (rfz == 'C'): 
		return 100
	if (rfz == 'D'): 
		return 500
	if (rfz == 'M'): 
		return 1000
	return -1

def romanToDecimal(str): 
	resfz = 0
	i = 0
	while (i < len(str)): 
		s1 = value(str[i]) 
		if (i+1 < len(str)): 
			s2 = value(str[i+1]) 
			if (s1 >= s2): 
				resfz = resfz + s1 
				i = i + 1
			else: 
				resfz = resfz + s2 - s1 
				i = i + 2
		else: 
			resfz = resfz + s1 
			i = i + 1
	return resfz 
Jfz = input()
print(romanToDecimal(Jfz)) 
