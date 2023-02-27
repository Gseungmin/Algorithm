#N*N 크기 격자, M*M 크기 열쇠
#4:25
#열쇠는 회전과 이동이 가능, 좌물쇠가 열리는 구조, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 좌물쇠의 홈부분이 정확히 일치해야 함
#돌기끼리 만나면 안됨, 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 함 0은 홈 1은 돌기
#lock이 자물쇠, key가 열쇠, 좌물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 영향 x

#M+M+N-2

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