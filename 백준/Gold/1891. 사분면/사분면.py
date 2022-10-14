import sys
input = sys.stdin.readline
N, num = map(int,input().split())
nx, ny = map(int,input().split())
num = list(str(num))
def reculsive(N,M,x1,x2,y1,y2,num,ans):
    if N == 0:
        ans.append([x1,y1])
        return
    if num[M] == '2':
        reculsive(N-1,M+1,x1,x1+2**(N-1),y1,y1+2**(N-1),num,ans)
    if num[M] == '1':
        reculsive(N-1,M+1,x1,x1+2**(N-1),y1+2**(N-1),y2,num,ans)
    if num[M] == '3':
        reculsive(N-1,M+1,x1+2**(N-1),x2,y1,y1+2**(N-1),num,ans)
    if num[M] == '4':
        reculsive(N-1,M+1,x1+2**(N-1),x2,y1+2**(N-1),y2,num,ans)
    return
ans = []
reculsive(N,0,0,2**N,0,2**N,num,ans)
x, y = ans.pop()
if nx >= 0:
    y += abs(nx)
else:
    y -= abs(nx)
if ny >= 0:
    x -= abs(ny)
else:
    x += abs(ny)
check = False
if 0<=x<2**N and 0<=y<2**N:
    check = True
if check == False:
    print(-1)
    sys.exit()
def reculsive2(N,x,y,x1,x2,y1,y2,num,ans):
    if N == 0:
        return
    if x1<=x<x1+2**(N-1) and y1<=y<y1+2**(N-1):
        ans.append(2)
        reculsive2(N-1,x,y,x1,x1+2**(N-1),y1,y1+2**(N-1),num,ans)
    if x1<=x<x1+2**(N-1) and y1+2**(N-1)<=y<y2:
        ans.append(1)
        reculsive2(N-1,x,y,x1,x1+2**(N-1),y1+2**(N-1),y2,num,ans)
    if x1+2**(N-1)<=x<x2 and y1<=y<y1+2**(N-1):
        ans.append(3)
        reculsive2(N-1,x,y,x1+2**(N-1),x2,y1,y1+2**(N-1),num,ans)
    if x1+2**(N-1)<=x<x2 and y1+2**(N-1)<=y<y2:
        ans.append(4)
        reculsive2(N-1,x,y,x1+2**(N-1),x2,y1+2**(N-1),y2,num,ans)
    return
ans2 = []
reculsive2(N,x,y,0,2**N,0,2**N,num,ans2)
for i in ans2:
    print(i, end = "")