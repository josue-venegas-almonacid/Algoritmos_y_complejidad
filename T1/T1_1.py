def ingresar_valores():
    n_columnas = int(input())                               #int
    id_columna = [int(x) for x in input().split(" ")]       #[id_columna1, id_columna2, ...]

    n_filas = int(input())                                  #int
    valores_dict = {}
    #R = {id_columna2: [int, int, ...], id_columna1: [int, int, ...], ...}
    #S = {id_columna1: [int, int, ...], id_columna3: [int, int, ...], ...}

    for i in id_columna:
        valores_dict[i] = []
    
    for i in range(n_filas):
        linea_nr = input()
        linea_nr = [int(x) for x in linea_nr.split(" ")]
        for i, valor in enumerate(id_columna):
            valores_dict[valor].append(linea_nr[i])
    return [n_columnas, id_columna, n_filas, valores_dict]  

def revisar_columna_help(R, S, id_c, i_R, i_S, n):
    columna = id_c[n]
    if R[columna][i_R] == S[columna][i_S]:
        if n+1 == len(id_c):
            return [True, [i_R, i_S]]
        else:
            return revisar_columna_help(R, S, id_c, i_R, i_S, n+1)
    else:
        return [False, []]

def revisar_columna(R, S, id_c):
    if id_c:
        columna = id_c[0]
        filas_coinciden = []
        for i, elemento_R in enumerate(R[columna]):
            for j, elemento_S in enumerate(S[columna]):
                if elemento_R == elemento_S:
                    if len(id_c) > 1:       # varias columnas coincidentes
                        r_c = revisar_columna_help(R, S, id_c, i, j, 1)
                        if r_c[0]:
                            filas_coinciden.append(r_c[1])
                    else:       # 1 columna coincidente
                        filas_coinciden.append([i, j])           
        return filas_coinciden
    else:
        return []

def join(dict1, dict2):

    id_c = []
    id_nc_nr = []
    id_nc_ns = []
    
    #Filtramos las columnas que coinciden entre ambas relaciones, y las que no
    for id1 in dict1.keys():
        if id1 in dict2.keys():
            id_c.append(id1)        
        else:
            id_nc_nr.append(id1)

    for id2 in dict2.keys():
        if id2 not in dict1.keys():
            id_nc_ns.append(id2)
    

    coincidentes = revisar_columna(dict1, dict2, id_c)
    filas_c = []
    n_columnas = len(dict1.keys())
    headers = list(dict1.keys())
    
    for key in dict2:
        if key not in id_c:
            n_columnas+=1
            headers.append(key)

    filas_c = [[n_columnas, headers, len(coincidentes)]]
    
    for tupla in coincidentes:
        fila = []
        for columna in dict1:
            fila.append(dict1[columna][tupla[0]])
        for columna in dict2:
            if columna not in id_c:
                fila.append(dict2[columna][tupla[1]])
        filas_c.append(fila)
    
    return filas_c


######################  MAIN  ######################

print("\n--------   INPUT  --------\n")
n, n_valores, nr, nr_valores = ingresar_valores()
m, m_valores, ns, ns_valores = ingresar_valores()

print("\n--------   OUTPUT  --------\n")

result = join(nr_valores, ns_valores)

#No Columnas
print(result[0][0])
#Columnas
print(*result[0][1])
#No Filas
print(result[0][2])
#Filas
for fila in result[1:]:
    print(*fila)


#No Columnas        3
#Columnas           0 1 2
#No Filas JOIN      4
#Filas Join         1 2 3
#                   5 2 3
#                   4 5 3
#                   3 5 3