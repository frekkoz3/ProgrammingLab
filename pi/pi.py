import math
#questo algoritmo calcola con molta velocità le cifre in maniera corretta del pi_greco, però occupa troppa memoria

def brent_salamin_algorithm(precision):

    a=1
    b=1/math.sqrt(2)
    t=0.25
    p = 1

    for s in range(0, precision):
        
        x = (a+b)/2
        y = math.sqrt(a*b)
        t = t - p*(a-x)*(a-x)
        
        a = x
        b = y
        p = 2*p


    return ((a+b)*(a+b))/(4*t)

print (brent_salamin_algorithm(3))
