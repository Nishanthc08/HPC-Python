import multiprocessing

def sum_numbers(numbers):
    """Function to sum numbers"""
    result = sum(numbers)
    print(f'Sum: {result}')

if __name__ == '__main__':
    numbers_list = [range(10), range(10, 20), range(20, 30), range(30, 40), range(40, 50)]
    jobs = []
    for numbers in numbers_list:
        p = multiprocessing.Process(target=sum_numbers, args=(numbers,))
        jobs.append(p)
        p.start()
        