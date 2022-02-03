"""
Produces load on all available CPU cores.
Requires system environment var STRESS_MINS to be set.
"""
from multiprocessing import Pool
from multiprocessing import cpu_count
import time
import os

STR_MIN = 10

def load_time():
    global STR_MIN
    if len(sys.argv) > 1:
        set_time=sys.argv[1] 
        #STR_MIN = set_time
    else:
        try:
            set_time = os.environ['STRESS_MINS']
        except KeyError: 
            print('STRESS_MINS: Environment variable does not exist')
            set_time = STR_MIN       
    STR_MIN = set_time 
    print('SET Environment variable  as STRESS_MINS = ', STR_MIN)

def f(x):
    print('STRESS processor : ', x)
    timeout = time.time() + 60*float(STR_MIN)  # X minutes from now
    while True:
        if time.time() > timeout:
            break
        x*x

if __name__ == '__main__':
    load_time()
    processes = cpu_count()
    print ('utilizing %d cores\n' % processes)
    pool = Pool(processes)
    try:
        pool.map(f, range(processes))
    except KeyboardInterrupt: 
        print("KeyboardInterrupt")
