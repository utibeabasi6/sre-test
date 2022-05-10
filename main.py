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
    return False

def primes(num):
    has_seen = set()
    results = []
    for i in range(num):
        if is_prime(i):
            if i in has_seen:
                results.append(str(i) + "*")
            else:
                results.append(str(i))
        else:
            continue
    return results

print(primes(10))