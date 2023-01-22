import sys
input = sys.stdin.readline
N = int(input())

List = []
origin = []
for i in range(N):
    a, b = map(int,input().split())
    List.append([b,a])
    origin.append([b,a])

List.sort()

Dict = dict()

for index in range(len(List)):
    size, color = List[index]
    
    if color not in Dict:
        Dict[color] = []
        Dict[color].append([index, 1, size, size])
    else:
        Dict[color].append([index, Dict[color][-1][1]+1, Dict[color][-1][2]+size, size])

Sum = 0

color_index = dict()

cnt = 0
prev = List[0][0]

ans = [0]*N
check = 0

last = dict()

for index in range(len(List)):
    
    size, color = List[index]
    
    if size != prev: #이전과 사이즈가 다른 경우
        Sum += prev*check
        prev = size
        cnt = index
        check = 1
    else: #이전과 사이즈가 같은 경우
        check += 1
        
    #먹을 수 있는 것이 없는 경우
    if cnt == 0:
        if color not in color_index:
            color_index[color] = 0
        else:
            color_index[color] += 1
        continue

    #먹을 수 있는 경우
    #해당 컬러가 나온적이 없으면
    if color not in color_index:
        color_index[color] = 0
        ans[index] = Sum
        last[color] = Sum
    else:
        if size != Dict[color][color_index[color]][3]: #사이즈가 같은 경우는 빼면 안됨
            ans[index] = (Sum - Dict[color][color_index[color]][2])
            last[color] = ans[index]
        else:
            ans[index] = last[color]
        color_index[color] += 1

from collections import deque
inverter = dict()
for i in range(N):
    a, b = List[i]
    if (a,b) not in inverter:
        inverter[(a,b)] = deque()
        inverter[(a,b)].append(ans[i])
    else:
        inverter[(a,b)].append(ans[i])

for i in range(N):
    x, y = origin[i]
    print(inverter[(x,y)].popleft())