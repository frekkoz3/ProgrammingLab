import tkinter as tk
from gestore_file_nomi import gestore_file_nomi_ikea
from random import randrange
import pyglet

class GUI:
    
    def play(self):
        self.createwindow()
        
    def createwindow(self):

        my_gestore = gestore_file_nomi_ikea()
        lista_nomi = my_gestore.file_nomi_ikea()

        #linea di codice per aggiungere un font
        pyglet.font.add_file('Livingst.ttf')
        pyglet.font.add_file('Cardinal.ttf')

        #WINDOW
        window = tk.Tk()
        window.columnconfigure(0, minsize=250)
        window.rowconfigure([0, 1], minsize=200)

        #FRAME A
        frame_a = myFrame.quickframe(self, window, 'black')
        #LABEL NOME
        lb = myLabel.quicklabel(self, frame_a, 'CHE NOME HAI?', '#FFFF00', 'black', 25, 10)
        frame_a.columnconfigure(0, minsize=500)
        frame_a.rowconfigure([0], minsize=400)
        lb.grid(row=0, column=0, sticky='nsew')
        frame_a.grid(row=0, column=0, sticky='nsew')

        #FRAME B
        frame_b = myFrame.quickframe(self, window, 'black' )
        #BOTTONE GENERA
        bt = myButton.quickbutton(self, frame_b, 'genera', 10, 5, '#FFFF00', 'black')
        
        def handle_click(event):
            lb['text'] = randomName.quickname(self, lista_nomi)
            
        bt.bind("<Button-1>", handle_click)
        frame_b.columnconfigure(0, minsize=500)
        frame_b.rowconfigure([0], minsize=400)
        bt.grid(row=0, column=0)
        frame_b.grid(row=1, column=0, sticky='nsew')
        
        window.mainloop()

    

#le classi my e le istanze quick richiedono che siano inserite tutte le variabili richieste
        
class myLabel:
    def quicklabel(self, masterP, text=None, foreground='white', background='black', width=10, height=10):
        return tk.Label(master=masterP, text='{}'.format(text), foreground='{}'.format(foreground), background='{}'.format(background), width='{}'.format(width), height='{}'.format(height), font=('Livingstone',25))

class myButton:
    def quickbutton(self, masterP, text='Click me', width=8, height=3, foreground='red', background='white', font=('Cardinal',12)):
        return tk.Button(master=masterP, text='{}'.format(text), fg='{}'.format(foreground), bg='{}'.format(background), width='{}'.format(width), height='{}'.format(height))

class myFrame:
    def quickframe(self, masterP, background='white', width=30, height=10):
        return tk.Frame(master=masterP,  bg='{}'.format(background), width='{}'.format(width), height='{}'.format(height))


#questa classe data una lista di nomi restituisce un nome casuale 
#con prima lettera MAIUSCOLA e tutto resto minuscolo
        
class randomName:

    def quickname(self, lista_nomi):
        n = randrange(0, len(lista_nomi)+1)
        return lista_nomi[n].title()

my_gui = GUI()
my_gui.play()