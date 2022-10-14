import sys
input = sys.stdin.readline
x, y, c = map(float,input().split())
import math
def C(x, y, c, num):
    h1 = math.sqrt(x**2 - num**2)
    h2 = math.sqrt(y**2 - num**2)
    return (h1*h2) / (h1+h2)
    

left = 0.0
right = min(x,y)
def P2022(x, y, c, left, right):
    while abs(right-left) > 1e-6:
        mid = (right + left) / 2.0
        h = C(x, y, c, mid)
        if h > c:
            left = mid
        else:
            right = mid
    return left

ans = P2022(x, y, c, left, right)
print('%.03f'%ans)