# This code will find all factors of the number given by the user
# excludes 1 and the number itself.
def factors(n):
    # Finds an integer 'x' inbetween 2 and n - 1, if n / x has a 0 remainder, adds to the list.
    factorList = [x for x in range(2, n - 1) if n % x == 0]
    return print(factorList)


if __name__ == '__main__':
    factors(int(input("Please enter integer: ")))
