import random

# 단어가 주어지면 이렇게 주어지는 사전순으로 
# 그러면 처음에 해당하는 것들 순서쌍 먼저 만든뒤에 그 다음에 그걸 하나씩 비교해가면서 순서쌍 앞에 빠른거만 저장하는 식으로 넘어가면 될듟

def plus_str(m_l):
    tmp=""
    for j in range(len(m_l)):
        tmp+=m_l[j]
    return tmp

my_str = list(input())

def make_sol(my_list):
    # 순서쌍을 먼저 만들어 내야함
    orders = []
    for i in range(len(my_str)-1):
        for j in range(i+1,len(my_str)-1):
            orders.append([i,j])
    #print(orders)

    ans = []
    tmp1 = []
    tmp2 = []
    tmp3 = []
    ans = ""
    re = []
    for j in range(len(orders)):
        for i in range(len(my_str)):
            if i<=orders[j][0]:
                tmp1.append(my_str[i])
            elif i<=orders[j][1]:
                tmp2.append(my_str[i])
            else:
                tmp3.append(my_str[i])
        tmp1.reverse()
        tmp2.reverse()
        tmp3.reverse()

        tmp4 = plus_str(tmp1)+plus_str(tmp2)+plus_str(tmp3)
        tmp1,tmp2,tmp3 = [],[],[]
        if ans == "":
            ans = tmp4
        elif ans>tmp4:
            ans = tmp4
        #print(ans)
        
        #re.append(ans)
    print(ans)
    pass

make_sol(my_str)