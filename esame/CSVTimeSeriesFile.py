class ExamException(Exception):
    pass

class CSVFile:
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise ExamException()
        self.name = name

    def get_data(self, start=None, end=None): 
        try:
            my_file = open(self.name, 'r')
        except:
            raise ExamException('File non apribile')
    
        data = []

        for row in my_file:
                elements = row.split(',')
                elements[-1] = elements[-1].strip()
                data.append(elements)
            
        if start == None and end == None:
            return data[1:]
        if start == 0:
            raise ExamException('Errore Logico-Matematico: Start value 0')

        #booleane di controllo
        negative = False
        start_None = False
        end_None = False

        #controllo sullo start
        try:
            if not start:
                start_None = True 
            else:
                int_start = int(start)
                if int_start < 0 :
                    raise ExamException('Start negativo')
        except:
            raise ExamException('Errore sullo start')
            
        #controllo sull'end    
        try:
            if not end:
                end_None = True
            else:
                int_end = int(end)
                if int_end < 0 :
                    raise ExamException('End negativo')
        except:
            raise ExamException('Errore sull''end')
            print('Errore di conversione')

        #controlli su start == None
        dim = len(data)
        if start_None:
            end = int(end)
            if end < dim:
                return data[1:end]
            raise ExamException('Errore: End maggiore di dim')

        #controllo su end == None
        if end_None:
            start = int(start)
            if start < dim:
                correct_data = []
                for item in data[start-1:]:  
                    correct_data.append(item)
                return correct_data
            raise ExamException('Errore: Start maggiore di dim')

        #Errori di outofbond
        start = int(start)
        end = int(end)
        if start > end:
            raise ExamException('Errore Logico-Matematico: Start maggiore di End')
        if start > dim or end > dim:
            raise ExamException("Errore Logico-Matematico: Start ed End / End out of bound")

        return data[start-1:end]

class TimeSeriesCSVFile(CSVFile):

    def get_data(self):
        data = super().get_data(None, None)
        sanitized_data = []
        for rows in data:
            try: 
                rows[0] = int(rows[0])
                rows[1] = float(rows[1])
                sanitized_row = []
                sanitized_row.append(rows[0])
                sanitized_row.append(rows[1])
                sanitized_data.append(sanitized_row)    
            except:
                pass #così mi rimuovo le righe che contengono cose brutte

        #gestisco i due possibili errori nel get data
        for i, rows in enumerate(sanitized_data):
            if i > 1:
                if sanitized_data[i-1][0] == rows[0]:
                    raise ExamException('Echop duplicato')
                if sanitized_data[i-1][0] > rows[0]:
                    raise ExamException('Echop fuoriposto')
                    
        return sanitized_data
