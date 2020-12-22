A = [6, 3, 1, 4, 10, 8]
for j in range(0, len(A) - 1):
    mins = j
    for i in range(j + 1, len(A)):
        if A[i] < A[mins]:
            mins = i
    A[j], A[mins] = A[mins], A[j]
print(A)
