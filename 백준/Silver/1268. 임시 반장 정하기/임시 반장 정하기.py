'''
백준 
처음에 숫자를 받으면 임시로 만든 리스트에 쭉 담는다.
그럼 2차원 배열이 하나 완성되겠지?
[[],[],[],...,[]] 같은 형식으로
각 학생에 맞는 딕셔너리를 만든다.
그 다음 2중 for문으로 교차 검증을 한다..
이중 포문을 돌면서 같은 숫자가 나올때마다 카운트 수를 1씩 증가한다.
한번 반복이 끝날 때 카운트를 한번 딕셔너리에 추가한다.
딕셔너리의 최솟값을 찾는다.
찾은 다음 만약 같다면, 더 작은 밸류의 값을 출력한다.
파이썬 딕셔너리를 정렬한 다음, 제일 앞 밸류를 출력하면 될 것 같다.



'''
import sys

total_stu = []
ans={}
num = int(input())
for i in range(num):
    k = list(map(int,sys.stdin.readline().strip().split()))
    total_stu.append(k)
#print(total_stu)

cnt = 0
bag = []
for i in range(len(total_stu)):
    for j in range(5):
        for k in range(len(total_stu)):
            #print('case',total_stu[i][j],total_stu[k][j])
            if total_stu[i][j] == total_stu[k][j]:
                if i==k:
                    pass
                elif k in bag:
                    pass
                else:
                    bag.append(k)
                    #print(bag)
                    #print('same!',total_stu[i][j],total_stu[k][j])
                    cnt+=1
    #print('i',i,cnt)
    ans[i]=len(bag)
    cnt=0
    bag=[]
#print(ans)

sort_ans = sorted(ans.items(),key=lambda x:x[1], reverse=True)
#print(sort_ans)
print(sort_ans[0][0]+1)