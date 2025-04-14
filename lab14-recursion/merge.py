def merge(src, low, mid, high, dst):
    i = low
    j = mid + 1
    for k in range(low, high + 1):
        if i > mid :
            dst[k] = src[j]
            j += 1
        elif j > high:
            dst[k] = src[j]
        elif src[i] < src[j]:
            dst[k] = src[i]
            i += 1
        else:
            dst[k] = src[j]
            j += 1


data = [0, 1, 5, 2, 7,9, 11]
