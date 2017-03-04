def to_int(array):
	return [int(i) for i in array] 

def bandwidth(entries_count, matrix_size):
	i = 0
	entries_count -= matrix_size
	while entries_count > 0:
		i += 1
		entries_count -= 2*(matrix_size - i)
	return i

T=int(input())

i = 0
while int(i)!= T:
	count = 0
	N=int(input())
	for j in range(N):	
		line = to_int(input().split())
		count += sum(line)
		
	print(str(bandwidth(count, N)))
	i += 1
