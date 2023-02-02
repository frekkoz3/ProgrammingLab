
h1 = open('output.txt', 'r')
h2 = open('output1.txt', 'r')

for row in h1:
    t = h2.readline()
    if row != t:
        raise Exception('Errore: {} diverso da {}'.format(row, t))

print('all ok')