import sys
input = sys.stdin.readline
N = int(input())
List = list(map(int,input().split()))

Max = max(List)
index = []
for i in range(len(List)):
    if List[i] == Max:
        index.append(i)

#무승부가 없는 경우
if len(index) == 1:
    i = index[0]
    B = i
    R = len(List)-(i+1)
    if B > R:
        print("B")
    else:
        print("R")
        
else: #무승부가 있는 경우
    left_index = index[0]
    right_index = index[-1]
    B = left_index
    R = len(List)-(right_index+1)
    if B > R:
        print("B")
    elif B == R:
        print("X")
    else:
        print("R")