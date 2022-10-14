def solve(n):
    if int((n**0.5))**2 == n:
        return 1

    for s in sqs:
        if n-s < 0:
            break
        x = int((n-s)**0.5)**2
        if x == n-s:
            return 2

    for s in sqs:
        if n-s < 0:
            break
        for t in sqs:
            if n-s-t < 0:
                break
            if int((n-s-t)**0.5)**2 == n-s-t:
                return 3

    return 4


import sys
input = sys.stdin.readline
n = int(input())

sqs = [i**2 for i in range(1, int(n**0.5)+1)]
print(solve(n))