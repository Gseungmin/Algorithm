def solution(gems):
    cnt = dict()
    gem = dict()
    for i in gems:
        if i not in cnt:
            cnt[i] = 0
    i = 0
    j = 0
    ans = int(1e9)
    List = []
    while j < len(gems):
        if len(gem) == len(cnt):
            while cnt[gems[i]] > 1:
                cnt[gems[i]] -= 1
                i += 1
            if j-i < ans:
                left = i+1
                right = j
                ans = j-i
            gem[gems[j]] = True
            cnt[gems[j]] += 1
            j += 1
        else:
            gem[gems[j]] = True
            cnt[gems[j]] += 1
            j += 1
        if j == len(gems):
            while cnt[gems[i]] > 1:
                cnt[gems[i]] -= 1
                i += 1
            if j-i < ans:
                left = i+1
                right = j
                ans = j-i
    answer = []
    answer.append(left)
    answer.append(right)
    return answer