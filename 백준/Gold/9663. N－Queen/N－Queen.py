import sys
input = sys.stdin.readline
N = int(input())
col = [0]*(N)
dia_1 = [0]*(2*N-1)
dia_2 = [0]*(2*N-1)
cnt = [0]

def check(N, col, dia_1, dia_2, i, j):
    if col[j] == 1:
        return False
    if dia_1[i+j] == 1:
        return False
    if dia_2[i-j+N-1] == 1:
        return False
    return True
    
def check_2(N, col):
    for i in range(N):
        if col[i] == 0:
            return False
    return True
    
def Queen(N, x, col, dia_1, dia_2, cnt):
    if check_2(N, col): #모든 곳을 돌았으면 리턴
        cnt[0] += 1
        return
    if x == N:
        return
    for y in range(N):
        if check(N, col, dia_1, dia_2, x, y):
            col[y] = 1
            dia_1[x+y] = 1
            dia_2[x-y+N-1] = 1
            Queen(N, x+1, col, dia_1, dia_2, cnt)
            col[y] = 0
            dia_1[x+y] = 0
            dia_2[x-y+N-1] = 0
    return
Queen(N, 0, col, dia_1, dia_2, cnt)
print(cnt[0])