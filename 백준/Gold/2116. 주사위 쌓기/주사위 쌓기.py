#1~6까지 정수가 적힌 주사위
#마주보는 면이 7인 주사위는 아님
#어느 한 면의 숫자 합이 최대가 되도록 주사위를 쌓자
#90, 180, 270도 가능
#8:5

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
dices = []
for i in range(N):
    dice = list(map(int,input().split()))
    
    info = [[dice[0],dice[5]], [dice[1],dice[3]], [dice[2],dice[4]]]
    
    dices.append(info)
    
answer = [0]

def RC(u, d, index, Sum):
    
    #최댓값
    Max = 0
    for i in range(6,0,-1):
        if i != u and i != d:
            Max = i
            break
    Sum += Max
    
    if index == len(dices):
        answer[0] = max(answer[0], Sum)
        return
    
    for x, y in dices[index]:
        if x == d:
            RC(x, y, index+1, Sum)
        elif y == d:
            RC(y, x, index+1, Sum)
    
    return

for i in dices[0]:
    u, d = i
    RC(u, d, 1, 0)
    d, u = i
    RC(u, d, 1, 0)

print(answer[0])