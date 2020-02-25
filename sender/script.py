#!/usr/bin/env python
import os
import time

# Wait time in milliseconds
#time_interval = 15;

# Compiling the C Script
os.system('gcc -o app main.c')
os.system('/bin/bash -c "./app"')

#while True:
	#start_time = int(round(time.time() * 1000))
	#os.system('/bin/bash -c "./app"')
	#os.system('./app')
	#after_time = int(round(time.time() * 1000))
	#elapsed_time = after_time - start_time
	#sleep_time = time_interval - elapsed_time
	#time.sleep(float(sleep_time/1000.0))
	#time.sleep(0.005)
	#print(sleep_time)
