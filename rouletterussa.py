from playsound import playsound
from random import randrange
import time

#ROULETTE RUSSA DA SVILUPPARE FIGA

#IDEA BANALE DI BASE

#SCEGLI UN NUMERO TRA 1 E 6

#I NUMERI SCALANO

#SE NON C'E' IL PROIETTILE VIENE UN SUONO

#SE C'E' UN ALTRO

print("HELLO, DO U WANNA PLAY WITH ME? Y/N: ")

c = input()

time.sleep(2.5)

print("WEEL I DON'T GIVE A FUCK ABOUT UR OPINION ")

time.sleep(1.8)

print("NOW WE WILL DO SOME GREAT RUSSIAN ROULETTE")

time.sleep(1.8)

print("CHOOSE A NUMBER BEETWEEN 1 AND 6: ")

n = input()

r = randrange(1, 7)

print("LET'S START")

time.sleep(1.5)

for i in range (1, r):

    print("SEEMS LIKE UR LUCKY, FOR NOW")
    time.sleep(1.5)

playsound('RevolverSoundEffect.mp3',True)

if n == r:
    print("UR DEAD HAHAHAHA")
    playsound("LaughEffect.mp3",True)

else:
    print("I'M SO SAD :(")