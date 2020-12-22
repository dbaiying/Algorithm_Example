def binary_search(arr, a):
    left, right = 0, len(arr) - 1
    while right - left >= 0:
        mid = (right + left) // 2
        if arr[mid] == a:
            return mid
        elif arr[mid] > a:
            right = mid - 1
        elif arr[mid] < a:
            left = mid + 1
    return False


A = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(A, 10))
print(binary_search(A, 9))
print(binary_search(A, 8))
print(binary_search(A, 7))
print(binary_search(A, 6))
print(binary_search(A, 5))
print(binary_search(A, 4))
print(binary_search(A, 3))
print(binary_search(A, 2))
print(binary_search(A, 1))
print(binary_search(A, 0))

print(A[binary_search(A, 6)])
