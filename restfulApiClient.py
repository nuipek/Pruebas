'''
Created on 14 nov. 2018

@author: saparicio
'''

import requests


if __name__ == '__main__':
    r = requests.get('http://127.0.0.1:5000/file')
    
    file = open("resp_content.py", "wb")
    file.write(r.content)
    file.close()
    print(r.content)