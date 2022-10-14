import sys
input = sys.stdin.readline
N = int(input())
S = [[]] + [[0]+list(map(int,input().split())) for i in range(N)]
team_1 = []
team_2 = []
Min = [0,0]

def reculsive(N,M,S,start,team_1,team_2,Min):
    if M == 0:
        if len(team_1) == 0 or len(team_2) == 0:
            return
        Sum_1 = 0
        for i in range(len(team_1)):
            for j in range(len(team_1)):
                Sum_1 += S[team_1[i]][team_1[j]]
        Sum_2 = 0
        for i in range(len(team_2)):
            for j in range(len(team_2)):
                Sum_2 += S[team_2[i]][team_2[j]]
        if Min[1] == 0:
            Min[0] = abs(Sum_1-Sum_2)
            Min[1] = 1
        else:
            Min[0] = min(Min[0], abs(Sum_1-Sum_2))
        return
    reculsive(N,M-1,S,start+1,team_1+[start],team_2,Min)
    reculsive(N,M-1,S,start+1,team_1,team_2+[start],Min)
    return

reculsive(N,N,S,1,team_1,team_2,Min)
print(Min[0])