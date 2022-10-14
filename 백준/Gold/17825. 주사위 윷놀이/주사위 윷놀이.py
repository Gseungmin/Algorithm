import sys
input = sys.stdin.readline
List = list(map(int,input().split()))
graph_l = [i for i in range(1,34)]
point_l = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,0,35,30,25,24,22,26,27,28,19,16,13]
ngraph_l = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,-1,21,23,24,25,26,25,28,29,25,31,32]
Blue_l = [6,11,16]
nBlue_l = [33,27,30]
ngraph = dict(zip(graph_l,ngraph_l))
point = dict(zip(graph_l,point_l))
nBlue = dict(zip(Blue_l,nBlue_l))

horse = [1,1,1,1]
Sum = [0,0,0,0]
ans = [0]
def RC(index):
    if index == 10:
        ans[0] = max(ans[0],sum(Sum))
        return
    if horse[0] == 22 and horse[1] == 22 and horse[2] == 22 and horse[3] == 22:
        ans[0] = max(ans[0],sum(Sum))
        return
    for i in range(4):
        if horse[i] == 22:
            continue
        if horse[i] == 6 or horse[i] == 11 or horse[i] == 16:
            x = horse[i]
            nx = nBlue[x]
            for k in range(List[index]-1):
                nx = ngraph[nx]
                if nx == 22:
                    break
            value = point[nx]
            check = True
            for k in range(4):
                if i == k:
                    continue
                if horse[k] == nx and nx != 22:
                    check = False
            if check == False:
                continue
            a, b = Sum[i], horse[i]
            Sum[i] += value
            horse[i] = nx
            RC(index+1)
            Sum[i] = a
            horse[i] = b
        else:
            nx = horse[i]
            for k in range(List[index]):
                nx = ngraph[nx]
                if nx == 22:
                    break
            value = point[nx]
            check = True
            for k in range(4):
                if i == k:
                    continue
                if horse[k] == nx and nx != 22:
                    check = False
            if check == False:
                continue
            a, b = Sum[i], horse[i]
            Sum[i] += value
            horse[i] = nx
            RC(index+1)
            Sum[i] = a
            horse[i] = b
    return
RC(0)
print(ans[0])