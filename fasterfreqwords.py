#this function reverses the sequence (c) bioinfo 101
def reverse(input_sequence):
    reverse_complement = ''
    n = len(input_sequence) - 1
    while n >= 0:
        if input_sequence[n] == 'A':
            reverse_complement += 'T'
            n = n-1
        elif input_sequence[n] == 'T':
            reverse_complement += 'A'
            n = n-1
        elif input_sequence[n] == 'C':
            reverse_complement += 'G'
            n = n-1
        else:
            reverse_complement += 'C'
            n = n-1
	#reverse the string otherwise its not reverse 
    return reverse_complement[::-1]


def NumberToSymbol(s):
	if s == 0:
       		return "A"
    	elif s == 1:
        	return "C"
    	elif s == 2:
        	return "G"
    	elif s == 3:
        	return "T"
def NumbertoPattern(index,k):
	if k == 1:
		return NumberToSymbol(index)
	prefixIndex = index /4
	r = index % 4
	symbol = NumberToSymbol(r)
	PrefixPattern = NumbertoPattern(prefixIndex,k-1)
	return PrefixPattern + symbol
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

def compfreq(text, k):
	freq_array =[0]* (4**k)
	for i in range(0, len(text) -k + 1):
		# extract current pattern (k-mer)
		pattern = text[i:i+k]
		patnum = PatterntoNumber(pattern)
	    	freq_array[patnum] += 1
	return freq_array
def fasterfreqword(text,k):
	max_pats = []  	# Ausgabeliste, alle Pattern mit maximalem count
	freq_array = compfreq(text,k)
	reverse_sum_fa = list(freq_array)
	'''misconception from last time made this more complex 
	#for every pattern reverse it and add the reverse sum to the reverse_sum_freqarray
	for pat_number, value in enumerate(freq_array):
		reverse_sum_fa[pat_number] += freq_array[PatterntoNumber(reverse(NumbertoPattern(pat_number,k)))]
	#find max value
	
	max_count = max(reverse_sum_fa)
	#find patterns with max count and append to max_pats
	for pat_number_index, value in enumerate(reverse_sum_fa):
		if value == max_count:
			max_pats.append(NumbertoPattern(pat_number_index,k))
	list(set(max_pats))  # remove duplicates
	ret_max_mers = ' '.join(max_pats)
	return ret_max_mers
	'''
	#find max value
	max_count = max(freq_array)
	#find patterns with max count and append to max_pats
	for pat_number_index, value in enumerate(freq_array):
		if value == max_count:
			max_pats.append(NumbertoPattern(pat_number_index,k))
	list(set(max_pats))  # remove duplicates
	ret_max_mers = ' '.join(max_pats)
	return ret_max_mers
dna="TCCGGCCAAGGACCCGAACCGTAGCTGACTCCGGCCAAGGTAGCTGACGTAGCTGACTCCGGCCAAGGACCCGAACCGTAGCTGACGTAGCTGACGACCCGAACCTCCGGCCAAGTTTTCGATTTTTCGATGACCCGAACCGACCCGAACCTCCGGCCAAGGACCCGAACCTCCGGCCAAGGTAGCTGACTCCGGCCAAGGTAGCTGACTGTTAAGTTTTTCGATTCCGGCCAAGTTTTCGATGACCCGAACCGTAGCTGACGACCCGAACCGTAGCTGACGACCCGAACCTCCGGCCAAGTCCGGCCAAGGTAGCTGACTTTTCGATTGTTAAGTTCCGGCCAAGGACCCGAACCTTTTCGATTGTTAAGTGTAGCTGACGTAGCTGACTTTTCGATGTAGCTGACTTTTCGATTCCGGCCAAGTTTTCGATGACCCGAACCGTAGCTGACGTAGCTGACTGTTAAGTTGTTAAGTGTAGCTGACGACCCGAACCGTAGCTGACTGTTAAGTTTTTCGATTCCGGCCAAGTCCGGCCAAGTGTTAAGTTCCGGCCAAGTGTTAAGTTGTTAAGTGTAGCTGACTCCGGCCAAGTTTTCGATTTTTCGATTGTTAAGTTGTTAAGTGTAGCTGACTCCGGCCAAGTTTTCGATTGTTAAGTTTTTCGATTGTTAAGTGACCCGAACCGTAGCTGACGACCCGAACCTGTTAAGTTCCGGCCAAGGACCCGAACCTCCGGCCAAGGTAGCTGACTTTTCGATGACCCGAACCGTAGCTGACTTTTCGATTTTTCGATGACCCGAACCTCCGGCCAAGTTTTCGATTGTTAAGTTGTTAAGTTTTTCGATTGTTAAGTGTAGCTGACTGTTAAGTTTTTCGATGTAGCTGACTGTTAAGTTGTTAAGTGACCCGAACCTTTTCGATTCCGGCCAAGTCCGGCCAAGTGTTAAGTTTTTCGAT"


k=11
print(fasterfreqword(dna,k))

