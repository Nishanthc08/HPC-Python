from concurrent.futures import ThreadPoolExecutor

def calculate_square(n):
    """Function to calculate the square of a number"""
    return n ** n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with ThreadPoolExecutor(max_workers=5) as executer:
        results = executer.map(calculate_square, numbers)
    for number, result in zip(numbers, results):
        print(f'Square of {number}: {result}')