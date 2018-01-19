from functools import lru_cache


@lru_cache(maxsize=100000000)
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


@lru_cache(maxsize=100000000)
def primes(array):
    prime = []
    indexes = []
    for i in range(0, len(array)):
        if isPrime(array[i]):
            prime.append(array[i])
            indexes.append(array.index(array[i]))
    indexes = tuple(indexes)
    prime = tuple(prime)
    return (prime, indexes)


@lru_cache(maxsize=100000000)
def mersennes(n):
    pArray = []
    for i in range(0, n):
        pArray.append(i)
    pArray = tuple(pArray)
    primed = primes(pArray)
    primed = primed[0]
    primed = tuple(primed)
    # print(primed)
    possibleMersenne = []
    mersenneFor = []
    for i in range(0, len(primed)):
        mersenneFor.append('2^' + str(primed[i]) + ' - 1')
        possibleMersenne.append((2**primed[i]) - 1)
    possibleMersenne = tuple(possibleMersenne)
    mersenne = primes(possibleMersenne)
    corrFor = []
    for i in range(0, len(mersenne[1])):
        corrFor.append(mersenneFor[mersenne[1][i]])
    both = {}
    for i in range(0, len(corrFor)):
        both[corrFor[i]] = mersenne[0][i]
    return both


retrn = mersennes(100)
print(retrn)
