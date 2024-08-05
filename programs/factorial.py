import multiprocessing

def factorial(n):
    """Function to calculate factorial of a number"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def worker(num):
    """Worker function to calculate and print factorial"""
    result = factorial(num)
    print(f'Factorial of {num}: {result}')

if __name__ == '__main__':
    numbers = [5, 7, 10, 12]
    jobs = []
    for num in numbers:
        p = multiprocessing.Process(target=worker, args=(num,))
        jobs.append(p)
        p.start()