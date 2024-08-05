import multiprocessing

def sum_of_squares(start, end):
    """Function to calculate the sum of squares in a range"""
    total = sum(i * i for i in range(start, end + 1))
    print(f'Sum of squares from {start} to {end}: {total}')

if __name__ == '__main__':
    ranges = [(1, 10), (11, 20), (21, 30), (31, 40)]
    jobs = []
    for r in ranges:
        p = multiprocessing.Process(target=sum_of_squares, args=(r[0], r[1]))
        jobs.append(p)
        p.start()