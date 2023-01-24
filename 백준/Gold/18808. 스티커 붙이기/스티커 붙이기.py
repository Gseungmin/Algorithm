import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
size = []
graph = []
for i in range(K):
    r, c = map(int,input().split())
    size.append([r,c])
    
    graph.append([list(map(int,input().split())) for i in range(r)])

paper = [[0]*M for i in range(N)]

#90도 회전 로직
def spin(index):

    sticker = graph[index]
    r, c = size[index]
    
    new_sticker =[]
    
    for i in range(c):
        List = []
        for j in range(r-1,-1,-1):
            List.append(sticker[j][i])
        new_sticker.append(List)
    
    
    graph[index] = new_sticker
    size[index] = [c,r]
    return

def find(index):
    
    sticker = graph[index]
    r, c = size[index]
    
    for i in range(N):
        for j in range(M):
            
            check = True
            
            for x in range(r):
                for y in range(c):
                    nx = i+x
                    ny = j+y
                    
                    if nx >= N or ny >= M:
                        check = False
                        break
                    
                    if sticker[x][y] == 1 and paper[nx][ny] == 1:
                        check = False
                        break
            
                if check == False:
                    break
            
            if check == True:
                for x in range(r):
                    for y in range(c):
                        
                        if sticker[x][y] == 1:
                        
                            nx = i+x
                            ny = j+y
                            
                            paper[nx][ny] = sticker[x][y]
                    
                return True
                
    return False
    



for index in range(K):
    
    check = False
    
    for k in range(4):
        
        if k != 0:
            spin(index)
            
        check = find(index)
        
        if check == True:
            break

cnt = 0
for i in range(N):
    for j in range(M):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)