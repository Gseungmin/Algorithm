import sys
input = sys.stdin.readline
import heapq

N = int(input())
people = [list(map(int,input().split())) for i in range(N)]
people.sort()

remain = []
computer = dict()
end_time = []

cnt = 0
for start, end in people:
    
    while end_time:
        if end_time[0][0] <= start:
            i, index = heapq.heappop(end_time)
            heapq.heappush(remain,index)
        else:
            break
        
    if len(remain) == 0:
        cnt += 1
        computer[cnt] = 1
        heapq.heappush(end_time, [end, cnt])
    else:
        index = heapq.heappop(remain) #사용할 수 있는 컴퓨터 인덱스
        computer[index] += 1
        heapq.heappush(end_time, [end, index])
        
print(len(computer))
for i in range(1,len(computer)+1):
    print(computer[i], end = " ")