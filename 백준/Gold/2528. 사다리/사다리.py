import sys
input = sys.stdin.readline
N, L = map(int,input().split())

if N == 1:
    print(0)
    sys.exit()

floor = []
for i in range(N):
    a, b = map(int,input().split())
    if b == 0:
        floor.append([1,a,b])
    elif b == 1:
        floor.append([L-a+1,L,b])

x = 0
nx = 1
time = 0
while 1:
    
    #점프 이동
    while x < N:
        x1, y1 = floor[x][0], floor[x][1]
        x2, y2 = floor[nx][0], floor[nx][1]
        check = True
        if (y2+1 < x1) or (y1+1 < x2):
            check = False
        if check == True:
            x, nx = nx, nx+1
            if x == N-1:
                print(time)
                sys.exit()
        else:
            break
    
    #막대 이동
    for i in range(N):
        
        #한층을 다 메웠으면
        if floor[i][0] == 1 and floor[i][1] == L:
            continue
        
        #왼쪽으로 이동
        if floor[i][2] == 1:
            floor[i][0] -= 1
            floor[i][1] -= 1
            if floor[i][0] == 1:
                floor[i][2] = 0
        
        #오른쪽으로 이동
        if floor[i][2] == 0:
            floor[i][0] += 1
            floor[i][1] += 1
            if floor[i][1] == L:
                floor[i][2] = 1
    
    time += 1