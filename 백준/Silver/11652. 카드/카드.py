import sys
input = sys.stdin.readline
N = int(input())
List = [int(input()) for i in range(N)]
List.sort()
List.append("N")
Max = 1
value = List[0]
count = 1
for i in range(1,N+1):
    if List[i] == List[i-1]:
        count += 1
        continue
    else:
        if Max < count:
            value = List[i-1]
            Max = max(Max, count)
        count = 1
print(value)