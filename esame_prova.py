class ExamException(Exception): 
    pass

class Diff():

    def __init__(self, ratio=1):
        try:
            int(ratio)
        except:
            raise ExamException('Ratio non numero')

        if ratio<=0:
            raise ExamException('Ratio negativo')
        self.ratio = ratio

    def sanitize(self, data):
        #verifico che la lista sia una lista
        if not isinstance(data, list):
            raise ExamException('Dati non contenuti in una lista')

        if len(data) <= 1:
            raise ExamException('Dimensione lista troppo piccola')
            
        #controllo che i miei dati siano numeri 
        for i in data:
            try:
                int(i)
            except:
                raise ExamException('Dati non numerici')

    def compute(self, data):
        dif = []
        self.sanitize(data)
        for i in range (1, len(data)):
            dif.append((data[i]-data[i-1])/self.ratio)
        return dif


        