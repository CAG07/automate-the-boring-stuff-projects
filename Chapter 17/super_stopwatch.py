#! python3
# super_stopwatch.py - A simple stopwatch program.

#Track the amount of time elapsed between presses of the ENTER key, with each key press starting a new “lap” on the timer.
#Print the lap number, total time, and lap time

import time

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input()
print('Started.')
start_time = time.time() # get the first lap's start time
last_time = start_time
lap_num = 1

# Start tracking the lap times.

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #%s: %s (%s)' % (lap_num, total_time, lap_time), end='')
        lap_num += 1
        last_time = time.time() # reset the last lap time

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    
