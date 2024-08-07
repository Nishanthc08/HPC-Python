from joblib import Parallel, delayed

def calculate_cube(n):
    """Function to calculate the cube of a number."""
    return n ** 3

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    results = Parallel(n_jobs=2)(delayed(calculate_cube)(n) for n in numbers)
    for number, result in zip(numbers, results):
        print(f'Cube of {number}: {result}')