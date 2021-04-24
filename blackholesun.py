#!/bin/python
import os
import sys
import subprocess
import requests
import threading

url        = 'http://speed.hetzner.de/10GB.bin'
#url        = 'https://eff.org'
pid        = os.getpid()
stopped    = False
period     = 0.4
print_info = True if len(sys.argv) > 1 and str(sys.argv[1]) == "info" else False

#Perform 'ss -pti | grep -A 1 pid' request each period of time
def infos():
    subprocess.run(["clear"])
    ss = subprocess.Popen(["ss", "-pti"], stdout=subprocess.PIPE)
    cp = subprocess.run(["grep", "-A 1", str(pid)], stdin=ss.stdout, capture_output=True)
    print(cp.stdout)
    if not stopped:
        threading.Timer(period, infos).start()

print('Download test with PID: ', pid)

r = requests.get(url, stream=True)

if print_info:
    infos()

for line in r.iter_lines():
    if r.status_code == 200:
        if line:
            del(line)
            
stopped = True
        
