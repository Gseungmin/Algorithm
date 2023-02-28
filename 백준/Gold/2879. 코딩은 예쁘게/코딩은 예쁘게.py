import sys
input = sys.stdin.readline

#4:41
#연속된 줄을 그룹으로 선택, 줄 앞에 탭 추가 및 삭제, 뒤죽박죽 인텐트를 고치는 방법은?
#줄 N개와 줄 앞에 탭 개수와 올바른 탭 개수가 주어짐

#1. 연속된 줄 선택
#2. 수정

N = int(input())
now = list(map(int,input().split()))
right = list(map(int,input().split()))

true = [False]*N #0은 x 1은 이미 확정
for i in range(N):
    if now[i] == right[i]:
        true[i] = True

cnt = 0
for i in range(N):
    
    if true[i] == True:
        continue
    
    while now[i] > right[i]:
        plus = []
        Min = int(1e9)
        for j in range(i,N):
            if now[j] > right[j]: #연속된 모든 것 찾기
                Min = min(Min, now[j]-right[j])
                plus.append(j)
            elif now[j] < right[j] or true[j] == True: #반대거나 이미 완료되었거나
                break
            
        for k in plus:
            now[k] -= Min
            if now[k] == right[k]:
                true[k] = True
        cnt += Min
    
    while now[i] < right[i]:
        Minus = []
        Min = int(1e9)
        for j in range(i,N):
            if now[j] < right[j]: #연속된 모든 것 찾기
                Min = min(Min, -now[j]+right[j])
                Minus.append(j)
            elif now[j] > right[j] or true[j] == True: #반대거나 이미 완료되었거나
                break
        for k in Minus:
            now[k] += Min
            if now[k] == right[k]:
                true[k] = True
        cnt += Min
    
print(cnt)