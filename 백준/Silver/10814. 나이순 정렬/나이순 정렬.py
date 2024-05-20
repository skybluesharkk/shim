'''
1. 일단 들어오는 순서대로 입력을 받는다.
2. 입력을 받으면 받는 순서대로 리스트의 이름 값을 처리한다 - 딕셔너리?
-> 딕셔너리를 사용하는 방법 괜찮은 거 같다.
딕셔너리에 순서랑 이름을 매칭해놓고
원래 리스트에는 이름을 지우고 순서만 남겨놓자.
3. 순서만 가지고 먼저 모든 정렬을 끝낸 다음에
4. 출력할 때 순서에 맞는 이름을 딕셔너리에 불러온다.
5. 딕셔너리를 사용할 시 같은 문자열로 이루어진 중복된 이름을 처리할 수 없다는 단점이 발생한다.
6. 이러한 문제를 해결하기 위해서 그냥 리스트를 사용할 까 싶었지만 그러면 나중에 찾을 때 여러번 뒤져야 하는 문제가 발생한다.

'''
person = {}
ans = []
num = int(input())
for i in range(num):
    age,name = map(str,input().split())
    person[i]=name
    ans.append([int(age),i])

#print(ans)
#print(person)

def merge(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    return merge_func(left,right)

def merge_func(left,right):
    merge_list = []
    left_id,right_id = 0,0

    while len(left)>left_id and len(right) > right_id:
        if left[left_id]>right[right_id]:
            merge_list.append(right[right_id])
            right_id+=1
        else:
            merge_list.append(left[left_id])
            left_id+=1
    while len(left) > left_id and len(right) <= right_id:
        merge_list.append(left[left_id])
        left_id +=1
    while len(right) > right_id and len(left) <= left_id:
        merge_list.append(right[right_id])
        right_id+=1

    return merge_list
try:
    ans = merge(ans)
    #print(ans)

    for j in range(num):
        print(str(ans[j][0])+" "+person[ans[j][1]])
except:
    RuntimeError