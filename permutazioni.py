import math
#function that moves a given element to the right by a given number of spaces (swaps position with the element in the target position)
def move_left(key, start, step):
    bound = len(key)
    end = (start+step)%bound
    key = swap(key, start, end)
    return key

def swap(key, a, b):
    t = key[a]
    key[a] = key[b]
    key[b] = t
    return key

def prime(n):
    for i in range (2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

#function that primes a given number
    
def primes(n):
    divisors = []
    i = 2
    while n > 1:
        if n%i == 0 :
            divisors.append(i)
            n = n/i
            i = 2
        else:
            i = i+1
    return divisors
    
#upper_bound of the test
upper_bound = 20

#list of the bounds that increase from 2 to a given upper_bound minus 1
bounds = [i for i in range (2, upper_bound)]

#gonna iterate over all the possible bound (from 2 to the upper_bound)
for bound in bounds:

    #we are calculating permutation cycles, so we give the first permutation the original_key name. in reality all permutations can be defined as keys due to the periodic nature of the cycle
    
    #the first permutation is simply the sequence of all numbers between zero and the given bound
    original_key = [i for i in range (0, bound)]
    
    key = [i for i in range (0, bound)]

    index = 0
    #gonna iterate over all the possible step of permutation (from 1 to the given bound)
    steps = [i for i in range(1, bound)]

    #gonna record the number of permutations obtainable from the cycle deriving from each possible step
    distribution = {}
    
    for step in steps:
        
        key = move_left(key, index, step)
        index = (index+step)%bound
        count = 1

        while(key != original_key):
            key = move_left(key, index, step)
            index = (index+step)%bound
            count = count + 1

        if count in distribution:
            distribution[count].append(step)
            
        else:
            distribution[count] = []
            distribution[count].append(step)

        #print("{} : {}".format(step, count))

    print("bound (primes): {} {}".format(bound, primes(bound)))

    print(" ↳distribution: ")
    for key, value in distribution.items():
        print("  ↳count (primes): {} {}".format(key, primes(key)))
        print("   ↳steps {}".format(value))
        
    
    print()