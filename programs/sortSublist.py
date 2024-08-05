import multiprocessing

def sort_sublist(sublist):
    """Function to sort a sublist"""
    sorted_list = sorted(sublist)
    print(f'Sorted sublist: {sorted_list}')

if __name__ == '__main__':
    sublists = [[5, 3, 8, 1], [10, 7, 6, 2], [14, 13, 12, 11], [21, 19, 20, 18]]
    jobs = []
    for sublist in sublists:
        p = multiprocessing.Process(target=sort_sublist, args=(sublist,))
        jobs.append(p)
        p.start()