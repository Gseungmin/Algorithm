N = int(input())

def solution(a):
    if a % 5 == 0:
        return N // 5
    b = a//5
    for i in range(b+1):
        c = a - (b-i)*5
        if c % 3 == 0:
            return (b-i) + c//3
    return -1

print(solution(N))