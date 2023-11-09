#cap는 최대 택배 개수
#deliveries는 i+1번째 집에 배달할 택배 상자 수
#pickups는 i+1번째 집에서 수거할 택배 상자 수

#1. 0 위치에서 수거할 위치와 배달할 위치를 측정
#2. 수거할 위치와 배달할 위치 중 더 큰 곳이 이동할 위치
#3. 수거와 배달을 반복하며 두 과정이 끝날때까지 이동 거리를 합친 후 * 2 하기

def solution(cap, n, deliveries, pickups):
    
    deliveryStack = [] # [이동거리, 개수]
    pickupStack = [] # [이동거리, 개수]

    #스택 초기화
    for i in range(n):
        dist = i+1
        if deliveries[i] != 0:
            deliveryStack.append([dist, deliveries[i]])
        
        if pickups[i] != 0:
            pickupStack.append([dist, pickups[i]])
    
    #총 이동거리
    totalDist = 0
    
    if pickupStack and deliveryStack:
            dist = max(deliveryStack[-1][0], pickupStack[-1][0])
    
    while (pickupStack or deliveryStack):
        dist = 0
        
        #수거할 것만 없는 경우
        if (not pickupStack) and deliveryStack:
            dist = deliveryStack[-1][0]
        
        #배달할 것만 없는 경우
        if pickupStack and (not deliveryStack):
            dist = pickupStack[-1][0]
            
        #둘다 배달할 수 있는 경우
        if pickupStack and deliveryStack:
            dist = max(deliveryStack[-1][0], pickupStack[-1][0])
        
        totalDist += dist*2
        
        pos = cap #가능한 수거 택배 수
        while pickupStack:
            count = pickupStack[-1][1] #수거할 수 있는 개수
            if (count > pos): #수거할 개수가 더 많은 경우
                pickupStack[-1][1] = count-pos
                break
            else: #수거할 개수가 더 적은 경우
                pickupStack.pop()
                pos -= count
            
            #만약 가능한 수거 개수가 없다면
            if pos == 0:
                break
                
        pos = cap #가능한 배달 택배 수
        while deliveryStack:
            count = deliveryStack[-1][1] #수거할 수 있는 개수
            if (count > pos): #수거할 개수가 더 많은 경우
                deliveryStack[-1][1] = count-pos
                break
            else: #수거할 개수가 더 적은 경우
                deliveryStack.pop()
                pos -= count
            
            #만약 가능한 수거 개수가 없다면
            if pos == 0:
                break
                
            
    return totalDist