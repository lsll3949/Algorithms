def selection_sort(i):
    if len(i) <= 1:
        return i
    
    pivot = i[len(i) // 2]
    left = [x for x in i if x < pivot]
    middle = [x for x in i if x == pivot]
    right = [x for x in i if x > pivot]

    # 분할 정복: 왼쪽, 중간, 오른쪽 부분 문제를 재귀적으로 정렬
    return selection_sort(left) + middle + selection_sort(right)

i = [150, 160, 170, 180, 190]
sorted_i = selection_sort(i)
print(sorted_i)