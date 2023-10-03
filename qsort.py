def partition(a, low, high):
    pivot = low
    i = low + 1
    j = high

    while True:
        while i <= j and a[i] <= a[pivot]:
            i += 1
        while i <= j and a[j] >= a[pivot]:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            break

    a[pivot], a[j] = a[j], a[pivot]
    return j

def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot - 1)
        qsort(a, pivot + 1, high)

a = [54, 88, 77, 26, 93, 17, 49, 10, 17, 77, 11, 31, 22, 44, 17, 20]
print('정렬 전:\t', a)
qsort(a, 0, len(a) - 1)
print('정렬 후:\t', a)
