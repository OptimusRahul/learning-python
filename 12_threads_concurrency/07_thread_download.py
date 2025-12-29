import threading
import requests
import time

def download_file(url):
    print(f"Started downloading file from {url}..")
    response = requests.get(url)
    print(f"Downloaded file from {url}, size: {len(response.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]


start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download_file, args=(url,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.time()
print(f"Time taken: {end - start:.2f} seconds")