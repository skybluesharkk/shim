def solution(arr):
    answer = []
    for i in range(len(arr)):
        if (i==0):
            answer.append(arr[i])
        if (arr[i] != answer[-1]):
            answer.append(arr[i])
    return answer