import sys
input = sys.stdin.readline
List = [int(input()) for i in range(10)]
Sum = 0
Dict = dict()
Dict[100] = [0]
for i in range(10):
    Sum += List[i]
    k = abs(100-Sum)
    if k in Dict:
        Dict[k].append(Sum)
    else:
        Dict[k] = [Sum]
Min = min(Dict.keys())
print(max(Dict[Min]))