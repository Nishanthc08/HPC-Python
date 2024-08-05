import multiprocessing
import os

def read_file(file_path):
    """Function to read and print file contents"""
    with open(file_path, 'r') as file:
        content = file.read()
    print(f'Contents of {file_path}:\n{content}')

if __name__ == '__main__':
    directory_path = r'D:\HPC\HPC\programs\filesReading'
    file_paths = [os.path.join(directory_path, f'file{i}.txt') for i in range(1, 4)]
    jobs = []
    for file_path in file_paths:
        p = multiprocessing.Process(target=read_file, args=(file_path,))
        jobs.append(p)
        p.start()
        p.join()