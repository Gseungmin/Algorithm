import sys
input = sys.stdin.readline
a, b, c = map(int,input().split())
def RC(a,b,c):
    if b == 0:
        return 1
    if b == 1:
        return a%c
    if b % 2 == 0:
        temp = RC(a,b//2,c)
        return (temp*temp) % c
    if b % 2 == 1:
        return (a * RC(a,b-1,c)) % c
print(RC(a,b,c))