def solution(arr1, arr2):
    answer = [[]]
    rows_a = len(arr1)
    cols_a = len(arr1[0])
    cols_b = len(arr2[0])
    
    answer = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    
    for i in range(len(arr1)):
        for j in range(cols_b):
            for k in range(cols_a):
                answer[i][j]+=arr1[i][k]*arr2[k][j]

    return answer