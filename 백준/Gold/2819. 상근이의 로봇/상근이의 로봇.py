import sys
input = sys.stdin.readline
from bisect import bisect_right

N, M = map(int,input().split())
x = []
y = []
for i in range(N):
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)
command = input().rstrip()
x.sort()
y.sort()
sum_x = [0]*N
sum_y = [0]*N
sx = 0
sy = 0
for i in range(N):
    sx += x[i]
    sy += y[i]
    sum_x[i] = sx
    sum_y[i] = sy
x_index = 0
y_index = 0
for c in command:
    if c == "S":
        y_index += 1
    elif c == "J":
        y_index -= 1
    elif c == "I":
        x_index += 1
    elif c == "Z":
        x_index -= 1
    left_x = bisect_right(x,x_index)
    left_y = bisect_right(y,y_index)
    dist = abs(sum_x[left_x-1]-x_index*left_x)+abs(sum_x[N-1]-sum_x[left_x-1]-x_index*(N-left_x))+abs(sum_y[left_y-1]-y_index*left_y)+abs(sum_y[N-1]-sum_y[left_y-1]-y_index*(N-left_y))
    print(dist)