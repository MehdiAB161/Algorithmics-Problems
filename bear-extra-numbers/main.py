from numpy import asarray
from numpy import diff
from numpy import sort
from numpy import where

def to_int(array):
	return [int(i) for i in array] 

def algorithm(sequence):
	array = asarray(sequence)
	array = sort(array)
	differ = diff(array)
	if where(differ != 1)[0] > 0 :
		return(array[-1])
	else :
		return array[where(differ != 1)][0]

T=int(input())

i = 0
while int(i)!= T:
	N=int(input())
	line = to_int(input().split())
	print(algorithm(line))
	i += 1
