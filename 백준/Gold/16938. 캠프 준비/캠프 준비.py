import sys
input = sys.stdin.readline
N, L, R, X = map(int,input().split())
List = list(map(int,input().split()))

ans = [0]
problem = []
def reculsive(N,L,R,X,List,index,problem,ans):
    if index == N:
        if len(problem) >= 2:
            Sum = sum(problem)
            dif = max(problem)-min(problem)
            if L<=Sum<=R and dif>=X:
                ans[0] += 1
        return
    problem.append(List[index])
    reculsive(N,L,R,X,List,index+1,problem,ans)
    problem.pop()
    reculsive(N,L,R,X,List,index+1,problem,ans)
    return

reculsive(N,L,R,X,List,0,problem,ans)
print(ans[0])