import sys
input = sys.stdin.readline

def D(num):
    return (2*num) % 10000
def S(num):
    if num == 0:
        return 9999
    return num-1
def L(num):
    return (num%1000)*10 + num//1000
def R(num):
    return (num%10)*1000 + num//10

from collections import deque
T = int(input())
for t in range(T):
    start, End = map(int,input().split())
    true = ["N"]*(10000)
    prev = [-1]*(10000)
    queue = deque()
    queue.append(start)
    true[start] = ""
    while queue:
        x = queue.popleft()
        x1 = D(x)
        x2 = S(x)
        x3 = L(x)
        x4 = R(x)
        if true[x1] == 'N':
            true[x1] = 'D'
            prev[x1] = x
            queue.append(x1)
        if true[x2] == 'N':
            true[x2] = 'S'
            prev[x2] = x
            queue.append(x2)
        if true[x3] == 'N':
            true[x3] = 'L'
            prev[x3] = x
            queue.append(x3)
        if true[x4] == 'N':
            true[x4] = 'R'
            prev[x4] = x
            queue.append(x4)
        if true[End] != 'N':
            ans = ""
            while End != start:
                ans = true[End] + ans
                End = prev[End]
            print(ans)
            break