import sys
input = sys.stdin.readline
A = [list(map(int,input().split())) for i in range(3)]

List = [1,2,3,4,5,6,7,8,9]
import itertools
per = list(itertools.permutations(List))
cnt = []
for case in per:
    r1 = case[0]+case[1]+case[2]
    r2 = case[3]+case[4]+case[5]
    r3 = case[6]+case[7]+case[8]
    c1 = case[0]+case[3]+case[6]
    c2 = case[1]+case[4]+case[7]
    c3 = case[2]+case[5]+case[8]
    x1 = case[0]+case[4]+case[8]
    x2 = case[2]+case[4]+case[6]
    if r1 == r2 == r3 == c1 == c2 == c3 == x1 == x2:
        Sum = 0
        Sum += abs(case[0]-A[0][0])
        Sum += abs(case[1]-A[0][1])
        Sum += abs(case[2]-A[0][2])
        Sum += abs(case[3]-A[1][0])
        Sum += abs(case[4]-A[1][1])
        Sum += abs(case[5]-A[1][2])
        Sum += abs(case[6]-A[2][0])
        Sum += abs(case[7]-A[2][1])
        Sum += abs(case[8]-A[2][2])
        cnt.append(Sum)
print(min(cnt))