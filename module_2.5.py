def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        a = []
        matrix.append(a)
        for j in range(m):
            a.append(value)
    return matrix

result_1 = get_matrix(2, 5, 7)
result_2 = get_matrix(4, 6, 8)
result_3 = get_matrix(1, 5, 10)
print(result_1)
print(result_2)
print(result_3)