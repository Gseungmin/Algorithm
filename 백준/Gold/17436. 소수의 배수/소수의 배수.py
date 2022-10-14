import sys
input = sys.stdin.readline
N, M = map(int,input().split())
prime = list(map(int,input().split()))
num = 1
Sum = [0]

def reculsive(N, M, num, pick, prime, start, List, Sum):
    if num == pick:
        value = 1
        for i in List:
            value *= i
        if num % 2 == 0:
            Sum[0] -= M//value
        else:
            Sum[0] += M//value
        return
    for i in range(start,N):
        List.append(prime[i])
        reculsive(N, M, num, pick+1, prime, i+1, List, Sum)
        List.pop()
    return

while num <= N:
    reculsive(N, M, num, 0, prime, 0, [], Sum)
    num += 1
print(Sum[0])