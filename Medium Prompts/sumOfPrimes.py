lBound = 10
uBound = 20

def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

nums = [i for i in range(lBound, uBound + 1) if isPrime(i)]
print(sum(nums))
