import sys
sys.setrecursionlimit(10**6)

def merge(arr):
    if len(arr) <=1:
        return arr

    mid = len(arr)//2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    return merge_func(left,right)

def merge_func(left,right):
    merge_list = []
    left_id, right_id = 0,0

    while len(left)>left_id and len(right) > right_id:
        if left[left_id]>right[right_id]:
            merge_list.append(right[right_id])
            right_id += 1
        else:
            merge_list.append(left[left_id])
            left_id += 1
    while len(left) > left_id and len(right) <= right_id:
        merge_list.append(left[left_id])
        left_id += 1
    while len(right) > right_id and len(left) <= left_id:
        merge_list.append(right[right_id])
        right_id+=1

    return merge_list

input=sys.stdin.readline

num = int(input())

box=[]


for i in range(num):
    plus=int(input())
    box.append(plus)
box = merge(box)
#print(box)


for j in range(len(box)):
    print(box[j])