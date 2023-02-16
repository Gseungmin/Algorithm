import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
Green = deque([[0]*4 for i in range(6)])
Blue = deque([[0]*4 for i in range(6)])

Score = 0

for _ in range(N):
    t, x, y = map(int,input().split())
    if t == 1: #t 값이 1일 경우
        check1 = False
        for i in range(1,5):
            if Green[i+1][y] == 1:
                check1 = True
                Green[i][y] = 1
                break
        if check1 == False:
            Green[5][y] = 1
            
        check2 = False
        for i in range(1,5):
            if Blue[i+1][3-x] == 1:
                check2 = True
                Blue[i][3-x] = 1
                break
        if check2 == False:
            Blue[5][3-x] = 1
    
    elif t == 2: #t값이 2일 경우
        check1 = False
        for i in range(1,5):
            if Green[i+1][y] == 1 or Green[i+1][y+1] == 1:
                check1 = True
                Green[i][y] = 1
                Green[i][y+1] = 1
                break

        if check1 == False:
            Green[5][y] = 1
            Green[5][y+1] = 1
            
        check2 = False
        for i in range(1,5):
            if Blue[i+1][3-x] == 1:
                check2 = True
                Blue[i][3-x] = 1
                Blue[i-1][3-x] = 1
                break
            
        if check2 == False:
            Blue[5][3-x] = 1
            Blue[4][3-x] = 1
            
    elif t == 3: #t값이 2일 경우
        check1 = False
        for i in range(1,5):
            if Green[i+1][y] == 1:
                check1 = True
                Green[i][y] = 1
                Green[i-1][y] = 1
                break
            
        if check1 == False:
            Green[5][y] = 1
            Green[4][y] = 1
            
        check2 = False
        for i in range(1,5):
            if Blue[i+1][3-x] == 1 or Blue[i+1][3-x-1] == 1:
                check2 = True
                Blue[i][3-x] = 1
                Blue[i][3-x-1] = 1
                break
            
        if check2 == False:
            Blue[5][3-x] = 1
            Blue[5][3-x-1] = 1
    
    new_blue = deque()
    new_green = deque()
    
    while Green:
        k = Green.pop()
        if sum(k) == 4:
            Score += 1
            continue
        else:
            new_green.appendleft(k)
    
    #이동해야 하면 삭제
    if len(new_green) > 4:
        for i in range(len(new_green)-4-1,-1,-1):
            if sum(new_green[i]) != 0:
                new_green.pop()
    
    while len(new_green) < 6:
        new_green.appendleft([0]*4)
        
    while Blue:
        k = Blue.pop()
        if sum(k) == 4:
            Score += 1
            continue
        else:
            new_blue.appendleft(k)
    
    #이동해야 하면 삭제
    if len(new_blue) > 4:
        for i in range(len(new_blue)-4-1,-1,-1):
            if sum(new_blue[i]) != 0:
                new_blue.pop()
    
    while len(new_blue) < 6:
        new_blue.appendleft([0]*4)
    
    Blue = new_blue
    Green = new_green
        
Cnt = 0
for i in range(6):
    for j in range(4):
        if Blue[i][j] != 0:
            Cnt += 1
        if Green[i][j] != 0:
            Cnt += 1

print(Score)
print(Cnt)