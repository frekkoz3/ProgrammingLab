class ExamException(Exception): 
    pass

def compute_max_difference(day):
    if len(day) == 1:
        return None
    else:
        return abs(max(day) - min(day))

def compute_daily_max_difference(time_series):

    #controllino sul tipo di time_series (fa mai male)
    if not isinstance(time_series, list):
        raise ExamException('time_series non contenuti in una lista')
    
    #mi divido i timeseries per giorni in un dizionario
    days = {}
    
    for row in time_series:

        epoch = row[0]
        temperature = row[1]
        starting_day = epoch - epoch%86400

        #se ho uno starting_day già inserito basta che aggiungo
        if starting_day in days:
            days[starting_day].append(temperature)
        #se uno starting_day non è ancora inserito allora creo la chiave ed aggiungo
        else:
            days[starting_day] = []
            days[starting_day].append(temperature)

    #calcolo i vari daily_max_difference
    daily_max_difference = []

    for starting_day in days:
        daily_max_difference.append(compute_max_difference(days[starting_day]))
        
    return daily_max_difference