#!/bin/python
import os
import subprocess
import requests

#url   = 'http://speed.hetzner.de/10GB.bin'
url   = 'https://eff.org'
pid   = os.getpid()


print('Download test with PID: ', pid)

r   = requests.get(url, stream=True)

for line in r.iter_lines():
    if r.status_code == 200:
        if line:
            del(line)
            
            #Perform 'ss -pti | grep -A 1 pid' request
            ss = subprocess.Popen(["ss", "-pti"], stdout=subprocess.PIPE)
            cp = subprocess.run(["grep", "-A 1", str(pid)], stdin=ss.stdout, capture_output=True)
            print(cp.stdout)
        
