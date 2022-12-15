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

    def comp_avg_increment(self, data):
        #primo errore possibile: DATA non è una lista
        if not isinstance(data, list):
            raise TypeError('Error: Data not stored into a list')
            
        #secondo errore possibile: DATA contiene o 0 o 1 dato
        if len(data) <= 1:
            raise ModelError('Error: Len of data too small (need at least 2 elements to calculate the variation')

        #ERRORI SUGLI ELEMENTI:
            #NON CONVERTIBILI A FLOAT
    
        try:
            data[0] = float(data[0])
        except:
            raise TypeError('Error: Element not convertible into float')
        
        prev_item = data[0]
        sum = 0
        for item in data[1:]:
            try:
                item = float(item)
            except:
                raise ModelError('Error: Element not convertible into float')
            
            sum = sum + (item - prev_item)
            prev_item = item

        return  sum / (len(data) - 1)     

    def predict(self, data):
        #poiché è la funzione comp_avg_increment
        #che implementa i controlli sui dati
        #la eseguo per prima
        increment = self.comp_avg_increment(data)
        pred_value = data[-1] + increment

        return pred_value

class FitIncrementModel(IncrementModel):

    def fit(self, data):
        self.global_avg_increment = self.comp_avg_increment(data)
        
    def predict(self, data):
        #poiché è la funzione comp_avg_increment
        #che implementa i controlli sui dati
        #la eseguo per prima
        increment = self.comp_avg_increment(data)
        pred_value = data[-1] + (increment + self.global_avg_increment)/2

        return pred_value

#gli slicing avvengono all'esterno della funzione
#fit e predict sono i più generali possibili
