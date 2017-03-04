from itertools import groupby

def to_int(array):
	return [int(i) for i in array] 


T=int(input())

i = 0
while int(i)!= T:
	N, K= to_int(input().split())
	line = to_int(input())
	groups = [ sum(1 for i in g) for k,g in groupby(line)]		
	groups = groups.sort()
	print(groups)
	i += 1
