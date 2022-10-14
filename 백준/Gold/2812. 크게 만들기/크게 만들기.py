from collections import deque
N, K = map(int,input().split())
num = deque(list(input()))
queue = []
cnt = 0
queue.append(int(num.popleft()))
while num:
    if cnt < K:
        while queue and queue[-1] < int(num[0]):
            queue.pop()
            cnt += 1
            if cnt == K:
                break
    queue.append(int(num.popleft()))
for i in range(K-cnt):
    queue.pop()
print("".join(map(str,queue)))