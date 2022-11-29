class CSVFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            my_file = open(self.name, 'r')
            data = []
            for row in my_file:
                elements = row.split(',')
                elements[-1].strip()
                data.append(elements)
            return data[1:] #tolgo già l'intestazione
        except :
            print("Errore")
        return False

class NumericalCSVFile(CSVFile):
    
    def get_data(self):
        data_str = super().get_data()
        data_num = []
        print("ciao!!!")
        for row_str in data_str:
            row_num = []
            for i, data in enumerate(row_str):
                if i==0:
                    row_num.append(data)
                else:
                    try:
                        row_num.append(float(data))
                    except:
                        print('Errore di conversione')
                        break;

            #con questo non inserisco le righe corrotte
                        
            if(len(row_num) == len(row_str)):         
                data_num.append(row_num)
                              
        return data_num