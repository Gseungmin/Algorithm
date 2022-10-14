import sys
input = sys.stdin.readline
T = int(input())

def RC(index):
    if index == 11:
        Sum = 0
        for k in range(11):
            Sum += graph[k][List[k]]
        ans[0] = max(ans[0],Sum)
        return
    for i in range(11):
        if i not in List and graph[index][i] != 0:
            List.append(i)
            RC(index+1)
            List.pop()
    return
    
    
for _ in range(T):
    graph = [list(map(int,input().split())) for i in range(11)]
    ans = [0]
    List = []
    RC(0)
    print(ans[0])