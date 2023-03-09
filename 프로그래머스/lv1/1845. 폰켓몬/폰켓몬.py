def solution(nums):
    answer = 0
    n = int(len(nums)/2)
    numss=list(set(nums))
    if (n>len(numss)):
        answer = len(numss)
    elif (n==len(numss)):
        answer = len(numss)
    else:
        answer = n
    return answer