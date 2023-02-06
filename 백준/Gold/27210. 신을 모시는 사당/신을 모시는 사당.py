import sys
input = sys.stdin.readline
N = int(input())
List = list(map(int,input().split()))

if N == 1:
    print(1)
    sys.exit()

left_prefix = [0]*len(List)
right_prefix = [0]*len(List)

left = 0
right = 0
for i in range(len(List)):
    if List[i] == 1:
        left += 1
    elif List[i] == 2:
        right += 1
    left_prefix[i] = left
    right_prefix[i] = right

prefix = [0]*len(List)

for i in range(len(List)):
    prefix[i] = left_prefix[i]-right_prefix[i]
    
Max = max(prefix)
Min = min(prefix)
Max_index = -1
Min_index = -1
for i in range(len(List)):
    if prefix[i] == Max:
        Max_index = i
    if prefix[i] == Min:
        Min_index = i

ans = 0
if 0 < Max:
    if Max_index == 0:
        pre_min = 0
    else:
        pre_min = min(prefix[:Max_index])
    pre_min = min(0, pre_min)
    ans = max(ans, Max-pre_min)
    
if Min < 0:
    if Min_index == 0:
        pre_max = 0
    else:
        pre_max = max(prefix[:Min_index])
    pre_max = max(0, pre_max)
    ans = max(ans, abs(Min-pre_max))

print(ans)