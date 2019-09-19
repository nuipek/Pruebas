'''
Created on 24 nov. 2018

@author: saparicio
'''

import concurrent.futures
import signal
import math
import time , sys
from builtins import enumerate
 
PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]
 
def is_prime(n,valor):
    time.sleep(0.5)
    print(valor)
    if n % 2 == 0:
        return n,False
 
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return n, False
    return n, True
 
def main():
    tiempo = time.time()    
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        #futures = executor.map(is_prime, PRIMES,[1,2,3,4,5,6,7,8,9,10,11,12])
        futures=[]
        
        while True:
            global some_flag
            print(some_flag)
            if not some_flag:
                executor.shutdown(wait=False)
                #sys.exit()
                break
            else:
                for index, prime in enumerate(PRIMES):
                    future = executor.submit(is_prime, prime,index)
                    futures.append(future)
                time.sleep(3.0)
                #some_flag = False
                for future in futures:
                    if not future.running():
                        future.cancel()
                    #print(future.result())
                #for future in concurrent.futures.as_completed(futures):
                #    print(future.result())   
                
        #futures.as_completed()
        
        """for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))"""
    tiempo2 = time.time()
    print(tiempo2-tiempo," Segundos")
    
def mainseq():
    tiempo = time.time()    
    futures = map(is_prime, PRIMES,[1,2,3,4,5,6,7,8,9,10,11,12])
    for future in futures:
        print(future)
    tiempo2 = time.time()
    print(tiempo2-tiempo," Segundos")
            
if __name__ == '__main__':
    some_flag = True
    main()
    #mainseq()
    
    

def handler(arg1, arg2):
    global some_flag
    print("Got interrupt")
    some_flag = False
    print("Shutdown")

signal.signal(signal.SIGTERM,handler)
signal.signal(signal.SIGINT,handler)    
    
"""    
    # We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
"""            