def merge_sort(a,b,low,high):
    if high <= low:
        return
    mid = low + (high - low) // 2
    merge_sort(a,b,low,mid)
    merge_sort(a,b,mid+1,high)
    merge_sort(a,b,low,mid,high)

input_list = [37,10,22,30,35,13,25,24]
aux = [None] * len(input_list)
print('정렬 전:\t', input_list)
merge_sort(input_list, aux, 0, len(input_list)-1)
print('정렬 후 :', input_list)

def merge(a,b,low,mid,high):
    i = low
    j = mid+1
    for k in range(low, high+1):
        if i > mid:
            b[k] = a[j]
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1
        elif j > high:
            a[j] = a[i]
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1
    for k in range(low, high+1):
        a[k] = b[k]