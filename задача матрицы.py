import random
# Печать
def print_m(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
# функция сооздания мматрицы н*н
def random_matrix(n):
    m = []

    for i in range(n):
        lst = []
        for j in range(n):  
            lst.append(random.randint(-num, num))
        m.append(lst)   
    return m

num = 25
n = 10
matrix1= random_matrix(n)
print("печать 1-ой матрицы")
print_m(matrix1)
matrix2= random_matrix(n)
print("печать 2-ой матрицы")
print_m(matrix2)

matrix3 = [[0] * n for i in range(n)]
print_m(matrix3)
for i in range(n):
    for j in range(n):
        matrix3[i][j] = matrix1[i][j]+matrix2[i][j]
print_m(matrix3)