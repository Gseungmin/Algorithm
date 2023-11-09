#users = [비율, 가격]
#emoticons = [각 이모티콘의 가격]

#1. 각 이모티콘 마다 할인율 설정
#2. 케이스가 완성이 되면 해당 케이스로 가격 측정, 그게 제한 가격보다 크다면 이모티콘 플러스 수 +1, 작다면 가격에 플러스
#3. 최종 정보에 따라 수정

def solution(users, emoticons):
    
    discount = [10, 20, 30, 40] #할인율    
    answer = [0, 0]
    
    RC(0, [], discount, users, emoticons, answer)
    
    return answer

def RC(index, case, discount, users, emoticons, answer):
    if (index == len(emoticons)):
        
        userCnt, totalPrice = 0, 0
        
        #각 유저를 돌면서 가격 측정 후, 가입 여부 확인 및 가격 더하기
        for i in range(len(users)):
            limitDC, limitPrice = users[i]
            userPrice = 0
            
            for j in range(len(case)):
                if limitDC <= case[j]:
                    userPrice += emoticons[j] * (100-case[j]) // 100
                    
            if userPrice >= limitPrice:
                userCnt += 1
            else:
                totalPrice += userPrice
        
        if userCnt > answer[0]:
            answer[0] = userCnt
            answer[1] = totalPrice
        elif userCnt == answer[0] and totalPrice > answer[1]:
            answer[1] = totalPrice
        
        return
    for i in range(4):
        case.append(discount[i])
        RC(index+1, case, discount, users, emoticons, answer)
        case.pop()
    return
    