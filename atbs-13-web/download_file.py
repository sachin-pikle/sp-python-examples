# Here’s the process for downloading and saving a file:
# 1. Call requests.get() to download the file.
# 2. Call open() with 'wb' to create a new file in write binary mode.
# 3. Loop over the Response object’s iter_content() method.
# 4. Call write() on each iteration to write the content to the file.

import requests

r = requests.get('https://automatetheboringstuff.com/files/rj.txt') ## 200 success

try:
    r.raise_for_status()
    print(len(r.text))

    with open ('RomeoAndJuliet.txt', 'wb') as out_file:
        for chunk in r.iter_content(1000000):
            out_file.write(chunk)
except Exception as exc:
    print(f'There was a problem in downloading: ', exc)
