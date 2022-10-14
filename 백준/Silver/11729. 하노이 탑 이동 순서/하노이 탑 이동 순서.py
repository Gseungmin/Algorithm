def hanoi(N, start, end, List):
    """원판을 하나씩 옮기는 함수"""
    if N == 0: #basecase 더이상 옮길 원판이 없는 경우
        return
    if N == 1: #basecase 원판을 하나만 옮기면 되는 경우
        List.append(start)
        List.append(end)
        hanoi(N-1, start, end, List)
    else:
        other = 6 - start - end
        hanoi(N-1, start, other, List) #맨 밑 하나를 옮겼으므로 N-1개를 옮겨야 한다
        List.append(start)
        List.append(end)
        hanoi(N-1, other, end, List)
    return List

num = int(input()) #원판의 개수
answer = hanoi(num, 1, 3, [])
print(len(answer)//2)
for i in range(0,len(answer),2):
    print(answer[i], answer[i+1])