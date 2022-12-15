from esercizio7 import FitIncrementModel
import random

#questo è un esperimento che va a vedere come cambia la previsione
#di uno stesso dataset in funzione del time 
#(time è la variabile che mi indica quando un dato si inserisce nel 
#historic_data)

#questo programma va eseguito nel prompt dei comandi con il file
#dell'esercizio 7 nella stessa directory

#questa è la versione che mostra il grafico delle previsioni in 
#funzione di time l'una diversa dalle altre

#@frekko

data = [25]
for i in range(100):
    sign = random.randrange(11)
    n = random.randrange(20)
    if sign < 3:
        n = data[i] - n
        data.append(n)
    else:
        n = data[i] + n
        data.append(n)

print(data)
prediction = []

for i in range (len(data) - 4):
    time = i + 3
    historic_data = data[:(len(data)-time)]
    latest_data = data[-time:]
    model = FitIncrementModel()
    model.fit(historic_data)
    pred_value = model.predict(latest_data)
    prediction.append(pred_value)

from matplotlib import pyplot

pyplot.plot(prediction, color = 'tab:blue')
pyplot.show()