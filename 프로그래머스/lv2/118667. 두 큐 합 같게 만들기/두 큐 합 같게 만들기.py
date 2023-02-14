def solution(queue1, queue2):
    #종료 조건
    Sum = sum(queue1) + sum(queue2)
    if Sum%2 == 1:
        return -1

    value = Sum//2 #각 큐가 가져야 하는 값
    if value == sum(queue1):
        return 0

    #투포인터로 접근
    L = len(queue1)+len(queue2)
    new_queue = queue1+queue2

    i = 0 #왼쪽 끝
    j = len(queue1)-1 #오른쪽 끝
    k = sum(queue1) #더한 값
    cnt = 0
    while 1:
        if j-i+1 == L: #길이가 초과한 경우
            break
        if k > value: #우리가 구해야 하는 값보다 큰경우
            k -= new_queue[i]
            i += 1
            if i > j: #i가 더 커진 경우
                if i >= len(new_queue):
                    break
                k = new_queue[i]
            j = max(i, j)
        elif k < value: #우리가 구해야 하는 값도가 작은 경우
            j += 1
            if j >= len(new_queue):
                break
            k += new_queue[j]
        elif k == value: #우리가 구해야 하는 값인 경우
            return cnt
        cnt += 1
        if j >= len(new_queue) or i >= len(new_queue):
            break
    return -1