def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j < high and a[j] < a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[i]
    return j

def selection(a, low, high, k):
    pivot = partition(a, low, high)
    if k < pivot:
        return selection(a, low, pivot-1, k)
    elif k == pivot:
        return a[k]
    else:
        return selection(a, pivot+1, high, k)
    
input_list = [35, 91, 28, 47, 12, 60, 35, 99, 6, 20]
N = len(input_list)
k = input('0에서 N-1사이에서 k를 입력하시오: ')
position = selection(input_list, 0, N-1, int(k))
print(sorted(input_list))
print('{:2}번째 작은 수는 {:2}이다.'.format(k, position))