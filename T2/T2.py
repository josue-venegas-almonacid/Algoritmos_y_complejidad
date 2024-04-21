import time

def sumar_matrices(a, b, n):
    c = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(a[i][j] + b[i][j])
        c.append(fila)
    return c

def restar_matrices(a, b, n):
    c = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(a[i][j] - b[i][j])
        c.append(fila)
    return c

def multiplicarMatrices(a, b, n):
    c = []
    for i in range(n):
        c.append([])
        for j in range(n):
            c[i].append(a[i][0] * b[0][j])
            for k in range(1, n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def generar_submatrices(a, n):
    m1 = []
    m2 = []
    m3 = []
    m4 = []
    half = n // 2
    for i in range(half):
        m1.append(a[i][0:half])
        m2.append(a[i][half:])
    for i in range(half, n):
        m3.append(a[i][0:half])
        m4.append(a[i][half:])
    return m1, m2, m3, m4

def fusionar_matrices(m1, m2, m3, m4):
    resultado = []
    for i, row in enumerate(m1):
        resultado.append(row + m2[i])
    for i, row in enumerate(m3):
        resultado.append(row + m4[i])
    return resultado

def strassen(m1, m2, n):
    half = n // 2
    if n == 1:
        return [[m1[0][0] * m2[0][0]]]
    else:
        a, b, c, d = generar_submatrices(m1, n)
        e, f, g, h = generar_submatrices(m2, n)

        p1 = strassen(a, restar_matrices(f, h, half), half)
        p2 = strassen(sumar_matrices(a, b, half), h, half)
        p3 = strassen(sumar_matrices(c, d, half), e, half)
        p4 = strassen(d, restar_matrices(g, e, half), half)
        p5 = strassen(sumar_matrices(a, d, half), sumar_matrices(e, h, half), half)
        p6 = strassen(restar_matrices(b, d, half), sumar_matrices(g, h, half), half)
        p7 = strassen(restar_matrices(a, c, half), sumar_matrices(e, f, half), half)

        c1 = restar_matrices(sumar_matrices(p5, p4, half), restar_matrices(p2, p6, half), half)
        c2 = sumar_matrices(p1, p2, half)
        c3 = sumar_matrices(p3, p4, half)
        c4 = restar_matrices(sumar_matrices(p1, p5, half), sumar_matrices(p3, p7, half), half)

        return fusionar_matrices(c1, c2, c3, c4)

#MAIN

#INPUT
n = int(input("Ingrese el tamaño de las matrices: "))
inicio = time.time()

# Matrices en formato matriz[fila][columna]
a = []
b = []

for i in range(n):
    f = input("Ingrese los valores de la fila {} de la matriz A: ".format(i+1))
    fila = [int(x) for x in f.split()]
    a.append(fila)
for i in range(n):
    f = input("Ingrese los valores de la fila {} de la matriz B: ".format(i+1))
    fila = [int(x) for x in f.split()]
    b.append(fila)


#OUTPUT
print("\nMétodo tradicional")
print("-------------")

c1 = multiplicarMatrices(a, b, n)
finalNormal=time.time()
print(len(c1))

for lista in c1:
    for elem in lista:
        print(elem, end = " ")
    print("\n")


print("Método Strassen")
print("-------------")

c2 = strassen(a, b, n)
finalStrassen=time.time()
print(len(c2))

for lista in c2:
    for elem in lista:
        print(elem, end = " ")
    print("\n")

print("Metodo tradicional toma {} ".format(finalNormal-inicio))
print("Metodo Strassen toma {} ".format(finalStrassen-inicio))