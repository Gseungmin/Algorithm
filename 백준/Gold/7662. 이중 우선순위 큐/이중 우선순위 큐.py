import sys
input = sys.stdin.readline
import heapq
t = int(input())
for _ in range(t):
    N = int(input())
    Max_heap = [] #최대 힙
    Min_heap = [] #최소 힙
    Dict = dict()
    for i in range(N):
        a, b = map(str,input().split())
        if a == "I":
            if int(b) in Dict:
                Dict[int(b)] += 1
            else:
                Dict[int(b)] = 1
            heapq.heappush(Max_heap,-int(b))
            heapq.heappush(Min_heap,int(b))
        if a == "D":
            if b == "-1" and Min_heap:
                while Min_heap and Dict[Min_heap[0]] == 0:
                    heapq.heappop(Min_heap)
                if Min_heap:
                    k = heapq.heappop(Min_heap)
                    if Dict[k] > 0:
                        Dict[k] -= 1
            if b == "1" and Max_heap:
                while Max_heap and Dict[-Max_heap[0]] == 0:
                    heapq.heappop(Max_heap)
                if Max_heap:
                    k = -heapq.heappop(Max_heap)
                    if Dict[k] > 0:
                        Dict[k] -= 1
    while Min_heap and Dict[Min_heap[0]] == 0:
        heapq.heappop(Min_heap)
    while Max_heap and Dict[-Max_heap[0]] == 0:
        heapq.heappop(Max_heap)
    if not Min_heap and not Max_heap:
        print("EMPTY")
    else:
        print(-heapq.heappop(Max_heap), end = " ")
        print(heapq.heappop(Min_heap))