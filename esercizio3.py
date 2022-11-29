def sum_csv(file_name):
    my_file = open(file_name,'r') 
    vuoto = True #booleana che mi dirà se il mio dataset è vuoto ergo pieno di None
    sum = 0 
    row = 0 #lo faccio per prevenire il caso in cui l'intestazione sia diversa dal solito
    for item in my_file: 
        values = item.split(',') #so che questo csv è diviso da virgole
        try:
            if(item != None and row != 0):
                vuoto = False
                sum += float(values[1]) 
        except ValueError: #sia che sia sbagliato tipo che sia None funziona
                pass
        row += 1
    if(vuoto):
        return None
    return sum 