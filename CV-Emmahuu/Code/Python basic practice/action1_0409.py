def sum(start, end, step):
	result = (start + end)*((end - start)/step + 1)/2
	print(result)

sum(1, 99, 2)
#16ms
sum(1, 100, 1)
sum(2, 100, 2)
sum(1, 100, 3)

sum2 = 0
for i in range(1, 100, 2):
	sum2 += i
print(sum2)
#20ms

def end(start, step, times):
	end_num = start + step * times