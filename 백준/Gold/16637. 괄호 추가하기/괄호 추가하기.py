N = int(input())
A = list(input())
B = []
check = []

if N == 1:
    print(int(A[0]))
    exit()

for i in A:
    if i != '*' and i != '-' and i != '+':
        B.append(int(i))
        continue
    B.append(i)

def reculsive(N, A, index, check, B, Max):
    if index >= N:
        now = B[0]
        for i in range(1,N,2):
            if B[i] == '+':
                now += B[i+1]
            if B[i] == '*':
                now *= B[i+1]
            if B[i] == '-':
                now -= B[i+1]
        if Max[1] == 0:
            Max[0] = now
            Max[1] = 1
        else:
            Max[0] = max(Max[0], now)
        return
    if index-2 not in check:
        check.append(index)
        if A[index] == '+':
            B[index-1] = B[index-1] + B[index+1]
            B[index+1] = 0
            reculsive(N, A, index+2, check, B, Max)
            B[index-1] = int(A[index-1])
            B[index+1] = int(A[index+1])
        elif A[index] == '*':
            B[index-1] = B[index-1] * B[index+1]
            B[index+1] = 0
            B[index] = '+'
            reculsive(N, A, index+2, check, B, Max)
            B[index-1] = int(A[index-1])
            B[index+1] = int(A[index+1])
            B[index] = '*'
        elif A[index] == '-':
            B[index-1] = B[index-1] - B[index+1]
            B[index+1] = 0
            B[index] = '+'
            reculsive(N, A, index+2, check, B, Max)
            B[index-1] = int(A[index-1])
            B[index+1] = int(A[index+1])
            B[index] = '-'
        check.pop()
    reculsive(N, A, index+2, check, B, Max)
    return

Max = [0,0]
reculsive(N, A, 1, check, B, Max)
print(Max[0])