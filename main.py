
def is_prime(num):
    # Function to check if a number is prime or not

    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, number is not prime
                return False
        else:
            return True
    # if number is less than 1, return False
    return False


def primes(num):
    global has_seen
    results = []
    for i in range(num):
        if is_prime(i):
            if i in has_seen:
                results.append(str(i) + "*")
            else:
                has_seen.add(i)
                results.append(str(i))
        else:
            continue
    for i in results:
        print(i, end=" ")
    print()


has_seen = set()


if __name__ == "__main__":
    # call script up to 10
    primes(10)

    # call script up to 20
    primes(20)
