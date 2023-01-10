from esercizio5 import *
from esercizio7 import FitIncrementModel

#esperimento ben riuscito che stampa il grafico di 
#shampoo_sales.csv ed inoltre 
#ci abbina un po' tutte le predizioni che vogliamo 
#fatte con la 

name = 'shampoo_sales.csv'
file = NumericalCSVFile(name)
data = file.get_data()

sales_data = []

for item in data:
    sales_data.append(item[-1])

print(sales_data)

model = FitIncrementModel()

prediction = []

for i in range (len(data) - 4):
    time = i + 3
    historic_data = sales_data[:(len(sales_data)-time)]
    latest_data = sales_data[-time:]
    model = FitIncrementModel()
    model.fit(historic_data)
    pred_value = model.predict(latest_data)
    prediction.append(pred_value)

from matplotlib import pyplot

for item in prediction:
   pyplot.plot(sales_data + [item], color='tab:red')
pyplot.plot(sales_data, color='tab:blue')
pyplot.show()


