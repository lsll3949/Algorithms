def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # 종료 조건: 더이상 나눌 수 없는 경우

    pivot = arr[len(arr) // 2]  # 피벗을 중앙 원소로 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 분할 정복: 왼쪽, 중간, 오른쪽 부분 문제를 재귀적으로 정렬
    return quick_sort(left) + middle + quick_sort(right)

# 테스트
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)
