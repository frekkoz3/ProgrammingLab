def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return(res)

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def factorial(n):
    product = 1
    for i in range (1, n+1):
        product = product * i
    return product

def permut(list):
    permut_list = list[::]
    permut_list = swap(permut_list, len(list)-1, 0)
    pos_pivot = 0
    conta_permuta = 1
    while convert(permut_list) != convert(list):
        new_pos_pivot = pos_pivot + 1 if (pos_pivot + 1) < len(list) else 0
        permut_list = swap(permut_list, pos_pivot, new_pos_pivot)
        pos_pivot = new_pos_pivot
        conta_permuta = conta_permuta + 1
    return conta_permuta

def test_permut(massimo):
    list = []
    conta_permut = []
    for i in range (3, massimo):
        element = []
        for j in range (1, i+1):
            element.append(j)
        list.append(element)
        conta_permut.append(permut(element))    

    #ABBIAMO TROVATO CHE 
    #IL RAPPORTO TRA DESIDERATO (DES) ED OTTENUTO (OTT)
    #E' 1 : (DIM DEL PREC : DES DEL PREC)
    #DUNQUE VOGLIAMO (N-2)! DIVERSI PUNTI DI PARTENZA
    #COSI' DA OTTENERE N FATTORIALI DIVERSE PERMUTAZIONI
    #(CIOE' TUTTE LE PERMUTAZIONI)

print()
test_permut(8)