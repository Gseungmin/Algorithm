import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    cafe = dict()
    for i in range(n):
        y, x = map(int,input().split())
        if y in cafe:
            cafe[y].append(x)
        else:
            cafe[y] = [x]
    ans = []
    x_index = 0
    y_index = 0
    cnt = 0
    while cnt < n:
        if y_index in cafe:
            cafe[y_index].sort()
            if cafe[y_index][0] == x_index: #x_index
                for j in cafe[y_index]:
                    ans.append([y_index, j])
                    cnt += 1
                x_index = j
            elif cafe[y_index][-1] == x_index: #y_index
                while cafe[y_index]:
                    j = cafe[y_index].pop()
                    ans.append([y_index, j])
                    cnt += 1
                x_index = j
        y_index += 1
    num = list(map(int,input().split()))
    for i in range(1,len(num)):
        x, y = ans[num[i]-1]
        print(x, y)