import sys
input = sys.stdin.readline
N = int(input())
Set = set(map(int,input().split()))
M = int(input())
List = list(map(int,input().split()))
true = [0]*M
for i in range(len(List)):
    if List[i] in Set:
        true[i] = 1
print(" ".join(map(str,true)))