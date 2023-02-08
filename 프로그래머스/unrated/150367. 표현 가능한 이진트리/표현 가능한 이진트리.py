def solution(numbers):
    def change(x):
        y = ""
        while x>0:
            y=str(x%2)+y
            x//=2
        return y

    List = [change(i) for i in numbers]

    def fun(num):
        l = len(num)
        k = 2
        while k-1 < l:
            k *= 2
        while len(num) < k-1:
            num = "0"+ num
        return num

    answer = [1]*len(List)

    def tree(left, right, num, index):
        if left == right:
            return num[left]
        root = (left+right)//2
        A = tree(left,root-1,num, index)
        B = tree(root+1,right,num, index)

        if num[root] == "0":
            if A == "1":
                answer[index] = 0
            if B == "1":
                answer[index] = 0
        return num[root]

    for i in range(len(List)):
        num = fun(List[i])
        tree(0,len(num)-1,num,i)

    return answer