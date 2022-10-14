def PS(string, size):
    for i in string:
        if size == 0 and i == ')': #닫는 괄호가 먼저나온 경우
            print('NO')
            return
        elif i == '(':
            size += 1
        elif i == ')':
            size -= 1
    if size == 0:
        print('YES')
        return
    print('NO')
    return

import sys
input = sys.stdin.readline
N = int(input())
for k in range(N):
    string = input()
    size = 0
    PS(string, size)