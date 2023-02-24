#manually testing a new theory

original_permutation = []
permutation = []
#simulating a double move_left permutation twice(twice 2 once 1)
#[0, 1, 2, 3, 4]
sequence = [i for i in range (0,5)]
print(sequence)
original_permutation.append(sequence.copy())

#[2, 1, 0, 3, 4]
sequence = move_left(sequence, 0, 2)
print(sequence)
original_permutation.append(sequence.copy())

#[2, 1, 4, 3, 0]
sequence = move_left(sequence, 2, 2)
print(sequence)
original_permutation.append(sequence.copy())

#[0, 1, 4, 3, 2]
sequence = move_left(sequence, 4, 1)
print(sequence)
original_permutation.append(sequence.copy())

#[4, 1, 0, 3, 2]
sequence = move_left(sequence, 0, 2)
print(sequence)
original_permutation.append(sequence.copy())

#[4, 1, 2, 3, 0]
sequence = move_left(sequence, 2, 2)
print(sequence)
original_permutation.append(sequence.copy())

sequence = move_left(sequence, 4, 1)

print()

index = 0
step = 1
count = 1

#[0, 1, 2, 3, 4] QUESTA E' UNA CHIAVE VALIDA
key = original_permutation[0].copy()
key = move_left(key, 0, 1)
original_permutation = perm(key, original_permutation, 0, 1, 1, 5)

#[2, 1, 0, 3, 4] QUESTA E' UNA CHIAVE VALIDA
key=original_permutation[1].copy()
key = move_left(key, 2, 1)
original_permutation = perm(key, original_permutation, 1, 3, 1, 5)

#[2, 1, 4, 3, 0] QUESTA E' UNA CHIAVE VALIDA
key=original_permutation[2].copy()
key = move_left(key, 4, 1)
original_permutation = perm(key, original_permutation, 2, 0, 1, 5)

#[0, 1, 4, 3, 2]
key=original_permutation[3].copy()
key = move_left(key, 0, 1)
original_permutation = perm(key, original_permutation, 3, 1, 1, 5)

#[4, 1, 0, 3, 2] QUESTA E' UNA CHIAVE VALIDA
key=original_permutation[4].copy()
key = move_left(key, 2, 1)
original_permutation = perm(key, original_permutation, 4, 3, 1, 5)

#[4, 1, 2, 3, 0]
key=original_permutation[5].copy()
key = move_left(key, 4, 1)
original_permutation = perm(key, original_permutation, 5, 0, 1, 5)

#riusciti a trovare 4 su 6 delle chiavi, come trovo le due restanti?
#provassi ad invertire le cifre restanti?

#[2, 3, 0, 1, 4] QUESTA E' UNA CHIAVE VALIDA 
#[0, 4, 2, 3, 1]
key = [2, 3, 0, 1, 4]
original_permutation.insert(6, key.copy())
key = move_left(key, 2, 1)
original_permutation = perm(key, original_permutation, 6, 3, 1, 5)

#[1, 2, 0, 4, 3] QUESTA E' UNA CHIAVE VALIDA
key = [1, 2, 0, 4, 3]
original_permutation.insert(7, key.copy())
key = move_left(key, 2, 1)
original_permutation = perm(key, original_permutation, 7, 3, 1, 5)