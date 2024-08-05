import multiprocessing

def is_prime(n):
    """Function to check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def worker(num):
    """Worker function to check if a number is prime"""
    result = is_prime(num)
    status = "is prime" if result else "is not prime"
    print(f'{num} {status}')

if __name__ == '__main__':
    numbers = [17, 23, 42, 56, 79]
    jobs = []
    for num in numbers:
        p = multiprocessing.Process(target=worker, args=(num,))
        jobs.append(p)
        p.start()