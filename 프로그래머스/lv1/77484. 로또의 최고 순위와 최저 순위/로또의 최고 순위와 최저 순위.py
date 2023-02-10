def solution(lottos, win_nums):
    
    #로또 번호 정리
    win = dict()
    for i in range(6):
        win[win_nums[i]] = True

    #순위
    level = dict()
    for i in range(7):
        if i == 0 or i == 1: #한개 또는 아예 못 맞춘 경우
            level[i] = 6
        else:
            level[i] = 7-i

    #최저 경우 구하기, 0의 개수 구하기
    zero = 0 #0의 개수
    equal = 0 #맞힌 로또 번호의 개수
    for i in range(6):
        if lottos[i] in win:
            equal += 1
        elif lottos[i] == 0:
            zero += 1

    #가능한 범위
    pos = zero+equal
    answer = [level[pos],level[equal]]
    
    return answer