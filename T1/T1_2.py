def ingresar_valores():
    n_columnas = int(input())                               # int
    id_columna = [int(x) for x in input().split(" ")]       # [id_columna1, id_columna2, ...]

    n_filas = int(input())                                  # int
    valores_dict = {}
    # R = {id_columna2: [int, int, ...], id_columna1: [int, int, ...], ...}
    # S = {id_columna1: [int, int, ...], id_columna3: [int, int, ...], ...}

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
    
    # Filtramos las columnas que coinciden entre ambas relaciones, y las que no
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
            n_columnas += 1
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


def triangulos_en_grafo(arcos):
    n_arcos = len(arcos)
    n_triangulos = 0
    for i, tupla1 in enumerate(arcos):
        flag = True
        if i+1 < n_arcos:
            j = i+1
            while j < n_arcos:
                tupla2 = arcos[j]
                if j+1 < n_arcos:
                    k = j+1
                    while k < n_arcos:
                        tupla3 = arcos[k]
                        if flag:
                            dict1 = {}
                            dict2 = {}
                            dict3 = {}
                            for pos_nodo in [0, 1]:
                                dict1[tupla1[pos_nodo]] = [tupla1[pos_nodo]]
                                dict2[tupla2[pos_nodo]] = [tupla2[pos_nodo]]
                                dict3[tupla3[pos_nodo]] = [tupla3[pos_nodo]]
                            union1 = join(dict1, dict2)
                            if union1[0][2]:        # si hay nodos coincidentes entre los dos arcos
                                union1 = union1[1]  # se bota toda la información menos la fila coincidente
                                dict1_2 = {}
                                for nodo in union1:
                                    dict1_2[nodo] = [nodo]
                                union2 = join(dict1_2, dict3)
                                if union2[0][2]:
                                    if union1 == union2[1]:
                                        n_triangulos += 1
                                        flag = False
                        k += 1
                j += 1
    return n_triangulos


# ——————————————————————————————— PARTE 2 ———————————————————————————————
arcos = []
triangulos = 0

flag = True
while flag:
    arco = input()
    if arco == "":
        flag = False
    else:
        x, y = arco.split(" ")
        arcos.append((int(x), int(y)))

print(triangulos_en_grafo(arcos))
