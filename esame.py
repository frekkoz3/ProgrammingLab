class ExamException(Exception): 
    pass

class Average():

    def sanitize(self, data):
        #verifico che la lista sia una lista
        if not isinstance(data, list):
            raise ExamException('Dati non contenuti in una lista')

        #controllo che i miei dati siano numeri 
        for i in data:
            try:
                int(i)
            except:
                raise ExamException('Dati non numerici')
        
    def compute(self, data):
        somma = sum(data)
        return somma / len(data)

class MovingAverage(Average):

    def __init__(self, window):
        #verifico che window sia di tipo intero
        if not isinstance(window, int):
            raise ExamException('Window non è di tipo intero')

        #verifico che la finestra abbia dimensione positiva
        if window <= 0:
            raise ExamException('Dimensione della finestra uguale o minore di zero')
        
        self.window = window

    def sanitize(self, data):
        super().sanitize(data)

        #verifico che la finestra abbia dimensione minore della lista
        if self.window > len(data):
            raise ExamException('Dimensione della finestra troppo lunga')

        
                
    def compute(self, data):
        #in primis sanitizzo l'input
        #se qua mi alza errori ho concluso
        self.sanitize(data)

        dim_data = len (data)
        mov_average = []

        for i in range (0, dim_data - self.window + 1):
            mov_average.append(super().compute(data[i:i+self.window]))

        return mov_average

