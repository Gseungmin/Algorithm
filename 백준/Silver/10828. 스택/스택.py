import sys
input = sys.stdin.readline
N = int(input())
List = []
size = 0
for i in range(N):
    M = input().split()
    if 'push' == M[0]:
        List.append(M[-1])
        size += 1
    elif 'pop' == M[0]:
        if size == 0: #만약 스택이 비어있을 경우
            print(-1)
        else: #스택이 비어있지 않을 경우
            print(List.pop(-1))
            size -= 1
    elif 'size' == M[0]:
        print(size)
    elif 'empty' == M[0]:
        if size == 0: #만약 스택이 비어있을 경우
            print(1)
        else: #스택이 비어있지 않을 경우
            print(0)
    elif 'top' == M[0]:
        if size == 0: #만약 스택이 비어있을 경우
            print(-1)
        else: #스택이 비어있지 않을 경우
            print(List[-1])
