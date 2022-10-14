import sys
input = sys.stdin.readline
Map = [list(map(int,input().split())) for i in range(9)]

def check_row(Map):
	List = [[0]*10 for i in range(9)]
	for x in range(9):
	    for y in range(9):
		    if Map[x][y] != 0:
		        List[x][Map[x][y]] = 1
	return List
	
def check_col(Map):
	List = [[0]*10 for i in range(9)]
	for x in range(9):
	    for y in range(9):
		    if Map[x][y] != 0:
		        List[y][Map[x][y]] = 1
	return List
		
def check_squ(Map):
	List = [[0]*10 for i in range(9)]
	for i in range(9):
		for j in range(9):
		    if Map[i][j] != 0:
		        List[j//3+(i//3)*3][Map[i][j]] = 1
	return List
	
row = check_row(Map)
col = check_col(Map)
squ = check_squ(Map)

N = 0
for i in range(9):
    for j in range(9):
        if Map[i][j] == 0:
            N += 1

def RC(index):
    if index == 81:
        for i in range(9):
            for j in range(9):
                print(Map[i][j], end = " ")
            print()
        sys.exit()
    x, y = index//9, index%9
    if Map[x][y] != 0:
        RC(index+1)
    else:
        for k in range(1,10):
            if row[x][k] == 0 and col[y][k] == 0 and squ[y//3+(x//3)*3][k] == 0:
                row[x][k] = col[y][k] = squ[y//3+(x//3)*3][k] = 1
                Map[x][y] = k
                RC(index+1)
                Map[x][y] = 0
                row[x][k] = col[y][k] = squ[y//3+(x//3)*3][k] = 0
    return
RC(0)