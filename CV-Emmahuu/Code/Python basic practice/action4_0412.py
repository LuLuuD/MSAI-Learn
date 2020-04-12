list = [0,1,2,3,4]
list2 = list.copy()
del list2[3]
list.pop(1)
print(list)
print(list2)
list += [40, 50]
print(list)

def tribonacci(signature, n):
	for i in range(n)[3::]:
		signature.append(sum(signature[i-3:i]))
	print(signature[:n])

tribonacci([1,1,1], 10)
tribonacci([300,200,100], 0)
tribonacci([0.5,0.5,0.5], 30)