import sys
input = sys.stdin.readline
import bisect

N, M, K = map(int,input().split())

Map = dict()
keys = []

for i in range(N):
    a, b = map(int,input().split())
    Map[a] = b
    keys.append(a)

keys.sort()

for q in range(M):
    command = list(map(int,input().split()))
    
    #삽입일 경우
    if command[0] == 1:
        a, b = command[1], command[2]
        bisect.insort(keys,a)
        Map[a] = b
        
    #데이터 검색후 변경
    if command[0] == 2:
        a, b = command[1], command[2]
        
        if a in Map:
            Map[a] = b
        else:
            index = bisect.bisect_left(keys, a)
            #index 값이 위치 값
            if index == 0: #맨 처음에 들어가는 경우
                if abs(keys[0]-a) <= K:
                    Map[keys[0]] = b
            elif index == len(keys): #맨 마지막에 들어가는 경우
                if abs(keys[-1]-a) <= K:
                    Map[keys[-1]] = b
            else: #중간에 들어가는 경우
                dif1 = abs(keys[index-1]-a)
                dif2 = abs(keys[index]-a)
                if dif1 == dif2:
                    continue
                if dif1 > dif2:
                    if dif2 <= K:
                        Map[keys[index]] = b
                elif dif1 < dif2:
                    if dif1 <= K:
                        Map[keys[index-1]] = b
    
    #데이터 검색 후 출력
    if command[0] == 3:
        a = command[1]
        check = False
        if a in Map:
            print(Map[a])
            check = True
        else:
            index = bisect.bisect_left(keys, a)
            #index 값이 위치 값
            if index == 0: #맨 처음에 들어가는 경우
                if abs(keys[0]-a) <= K:
                    print(Map[keys[0]])
                    check = True
            elif index == len(keys): #맨 마지막에 들어가는 경우
                if abs(keys[-1]-a) <= K:
                    check = True
                    print(Map[keys[-1]])
            else: #중간에 들어가는 경우
                dif1 = abs(keys[index-1]-a)
                dif2 = abs(keys[index]-a)
                if dif1 == dif2:
                    if dif1 <= K:
                        print("?")
                        continue
                if dif1 > dif2:
                    if dif2 <= K:
                        print(Map[keys[index]])
                        check = True
                elif dif1 < dif2:
                    if dif1 <= K:
                        check = True
                        print(Map[keys[index-1]])
        if check == False:
            print(-1)