import sys
input = sys.stdin.readline
H, W = map(int,input().split())
N = int(input())
sticker = []
for i in range(N):
    sticker.append(list(map(int,input().split())))

Max = 0
for i in range(N):
    for j in range(i+1,N):
        check = 0
        x1, y1 = sticker[i]
        x2, y2 = sticker[j]
        if max(x1,x2) <= H and y1+y2 <= W:
            Max = max(Max, x1*y1+x2*y2)
        if x1+x2 <= H and max(y1,y2) <= W:
            Max = max(Max, x1*y1+x2*y2)
        if max(y1,x2) <= H and x1+y2 <= W:
            Max = max(Max, x1*y1+x2*y2)
        if max(x1,y2) <= W and x2+y1 <= H:
            Max = max(Max, x1*y1+x2*y2)
        if max(x1,y2) <= H and y1+x2 <= W:
            Max = max(Max, x1*y1+x2*y2)
        if max(y1,x2) <= W and x1+y2 <= H:
            Max = max(Max, x1*y1+x2*y2)
        if max(y1,y2) <= H and x1+x2 <= W:
            Max = max(Max, x1*y1+x2*y2)
        if max(x1,x2) <= W and y1+y2 <= H:
            Max = max(Max, x1*y1+x2*y2)
print(Max)