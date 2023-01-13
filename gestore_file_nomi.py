import os

class gestore_file_nomi_ikea:

    def file_nomi_ikea(self):
        
        file_ikea = open('file_ikea.csv', 'r')

        file_ikea.readline()

        nomi = []

        nome_attuale = 'ciao'

        #nel file dell'ikea nella terza colonna ci sono i nomi 
        #dei vari mobili

        for line in file_ikea:
            riga = line.split(',')
            #questo è un piccolo controllo giusto per abbassare un po 
            #il numero dei duplicati
            if riga[2] != nome_attuale:
                if len(riga[2].split(' ')) == 1:
                    nomi.append(riga[2])
                    nome_attuale = riga[2]

        nomi_puliti = []

        for nome in nomi:
            if nome not in nomi_puliti: 
                nomi_puliti.append(nome)

        nomi_puliti.sort()

        file_nomi = open('file_nomi.csv', 'w')

        for nome in nomi_puliti:
            file_nomi.write(nome)
            file_nomi.write('\n')

        return nomi_puliti