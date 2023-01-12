import sys
input = sys.stdin.readline

def electric_to_money(elec):
    money = 0
    if elec <= 100:
        money = elec*2
    elif elec <= 10000:
        money = 100*2 + (elec-100)*3
    elif elec <= 1000000:
        money = 100*2 + (10000-100)*3 + (elec-10000)*5
    elif elec > 1000000:
        money = 100*2 + (10000-100)*3 + (1000000-10000)*5 + (elec-1000000)*7
    return money

def money_to_electric(money):
    if money <= 200:
        elec = money//2
    elif money <= (100*2+(10000-100)*3):
        elec = (money-200)//3+100
    elif money <= (100*2+(10000-100)*3+(1000000-10000)*5):
        elec = (money-100*2-(10000-100)*3)//5+10000
    else:
        elec = (money-100*2-(10000-100)*3-(1000000-10000)*5)//7+1000000
    return elec

while 1:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    all_elec = money_to_electric(a)
    left = 1
    right = all_elec
    while left <= right:
        mid = (left+right)//2 #전기 사용량
        me = electric_to_money(mid) #내가 낼 돈
        nei_elec = all_elec-mid
        nei = electric_to_money(nei_elec)
        if me > nei: #내가 더 전기요금이 많을 경우
            right = mid-1
        else: #이웃이 더 많이 낸 경우
            if nei-me == b:
                print(me)
                break
            elif nei-me > b: #차이가 더 작아야 하는 경우, 즉 내가 더 내야 하는 경우
                left = mid+1
            elif nei-me < b:
                right = mid-1