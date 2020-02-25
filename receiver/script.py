#!/usr/bin/env python
import os
import time

# Wait time in milliseconds
time_interval = 0.005

# Compiling the C script
os.system('gcc -o app main.c')

while True:
	start_time = int(round(time.time() * 1000))
	os.system('/bin/bash -c "./app <<< ' + str(start_time) + ' >> timings.txt"')
	time.sleep(time_interval)
