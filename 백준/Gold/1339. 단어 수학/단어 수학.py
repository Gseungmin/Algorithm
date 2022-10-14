import sys
input = sys.stdin.readline
N = int(input())
arr = [list(input()[:-1]) for i in range(N)]
Dict = dict()
for i in arr:
    Len = len(i)-1
    for j in i:
        if j not in Dict:
            Dict[j] = pow(10, Len)
        elif j in Dict:
            Dict[j] += pow(10, Len)
        Len -= 1
Dict = sorted(Dict.values(), reverse=True)

total, k = 0, 9
for i in Dict:
    total += i*k
    k -= 1
print(total)