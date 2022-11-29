def sum_list(list):    #ricordarsi i due punti quando si apre un blocco
    if len(list) == 0 :    #caso base in cui non ci siano elementi
        return None
    s = 0 
    for item in list:    #ricordarsi i due punti
        s = s + item;
    return s;

