class ModelError(Exception):
    pass
class Model():

    def fit(self, data):
        # fit non implementato nella classe madre
        raise NotImplementedError('Method not implemented yet')

    def predict(self, data):
        #predict non implementato nella classe madre
        raise NotImplementedError('Method not implemented yet')

class IncrementModel(Model):

    def predict(self, data):
        
        #primo errore possibile: DATA non è una lista
        if not isinstance(data, list):
            raise ModelError('Error: Data not stored into a list')

        #secondo errore possibile: DATA contiene o 0 o 1 dato
        if len(data) <= 1:
            raise ModelError('Error: Len of data too small (need at least 2 elements to calculate the variation')

        #ERRORI SUGLI ELEMENTI:
            #NON CONVERTIBILI A FLOAT
            #NUMERI NEGATIVI
    
        try:
            data[0] = float(data[0])
        except:
            raise ModelError('Error: Element not convertible into float')

        if data[0] < 0:
            raise ModelError('Error: Element with negative value (expected positive values')
        
        prev_item = data[0]
        sum = 0
        for item in data[1:]:
            try:
                item = float(item)
            except:
                raise ModelError('Error: Element not convertible into float')
            if item < 0:
                raise ModelError('Error: Element with negative value (excepted positive values')
            sum = sum + (item - prev_item)
            prev_item = item
            
        prev_value = data[-1] + (sum / (len(data) - 1))

        #se la variazione media è negativa e maggiore in valore assoluto 
        #dell'ultimo elemento (e dunque prevederebbe un valore negativo
        #che non possiamo avere)
        prev_value = 0 if prev_value < 0 else prev_value
        return prev_value

