#!/bin/python

import requests

print('Download test')

url = 'http://speed.hetzner.de/10GB.bin'
r   = requests.get(url, stream=True)

for line in r.iter_lines():
    if r.status_code == 200:
        if line:
            del(line)
        
        
