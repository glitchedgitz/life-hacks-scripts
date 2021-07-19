import time
import msvcrt as m
import webbrowser as w
import sys, time

def sp():
    time.sleep(timeout)

def runit(func):
    for url in lines:
        url = url.strip()
        if url != "":
            print(url)
            w.open(url)
            func()

timeout = 0

lines = []
for line in sys.stdin:
    lines.append(line)

if len(sys.argv) > 1:
    timeout = int(sys.argv[1])

if timeout == 0:
    runit(m.getch)
else:
    runit(sp)



        
    
