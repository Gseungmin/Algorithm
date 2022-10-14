import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    start, end = map(int,input().split())
    arr.append([end, start])
arr.sort()
total = 1
index = 1
end, start = arr[0]
while index < N:
    next_end, next_start = arr[index]
    if next_start >= end:
        total += 1
        end = next_end
    index += 1
print(total)