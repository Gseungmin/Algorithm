def solution(survey, choices):
    List = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    
    score = dict()
    for x, y in List:
        score[x] = 0
        score[y] = 0


    for i in range(len(survey)):
        x, y = survey[i][0], survey[i][1]
        k = choices[i]
        if k <= 3:
            score[x] += 4-k
        elif 4 < k:
            score[y] += k-4


    answer = ""
    for x, y in List:
        if score[x] >= score[y]:
            answer += x
        else:
            answer += y
    return answer