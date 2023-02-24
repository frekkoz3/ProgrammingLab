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


def permutation(sequence):
    if len(sequence) <= 3:
        keys = []
        copy_sequence = sequence.copy()
        keys.append(copy_sequence.copy())
        bound = len(sequence)
        index = 0 
        step = 1
        copy_sequence = move_left(copy_sequence, index, step)
        index = (index + step)%bound
        while copy_sequence != sequence:
            keys.append(copy_sequence.copy())
            copy_sequence = move_left(copy_sequence, index, step)
            index = (index + step)%bound
        return keys
    else:
        lower_keys = permutation(sequence[2::])
        keys = []
        for key in lower_keys:
            original_sequence = sequence[0:2] + key
            copy_sequence = original_sequence.copy()
            keys.append(copy_sequence.copy())
            bound = len(original_sequence)
            index = 0
            step = 1
            copy_sequence = move_left(copy_sequence, index, step)
            index = (index + step)%bound            
            while copy_sequence != original_sequence:
                keys.append(copy_sequence.copy())
                copy_sequence = move_left(copy_sequence, index, step)
                index = (index + step)%bound
        return keys     

#this is the sequence whose permutations you want to find
        
sequence = [0, 1, 2, 3, 4, 5, 6]
keys = permutation(sequence)

for key in keys:
    print(key)

