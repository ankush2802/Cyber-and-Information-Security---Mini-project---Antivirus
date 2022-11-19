import time
import os

def rCheck():
    with open("real-time_switch.blink","r") as tc:
        x = tc.read()
        tc.close()

    if x == "1" or x == None:
        os.system('cmd /c "python real-time.py"')

while 1:
    try:
        rCheck()
    except:
        pass
    time.sleep(2)