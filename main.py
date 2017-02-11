def total(N, array):
    i = 0
    while i < N and array[i] == 1:
        i = i + 1
    thousands = (N - sum(array)) * 1000 + 100*( N - i)
    return thousands

T = raw_input()

lines = list()
lines = lines.append(raw_input())
lines = [x.strip() for x in lines] 

for i in range(T):
    array = list(map(int, lines[1].split()))
    N = int(lines[0])
    del lines[0]
    del lines[0]
    print(total(N, array))
