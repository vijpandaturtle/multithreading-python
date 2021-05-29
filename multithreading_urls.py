from pathlib import Path 
import urllib.request 
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_one(url):
    '''Download the specified URL and saves to disk'''
    req = urllib.request.urlopen(url)
    fullpath = Path(url)
    fname = fullpath.name 
    ext = fullpath.suffix

    if not ext:
        raise RuntimeError("URL does not contain an extension")

    with open(fname, "wb") as handle:
        while True:
            chunk = req.read(1024)
            if not chunk:
                break
            handle.write(chunk)
    
    msg = f"Finished Downloading {fname}"
    return msg

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