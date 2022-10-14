import sys
input = sys.stdin.readline
        
def BF(case):
    out = 0
    one = False
    two = False
    three = False
    score = 0
    index = 0
    for k in graph:
        while 1:
            i = case[index]
            if k[i] == 0:
                out += 1
                if out == 3:
                    one = False
                    two = False
                    three = False
                    index += 1
                    index %= 9
                    out = 0
                    break
            if k[i] == 1:
                if three == True:
                    score += 1
                    three = False
                if two == True:
                    three = True
                    two = False
                if one == True:
                    two = True
                    one = False
                one = True
            if k[i] == 2:
                if three == True:
                    score += 1
                    three = False
                if two == True:
                    score += 1
                    two = False
                if one == True:
                    three = True
                    one = False
                two = True
            if k[i] == 3:
                if three == True:
                    score += 1
                    three = False
                if two == True:
                    score += 1
                    two = False
                if one == True:
                    score += 1
                    one = False
                three = True
            if k[i] == 4:
                if three == True:
                    score += 1
                    three = False
                if two == True:
                    score += 1
                    two = False
                if one == True:
                    score += 1
                    one = False
                score += 1
            index += 1
            index %= 9
    return score

N = int(input())
graph = [[0] + list(map(int,input().split())) for i in range(N)]
List = [1,2,3,4,5,6,7,8,9]
import itertools
List = list(itertools.permutations(List))
case = []
ans = 0
for i in List:
    if i[3] == 1:
        m = BF(i)
        ans = max(ans, m)
print(ans)