def First(num):
    List = []
    for i in range(1,10):
        List.append(num-(num//1000)*1000+i*1000)
    return List
def Second(num):
    List = []
    for i in range(10):
        List.append(num-(num//100)*100+(num//1000)*1000+i*100)
    return List
def Third(num):
    List = []
    for i in range(10):
        List.append(num-(num//10)*10+(num//100)*100+i*10)
    return List
def Forth(num):
    List = []
    for i in range(10):
        List.append((num//10)*10+i)
    return List

from collections import deque
def Prime(start, end, prime, true):
    if start == end:
        print(0)
        return
    queue = deque()
    queue.append(start)
    true[start] = 0
    while queue:
        now = queue.popleft()
        F = First(now)
        for i in F:
            if prime[i] == 0 and true[i] == -1: #소수이고 방문한 적이 없으면
                true[i] = true[now] + 1
                queue.append(i)
                if i == end:
                    print(true[i])
                    return
        S = Second(now)
        for i in S:
            if prime[i] == 0 and true[i] == -1: #소수이고 방문한 적이 없으면
                true[i] = true[now] + 1
                queue.append(i)
                if i == end:
                    print(true[i])
                    return
        T = Third(now)
        for i in T:
            if prime[i] == 0 and true[i] == -1: #소수이고 방문한 적이 없으면
                true[i] = true[now] + 1
                queue.append(i)
                if i == end:
                    print(true[i])
                    return
        F_2 = Forth(now)
        for i in F_2:
            if prime[i] == 0 and true[i] == -1: #소수이고 방문한 적이 없으면
                true[i] = true[now] + 1
                queue.append(i)
                if i == end:
                    print(true[i])
                    return
    print('Impossible')
    return

import sys
input = sys.stdin.readline
prime = [0]*10000
prime[0] = 1
prime[1] = 1
for i in range(101):
    if prime[i] == 0:
        j = i
        while i*j < 10000:
            prime[i*j] = 1
            j += 1    
T = int(input())
for i in range(T):
    A, B = map(int,input().split())
    true = [-1]*10000
    Prime(A, B, prime, true)