#삭제 시 x, y 기둥에 문제가 발생하는 지 확인
def delete_c(x, y, col, row):
    check = True
    
    if y == 0:
        return True
    elif (x-1,y) in row or (x,y) in row: #보의 한쪽 끝 부분 위에 있는 경우
        return True
    elif (x,y-1) in col:#다른 기둥 위인 경우
        return True
    
    return False
    

#삭제 시 x, y 보에 문제가 발생하는 지 확인
def delete_r(x, y, col, row):

    #한쪽 끝이 기둥 위에 있거나
    if (x,y-1) in col or (x+1,y-1) in col:
        return True
    elif (x-1,y) in row and (x+1, y) in row : #양쪽이 다른 보와 연결
        return True
    
    return False

def solution(n, build_frame):
    
    #기둥과 보를 연결할 그래프
    col = dict()
    row = dict()
    
    #각 경우 세울수 있는지 판단
    #x,y는 좌표, a = 0은 기둥, a = 1은 보, b는 설치 또는 삭제
    for x, y, a, b in build_frame:

        #기둥일 경우
        if a == 0:
            
            #설치할 경우
            if b == 1:
                #바닥일 경우
                if y == 0:
                    col[(x,y)] = True
                elif (x-1,y) in row or (x,y) in row: #보의 한쪽 끝 부분 위에 있는 경우
                    col[(x,y)] = True
                elif (x,y-1) in col: #다른 기둥 위인 경우
                    col[(x,y)] = True
            
            else: #삭제할 경우
                
                #문제가 없으면 삭제
                col.pop((x,y))
                
                #바로 위에 기둥이 있는 경우
                if (x,y+1) in col:
                    check = delete_c(x,y+1, col, row)
                    if check == False:
                        col[(x,y)] = True
                        continue
                
                #바로 아래 기둥이 있는 경우
                if (x,y-1) in col:
                    check = delete_c(x,y-1, col, row)
                    if check == False:
                        col[(x,y)] = True
                        continue
                
                #바로 왼쪽에 보가 있는 경우
                if (x-1,y) in row:
                    check = delete_r(x-1,y, col, row)
                    if check == False:
                        col[(x,y)] = True
                        continue
                        
                #바로 오른쪽에 보가 있는 경우
                if (x,y) in row:
                    check = delete_r(x,y, col, row)
                    if check == False:
                        col[(x,y)] = True
                        continue
                        
                #바로 왼쪽에 보가 있는 경우
                if (x-1,y+1) in row:
                    check = delete_r(x-1,y+1, col, row)
                    if check == False:
                        col[(x,y)] = True
                        continue
                        
                #바로 오른쪽에 보가 있는 경우
                if (x,y+1) in row:
                    check = delete_r(x,y+1, col, row)
                    if check == False:
                        col[(x,y)] = True
                        continue
        
        #보일 경우
        elif a == 1:
            
            #설치할 경우
            if b == 1:
                #한쪽 끝이 기둥 위에 있거나
                if (x,y-1) in col or (x+1,y-1) in col:
                    row[(x,y)] = True
                elif (x-1,y) in row and (x+1, y) in row : #양쪽이 다른 보와 연결
                    row[(x,y)] = True
            
            else: #삭제할 경우
                
                #삭제 후 문제 있는지 파악
                row.pop((x,y))
                
                #바로 위에 기둥이 있는 경우
                if (x,y) in col:
                    check = delete_c(x,y, col, row)
                    if check == False:
                        row[(x,y)] = True
                        continue
                
                if (x+1,y) in col:
                    check = delete_c(x+1,y, col, row)
                    if check == False:
                        row[(x,y)] = True
                        continue
                
                #바로 아래 기둥이 있는 경우
                if (x,y-1) in col:
                    check = delete_c(x,y-1, col, row)
                    if check == False:
                        row[(x,y)] = True
                        continue
                
                if (x+1,y-1) in col:
                    check = delete_c(x+1,y-1, col, row)
                    if check == False:
                        row[(x,y)] = True
                        continue
                
                #바로 왼쪽에 보가 있는 경우
                if (x-1,y) in row:
                    check = delete_r(x-1,y, col, row)
                    if check == False:
                        row[(x,y)] = True
                        continue
                        
                #바로 오른쪽에 보가 있는 경우
                if (x+1,y) in row:
                    check = delete_r(x+1,y, col, row)
                    if check == False:
                        row[(x,y)] = True
                        continue
    
    answer = []
    
    for i, j in col:
        answer.append([i,j,0])
        
    for i, j in row:
        answer.append([i,j,1])
    
    answer.sort()
    
    return answer