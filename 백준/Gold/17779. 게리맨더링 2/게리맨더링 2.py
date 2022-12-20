import sys
input = sys.stdin.readline
N = int(input())
people = [list(map(int,input().split())) for i in range(N)]
total = 0
for i in range(N):
    for j in range(N):
        total += people[i][j]

ans = int(1e9)
for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                
                check = False
                if (1<=x<x+d1+d2) and (x+d1+d2<=N) and (1<=y-d1<y) and (y<y+d2<=N):
                    check = True
                
                if check == False:
                    continue
                
                #경계선 구하기
                boundary = dict()
                k1 = 0
                k2 = 0
                
                row = [set() for i in range(N+1)]
                
                while k1 <= d1:
                    if x+k1<= N and 1<=y-k1:
                        boundary[(x+k1,y-k1)] = True
                        row[x+k1].add(y-k1)
                    if x+d2+k1 <= N and (1 <= y+d2-k1 <= N):
                        boundary[(x+d2+k1,y+d2-k1)] = True
                        row[x+d2+k1].add(y+d2-k1)
                    k1 += 1
                
                while k2 <= d2:
                    if x+k2 <= N and y+k2 <= N:
                        boundary[(x+k2,y+k2)] = True
                        row[x+k2].add(y+k2)
                    if x+d1+k2 <= N and (1<=y-d1+k2<= N):
                        boundary[(x+d1+k2,y-d1+k2)] = True
                        row[x+d1+k2].add(y-d1+k2)
                    k2 += 1
                
                for i in range(1,N+1):
                    if len(row[i]) == 2:
                        new = list(row[i])
                        left = new[0]
                        right = new[1]
                        left, right = min(left, right), max(left,right)
                        for j in range(left+1, right):
                            boundary[(i,j)] = True
                
                #구역 초기화
                one = 0
                two = 0
                three = 0
                four = 0
                for i in range(1,min(x+d1, N+1)):
                    for j in range(1,y+1):
                        if (i,j) not in boundary:
                            one += people[i-1][j-1]
                
                if one == 0:
                    continue
                            
                for i in range(1,min(x+d2+1, N+1)):
                    for j in range(y+1,N+1):
                        if (i,j) not in boundary:
                            two += people[i-1][j-1]
                
                if two == 0:
                    continue
                            
                for i in range(x+d1, N+1):
                    for j in range(1,min(y-d1+d2, N+1)):
                        if (i,j) not in boundary:
                            three += people[i-1][j-1]
                
                if three == 0:
                    continue
                            
                for i in range(x+d2+1,N+1):
                    for j in range(y-d1+d2,N+1):
                        if (i,j) not in boundary:
                            four += people[i-1][j-1]
                
                if four == 0:
                    continue
                        
                five = total - one - two - three - four
                ans = min(ans, max(one,two,three,four,five)-min(one,two,three,four,five))
            

print(ans)