def solution(s):
    answer = True
    ss = list(s)
    ans=[] #stack
    #print(len(ss))
    
    for i in range(len(ss)):
        if ss[i]=='(':
            ans.append(ss[i])
        else:
            if ans == []:
                return False
            else:
                ans.pop()
    if ans !=[]:
        return False

    return True