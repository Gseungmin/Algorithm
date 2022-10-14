import sys
input = sys.stdin.readline
N, r, c = map(int,input().split())
ans = [0]
def reculsive(N,r,c,x1,x2,y1,y2,one,ans):
    two = one + (((2**N)**2)-1)//3
    three = one + ((((2**N)**2)-1)//3)*2
    four = one + ((2**N)**2)-1
    if r == x1 and c == y1:
        ans[0] = one
        return
    if r == x2 and c == y1:
        ans[0] = two
        return
    if r == x1 and c == y2:
        ans[0] = three
        return
    if r == x2 and c == y2:
        ans[0] = four
        return
    check = False
    if x1<=r<x2 and y1<=c<y2:
        check = True
    if check:
        reculsive(N-1,r,c,x1,x1+2**(N-1),y1,y1+2**(N-1),one,ans)
        reculsive(N-1,r,c,x1,x1+2**(N-1),y1+2**(N-1),y2,one+(2**(N-1))**2,ans)
        reculsive(N-1,r,c,x1+2**(N-1),x2,y1,y1+2**(N-1),one+((2**(N-1))**2)*2,ans)
        reculsive(N-1,r,c,x1+2**(N-1),x2,y1+2**(N-1),y2,one+((2**(N-1))**2)*3,ans)
    return
reculsive(N,r,c,0,2**N,0,2**N,0,ans)
print(ans[0])