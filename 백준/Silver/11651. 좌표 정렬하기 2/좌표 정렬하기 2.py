'''
퀵소트 활용

피벗이 있어야 함

'''
import sys

n = int(sys.stdin.readline().strip())
dots = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    dots.append([x,y])

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [],[],[]
    for i in range(len(arr)):
        if arr[i][1] < pivot[1]:
            lesser_arr.append(arr[i])
        elif arr[i][1] > pivot[1]:
            greater_arr.append(arr[i])
        else:
            if arr[i][0]>pivot[0]:
                greater_arr.append(arr[i])
            elif arr[i][0]<pivot[0]:
                lesser_arr.append(arr[i])
            else:
                equal_arr.append(arr[i])
    return quick_sort(lesser_arr)+equal_arr+quick_sort(greater_arr)

res = quick_sort(dots)
for k in range(len(res)):
    print(res[k][0],res[k][1])