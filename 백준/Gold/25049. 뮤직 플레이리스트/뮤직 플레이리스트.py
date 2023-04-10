import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

ans = sum(arr)

front = []
Sum = 0
for i in range(N):
    Sum += arr[i]
    if Sum < 0:
        Sum = 0
    front.append(Sum)

back = [] 
Sum = 0
for i in range(N-1,-1,-1):
    Sum += arr[i]
    if Sum < 0:
        Sum = 0
    back.append(Sum)
    
f_Max = 0
f_List = [0]*N

for i in range(N):
    f_Max = max(f_Max, front[i])
    f_List[i] = f_Max

b_Max = 0
b_List = [0]*N

for i in range(N):
    b_Max = max(b_Max, back[i])
    b_List[i] = b_Max

Max = f_List[-1]
for i in range(N-1):
    Max = max(Max, f_List[i] + b_List[N-(i+2)])

print(ans+Max)

