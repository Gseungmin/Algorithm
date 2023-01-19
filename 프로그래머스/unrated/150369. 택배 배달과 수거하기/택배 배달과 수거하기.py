def solution(cap, n, deliveries, pickups):
    deliv_stack = []
    pick_stack = []
    for i in range(n):
        if deliveries[i] != 0:
            deliv_stack.append([i,deliveries[i]])
        if pickups[i] != 0:
            pick_stack.append([i,pickups[i]])

    deliv_sum = sum(deliveries)
    pick_sum = sum(pickups)

    dist = 0
    while 1:

        if deliv_sum == 0 and pick_sum == 0:
            answer = dist*2
            break

        if deliv_sum == 0 and pick_sum != 0:
            d = pick_stack[-1][0]+1
            cnt = min(cap, pick_sum)
            while 1:
                if pick_stack[-1][1] > cnt:
                    pick_stack[-1][1] -= cnt
                    pick_sum -= cnt
                    break
                else:
                    pick_sum -= pick_stack[-1][1]
                    cnt -= pick_stack[-1][1]
                    pick_stack.pop()
                if not pick_stack or cnt == 0:
                    break
            dist += d

        elif deliv_sum != 0 and pick_sum == 0:
            d = deliv_stack[-1][0]+1
            cnt = min(cap, deliv_sum)
            while 1:
                if deliv_stack[-1][1] > cnt:
                    deliv_stack[-1][1] -= cnt
                    deliv_sum -= cnt
                    break
                else:
                    deliv_sum -= deliv_stack[-1][1]
                    cnt -= deliv_stack[-1][1]
                    deliv_stack.pop()
                if not deliv_stack or cnt == 0:
                    break
            dist += d

        else:
            d = max(pick_stack[-1][0], deliv_stack[-1][0])+1
            dist += d

            #배달
            cnt = min(cap, deliv_sum)
            while 1:
                if deliv_stack[-1][1] > cnt:
                    deliv_stack[-1][1] -= cnt
                    deliv_sum -= cnt
                    break
                else:
                    deliv_sum -= deliv_stack[-1][1]
                    cnt -= deliv_stack[-1][1]
                    deliv_stack.pop()
                if not deliv_stack or cnt == 0:
                    break

            #수거
            cnt = min(cap, pick_sum)
            while 1:
                if pick_stack[-1][1] > cnt:
                    pick_stack[-1][1] -= cnt
                    pick_sum -= cnt
                    break
                else:
                    pick_sum -= pick_stack[-1][1]
                    cnt -= pick_stack[-1][1]
                    pick_stack.pop()
                if not pick_stack or cnt == 0:
                    break
                
    return answer