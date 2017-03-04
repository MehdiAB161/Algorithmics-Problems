def timing(kate, yanna):
	return sum(kate[::2]) + sum(yanna[1::2])


def to_int(array):
	return [int(i) for i in array] 

T=int(input())

i = 0
while int(i)!= T:
	N=int(input())
	yanna = to_int(input().split())
	kate = to_int(input().split())
	time = str(min(timing(kate, yanna), timing(yanna, kate)))
	print(str(time))
	i += 1
