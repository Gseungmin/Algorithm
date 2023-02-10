#이모티콘의 모든 할인 경우의 수
def RC(index,info,users,emoticons,case,answer):
    if index == len(emoticons):
        
        cnt = 0 #서비스 가입자 수
        price = 0
        
        #모든 유저를 확인
        for user in users:
            percent, upper = user
            Sum = 0 #각 유저당 구매 값의 총 합
            check = False #유저가 서비스 가입할지 안할지 정함
            for i in range(len(info)):
                if info[i] >= percent: #구매 경우
                    Sum += emoticons[i]*(100-info[i])//100
                    if Sum >= upper: #값보다 큰 경우
                        check = True
                        break
            if check == False: #가입자가 아니면
                price += Sum
            else: #가입자면
                cnt += 1
        
            if answer[0] < cnt: #현재 경우가 서비스 가입자가 더 많은 경우
                answer[0] = cnt
                answer[1] = price 
            elif answer[0] == cnt: #서비스 가입자가 같은 경우
                answer[1] = max(answer[1], price)
        return
    
    for i in range(4):
        info.append(case[i])
        RC(index+1,info,users,emoticons,case,answer)
        info.pop()
    return

def solution(users, emoticons):
    case = [10,20,30,40]
    answer = [0,0]
    RC(0,[],users,emoticons,case,answer)
    return answer