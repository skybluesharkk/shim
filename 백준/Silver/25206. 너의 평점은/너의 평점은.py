import sys

# 전체를 입력 받는 방법을 알아낸다.
# 공백을 기준으로 슬라이싱 한다.
# 슬라이싱 한 뒤 앞 전공과목 이름 부분은 버린다. -> 필요 없음
# 학점 곱을 구한다.
# 총 학점을 나눠서 평점을 구한다.
# 평점을 구한 뒤 오차 값, 소숫점 값이 문제의 기준과 같은 지 확인한다.
# p인 과목은 계산에서 제외하여야 한다.


data = [sys.stdin.readline().split() for i in range(20)]

#print(data)
total = 0
total_2 = 0
for j in range(20):
    if data[j][2] == 'A+':
        total_2 += float(data[j][1])
        total += float(data[j][1])*float(4.5)
        pass
    elif data[j][2] == 'A0':
        total_2 += float(data[j][1])
        total += float(data[j][1]) * float(4.0)
        pass
    elif data[j][2] == 'B+':
        total_2 += float(data[j][1])
        total += float(data[j][1]) * float(3.5)
        pass
    elif data[j][2] == 'B0':
        total_2 += float(data[j][1])
        total += float(data[j][1]) * float(3.0)
        pass
    elif data[j][2] == 'C+':
        total_2 += float(data[j][1])
        total += float(data[j][1]) * float(2.5)
        pass
    elif data[j][2] == 'C0':
        total_2 += float(data[j][1])
        total += float(data[j][1]) * float(2.0)
        pass
    elif data[j][2] == 'D+':
        total_2 += float(data[j][1])
        total += float(data[j][1]) * float(1.5)
        pass
    elif data[j][2] == 'D0':
        total_2 += float(data[j][1])
        total += float(data[j][1]) * float(1.0)
        pass
    elif data[j][2] == 'F':
        total_2 += float(data[j][1])
        total += float(data[j][1]) * float(0.0)
        pass
    elif data[j][2] == 'P':
        #total_2 += float(data[j][1])
        pass

print(total/total_2)