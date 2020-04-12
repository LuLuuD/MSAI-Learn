def DNA_strand(dna):
	base = {'A':'T','T':'A','C':'G','G':'C'}
	result = []
	for i in dna:
		result.append(base[i])
	print(''.join(result))

DNA_strand("ATTGC")
DNA_strand("AAAA")
DNA_strand("ATTGC")
# 24ms

def DNA_strand2(dna):
	base = {'A':'T','T':'A','C':'G','G':'C'}
	result2 = ''.join(base[i] for i in dna)
	print(result2)
DNA_strand2("ATTGC")
DNA_strand2("AAAA")
DNA_strand2("ATTGC")
#28ms

def DNA_strand3(dna):
	base = {'A':'T','T':'A','C':'G','G':'C'}
	result = []
	for i in dna:
		result.append(base.get(i))
	print(result)

DNA_strand3("ATTGC")
DNA_strand3("AAAA")
DNA_strand3("ATTGC")
# 28ms