import random

def quick_sort(lists):
    if len(lists) <= 1:
        return lists
    else:
        left = [i for i in lists[1:] if i< lists[0]]
        right = [i for i in lists[1:] if i>= lists[0]]
        return quick_sort(left)+lists[0:1]+quick_sort(right)

def insert_sort(lists):
    for i in range(1,len(lists)):
        key = lists[i]
        j = i-1
        while j>=0:
            if key < lists[j]:
                lists[j+1] = lists[j]
                lists[j] = key
            else:
                break
            j = j -1
    return lists


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)

if __name__ == '__main__':

    print('hello')
    n = 10
    arr = [0]*n
    for i in range(10):
        # arr = [5,6,9,2,1,8,3]
        arr[i] = random.randint(1,100)
    print(arr)

    # print(quick_sort(arr))
    # print(insert_sort(arr))
    print(merge_sort(arr))