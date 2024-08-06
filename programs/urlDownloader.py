import threading 
import requests

def download_url(url):
    """Function to download content from a URL and print status."""
    response = requests.get(url)
    print(f'Downloaded {url} with status code {response.status_code}')

if __name__ == '__main__':
    urls = [
        'https://httpbin.org/get',
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/posts/2'
    ]
    
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_url, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
