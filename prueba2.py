'''
Created on 24 nov. 2018

@author: saparicio
'''
import concurrent.futures

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 323, 1235)
        print(future.result())