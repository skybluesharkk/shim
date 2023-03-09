def solution(array, commands):
    answer=[]
    for i in range(len(commands)):
        ans=[]
        if (commands[i][0]==commands[i][1]):
            ans.append(array[commands[i][0]-1])
        else:
            ans = array[int(commands[i][0]-1):int(commands[i][1])]
        ans.sort()
        print(ans,i)
        answer.append(ans[commands[i][2]-1])

    return answer