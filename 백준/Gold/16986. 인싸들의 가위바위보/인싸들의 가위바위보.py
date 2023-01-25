import sys
input = sys.stdin.readline
N, K = map(int,input().split()) #N은 손동작 수, K는 필요한 승 수

#승리 정보 (i,j)가 2일 경우 i가 j를 이김, 1일 경우 무승부, 0일 경우 i가 j에 진다를 의미
info = [list(map(int,input().split())) for i in range(N)]

second = list(map(int,input().split()))
third = list(map(int,input().split()))

#cnt는 승 수, index는 각 인덱스, before는 이전에 낸 Set, p1, p2는 플레이 참여자
def RC(x_cnt, y_cnt, z_cnt, x_index, y_index, z_index, p1, p2, before):
    
    #x가 가장 먼저 승리수를 달성한 경우
    if x_cnt == K:
        print(1)
        sys.exit()
        
    #y와 z가 먼저 승리수를 달성한 경우
    if y_cnt == K or z_cnt == K:
        return
    
    if y_index == 20 or z_index == 20 or x_index == N:
        return
    
    #1과 2와 연결하는 경우
    if p1 == 1 and p2 == 2:
        v1 = second[y_index]-1
        v2 = third[z_index]-1
        value = info[v1][v2] #2 or 1 or 0
        
        if value == 2:
            RC(x_cnt, y_cnt+1, z_cnt, x_index, y_index+1, z_index+1, 0, 1, before)
        elif value == 1:
            RC(x_cnt, y_cnt, z_cnt+1, x_index, y_index+1, z_index+1, 0, 2, before)
        elif value == 0:
            RC(x_cnt, y_cnt, z_cnt+1, x_index, y_index+1, z_index+1, 0, 2, before)
    
    if p1 == 0:
        for i in range(N):
            if i in before:
                continue
            before.add(i)
            
            if p2 == 1:
                v1 = i
                v2 = second[y_index]-1
                value = info[v1][v2] #2 or 1 or 0
                if value == 2:
                    RC(x_cnt+1, y_cnt, z_cnt, x_index+1, y_index+1, z_index, 0, 2, before)
                elif value == 1:
                    RC(x_cnt, y_cnt+1, z_cnt, x_index+1, y_index+1, z_index, 1, 2, before)
                elif value == 0:
                    RC(x_cnt, y_cnt+1, z_cnt, x_index+1, y_index+1, z_index, 1, 2, before)
            elif p2 == 2:
                v1 = i
                v2 = third[z_index]-1
                value = info[v1][v2] #2 or 1 or 0
                if value == 2:
                    RC(x_cnt+1, y_cnt, z_cnt, x_index+1, y_index, z_index+1, 0, 1, before)
                elif value == 1:
                    RC(x_cnt, y_cnt, z_cnt+1, x_index+1, y_index, z_index+1, 1, 2, before)
                elif value == 0:
                    RC(x_cnt, y_cnt, z_cnt+1, x_index+1, y_index, z_index+1, 1, 2, before)
                
            before.discard(i)
            
    return

before = set()
RC(0, 0, 0, 0, 0, 0, 0, 1, before)

print(0)