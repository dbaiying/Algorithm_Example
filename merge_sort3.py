arr = [1, 4, 2, 5, 9, 10, 30, 6]


def merge(a, b):
    merged = []
    i = 0
    j = 0
    while len(a) > i and len(b) > j:  # 如果while len(a)>0 and len(b)>0,则此式永为真，当使用条件判断时,不能常量与常量比较
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
    # a = c[:mid]  c[:mid]不是已经拍好序的子数组
    # b = c[mid:]
    return merge(a, b)


print(merge_sort(arr))
