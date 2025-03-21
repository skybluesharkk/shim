def solution(s):
    nums = list(map(int,s.split()))
    #print(nums)
    nums.sort()
    _max = max(nums)
    _min = min(nums)
    answer = str(_min)+' '+str(_max)
    return answer