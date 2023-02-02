from CSVTimeSeriesFile import TimeSeriesCSVFile

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
    
    #mi divido i timeseries per giorni
    days = []
    dim = len(time_series)
    
    for i, row in enumerate(time_series):

        #caso in cui ci troviamo alla prima riga
        if i == 0:
            temperature = row[1]
            epoch = row[0]
            #questo mi dice quanto mi manca ad arrivare al prossimo giorno
            day_start_epoch = epoch - (epoch % 86400)
            day = []
            day.append(temperature)

        #tutte le righe di mezzo 
        elif i < (dim - 1): 
            epoch = row[0]

            #epoch di uno stesso giorno
            if epoch - day_start_epoch < 86400:
                #qui devo aggiungere la temperatura al giorno 
                temperature = row[1]
                day.append(temperature)

            #epoch di giorni diversi
            elif epoch - day_start_epoch >= 86400:
                days.append(day)
                print(day)
                print()
                day_start_epoch = epoch - (epoch % 86400)
                #qui devo creare nuovo giorno
                day = []
                temperature = row[1]
                day.append(temperature)

        #caso dell'ultima riga
        else:
            epoch = row[0]

            #epoch di uno stesso giorno
            if epoch - day_start_epoch < 86400:
                #qui devo aggiungere la temperatura al giorno 
                temperature = row[1]
                day.append(temperature)

            #epoch di giorni diversi
            else :
                days.append(day)
                #qui devo creare nuovo giorno
                day = []
                temperature = row[1]
                day.append(temperature)
        
            #essendo l'ultima riga aggiungo in ogni caso il giorno
            days.append(day)
            
    daily_max_difference = []

    for day in days:
        daily_max_difference.append(compute_max_difference(day))
        
    return daily_max_difference

m = TimeSeriesCSVFile('data.csv')

days = compute_daily_max_difference(m.get_data())

print(days)
output = open('output', 'w')
for day in days:
    output.write(str(day))
    output.write('\n')
        