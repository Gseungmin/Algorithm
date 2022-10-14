import sys
input = sys.stdin.readline
import math
A1, A2, A3, B1, B2, B3, C1, C2, C3 = map(int,input().split())
def dist(x1,x2,x3,y1,y2,y3):
    return math.sqrt(((x1-y1)**2+(x2-y2)**2+(x3-y3)**2))
dx = B1-A1
dy = B2-A2
dz = B3-A3
left = 0.0
right = 1.0
m = 0
while True:
    if abs(right-left) < 1e-9:
        m = (left+right)/2
        break
    m1 = left+(right-left)/3
    m2 = right-(right-left)/3
    m1x = A1 + m1*(dx)
    m1y = A2 + m1*(dy)
    m1z = A3 + m1*(dz)
    m2x = A1 + m2*(dx)
    m2y = A2 + m2*(dy)
    m2z = A3 + m2*(dz)
    d1 = dist(m1x,m1y,m1z,C1,C2,C3)
    d2 = dist(m2x,m2y,m2z,C1,C2,C3)
    if d1 > d2:
        left = m1
    else:
        right = m2

x0 = A1 + m*dx
y0 = A2 + m*dy
z0 = A3 + m*dz
ans = dist(x0,y0,z0,C1,C2,C3)
print('%.10f'%ans)