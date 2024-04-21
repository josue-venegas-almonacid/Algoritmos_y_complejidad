import fileinput
import sys

def BBinaria(arr, inicio, final, elm):
    if final >= inicio:
        pivote = (final + inicio) // 2
        if arr[pivote] == elm:
            if pivote > 0:  # encontrar primera aparición de j
                while arr[pivote - 1] == elm and pivote > 0:  
                    pivote -= 1
            return pivote
        elif arr[pivote] > elm:
            return BBinaria(arr, inicio, pivote - 1, elm)
        else:
            return BBinaria(arr, pivote + 1, final, elm)
    else:
        return -1

aux=1
for line in fileinput.input():
    if fileinput.isfirstline():
        n=int(line.rstrip())
    else:
        if aux>0:
            precios=[int(x) for x in line.rstrip().split(" ")]
            aux=-1
        else:
            m=int(line.rstrip())         

i = 0
while i < n:
    libro1 = precios[i]
    precios[i] = -1
    j = BBinaria(precios, 0, n, (m - libro1))
    if j != -1:
        if i <= j:
            sys.stdout.write("{} {}".format(i+1, j+1))
        else:
            sys.stdout.write("{} {}".format(j+1, i+1))
        n = 0
    precios[i] = libro1
    i += 1