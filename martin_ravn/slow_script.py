import time

seconds_to_sleep = 200

for i in range(int(seconds_to_sleep)):
    time.sleep(1)
    print("Slept for "+str(i+1)+" seconds")