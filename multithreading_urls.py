from pathlib import Path 
import urllib.request 
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_one(url):
    '''Download the specified URL and saves to disk'''
    req = urllib.request.urlopen(url)
    fullpath = Path(url)
    fname = fullpath.name 
    ext = fullpath.suffix

    futures_list = []
    results = []

    with ThreadPoolExecutor(max_workers=13) as executor:
        for url in urls:
            futures = executor.submit(download_one, url)
            futures_list.append(futures)

        for future in futures_list:
            try:
                result = future.result(timeout=60)
                results.append(result)
            except Exception:
                results.append(None)
    return results

@timeit
def download_all(urls):
    '''Create a threadpool and download specified urls'''
    with ThreadPoolExecutor(max_workers=13) as executor:
        return executor.map(download_one, urls, timeout=60)

if __name__=="main":
    urls = {
        'http://www.irs.gov/pub/irs-pdf/f1040.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040a.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040ez.pdf',
        'http://www.irs.gov/pub/irs-pdf/f1040es.pdf'
    }

    results = download_all(urls)
    for result in results:
        print(result)