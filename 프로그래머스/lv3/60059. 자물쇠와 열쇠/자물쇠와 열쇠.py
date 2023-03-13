

#90도 회전
def rotate(key, M):
    new_key = []
    for j in range(M):
        List = []
        for i in range(M-1,-1,-1):
            List.append(key[i][j])
        new_key.append(List)
    return new_key

def solution(key, lock):
    
    M = len(key)
    N = len(lock)
    K = M+M+N-2
    S, E = M-1, M-1+N
    graph = [[-1]*K for i in range(K)]
    #새로운 그래프 초기화
    hom = 0
    for i in range(S,E):
        for j in range(S,E):
            graph[i][j] = lock[i-S][j-S]
            if graph[i][j] == 0:
                hom += 1
            
    for _ in range(4):
        
        #총 이동 가능 범위
        for i in range(N+M-1):
            for j in range(N+M-1):
                check = True
                cnt = 0
                
                for x in range(M):
                    for y in range(M):
                        
                        if (S<=i+x<E) and (S<=j+y<E):
                            if graph[i+x][j+y] == 1 and key[x][y] == 1: #둘다 돌기일 경우
                                check = False
                                break

                            if graph[i+x][j+y] == 0 and key[x][y] == 1: #맞을 경우
                                cnt += 1
                                
                            elif graph[i+x][j+y] == 0 and key[x][y] == 0: #안 맞을 경우
                                check = False
                                break
                            
                    if check == False:
                        break
                        
                if check == True and cnt == hom:
                    return True
                        
        #회전
        key = rotate(key, M)
    
    return False