def NumberToSymbol(s):
	if s == 0:
       		return "A"
    	elif s == 1:
        	return "C"
    	elif s == 2:
        	return "G"
    	elif s == 3:
        	return "T"
def NumberToPattern(index,k):
	if k == 1:
		return NumberToSymbol(index)
	prefixIndex = index /4
	r = index % 4
	symbol = NumberToSymbol(r)
	PrefixPattern = NumberToPattern(prefixIndex,k-1)
	return PrefixPattern + symbol
print(NumberToPattern(6915,9))
