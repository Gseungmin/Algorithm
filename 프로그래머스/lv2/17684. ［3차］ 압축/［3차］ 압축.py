#5:33
#전송 효율을 높이는 업무, 압축 전 정보를 완벽하게 복원 가능한 무손실 압축
#LZW 압축 구현
#길이가 1인 모든 단어를 포함
#

def solution(msg):
    answer = []
    
    alpha = dict()
    cnt = 1
    for i in range(65,91):
        alpha[chr(i)] = cnt
        cnt += 1
    
    i = 0
    while 1:
        Str = ""
        check = True
        for j in range(i,len(msg)):
            before = Str
            Str += msg[j]
            if Str not in alpha:
                alpha[Str] = cnt
                answer.append(alpha[before])
                cnt += 1
                i = j
                check = False
                break
        if check == True:
            answer.append(alpha[Str])
            break            
            
    return answer