from array_queue import ArrayQueue


def sieve(value):
    # initializes ArrayQueue with the name 'PrimeQueue'
    PrimeQueue = ArrayQueue()

    # Starts lists, one will hold all the prime numbers, the other will be a temp list to see if
    primeList = []
    tempList = []

    # Loads queue with all the values given in function parameter
    for i in range(2, value + 1):
        PrimeQueue.enqueue(i)

    # While PrimeQueue is not empty, loads 'tempList' with factors of a given value, meaning they cant be prime.
    # Checks if tempList is empty if it is then it is a prime and added to list, else it is removed entirely
    while not PrimeQueue.is_empty():
        tempList = [x for x in range (2, PrimeQueue.first() - 1) if PrimeQueue.first() % x == 0]
        if not tempList:
            primeList.append(PrimeQueue.dequeue())
        else:
            PrimeQueue.dequeue()
    # Resets tempList
        tempList = []

    # Returns primeList
    return primeList

