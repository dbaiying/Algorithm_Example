def merge(a, b):
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged


def merge_sort(c):
    if len(c) <= 1:
        return c
    mid = len(c) // 2
    a = merge_sort(c[:mid])
    b = merge_sort(c[mid:])
    return merge(a, b)


A = [32, 12, 44, 11, 43, 10, 33]
merge_sort(A)

print(merge_sort(A))
