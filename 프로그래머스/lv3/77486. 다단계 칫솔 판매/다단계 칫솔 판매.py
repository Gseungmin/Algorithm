import sys
sys.setrecursionlimit(10**5)

#10프로 넘기고 남은거 먹기, name이 center일때 까지 진행
def RC(money, name, price, tree):
    if name == "-":
        price[name] += money
        return
    value = money//10 #추천인 금액
    price[name] += (money-value)
    if value == 0:
        return
    RC(value, tree[name], price, tree)
    return

def solution(enroll, referral, seller, amount):
    #가격 초기화
    for i in range(len(amount)):
        amount[i] = amount[i]*100

    tree = dict() #부모를 가리키는 트리 구조
    for i in range(len(enroll)):
        name = enroll[i]
        tree[name] = referral[i]

    #수익 초기화
    price = dict()
    price["-"] = 0
    for i in enroll:
        price[i] = 0

    #재귀 함수 호출 
    for i in range(len(seller)):
        RC(amount[i], seller[i], price, tree)

    answer = []
    for i in enroll:
        answer.append(price[i])
    
    return answer