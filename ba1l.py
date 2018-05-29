def SymbolToNumber(s):
	if s == 'A':
       		return 0
    	elif s == 'C':
        	return 1
    	elif s == 'G':
        	return 2
    	elif s == 'T':
        	return 3


#recursive function to convert PatterntoNumber
def PatterntoNumber(Pattern):
	if Pattern == "":
		return 0
	symbol = Pattern[-1:]
	prefix = Pattern[:-1]
	return 4 * PatterntoNumber(prefix) +SymbolToNumber(symbol)
print(PatterntoNumber("CCGCTGACAGCCGGCTCCATTGA"))
