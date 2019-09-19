'''
Created on 14 nov. 2018

@author: saparicio
'''


import random

ALPHABET = 'abcdefghijklmnpqrstuvwxyz1234567890'
CHUNK_SIZE = 5
NUMBER_CHUNKS=6

SCORE_MIN=1500
SCORE_MAX=3000

class Key:

    def __init__(self):
        self.check_digit_count = random.randint(2,6)
        self.key=""
        

    def verify(self, key):
        score = 0
        check_digit = key[0]
        check_digit_count = 0
        chunks = key.split('-')
        for chunk in chunks:
            for char in chunk:
                if char == check_digit:
                    check_digit_count += 1
                score += ord(char)
        if  self.check_digit_count  == check_digit_count and score > SCORE_MIN and score < SCORE_MAX:
            return True
        else:
            return False

    def generate(self):
        while True:
            key =  '-'.join(''.join(random.choice(ALPHABET) for _ in range(CHUNK_SIZE)) for _ in range(NUMBER_CHUNKS))
            #key = key[:-1]
            if self.verify(key):
                self.key = key.upper()
                return self.key
            else:
                key = ''

    def __str__(self):
        valid = 'Invalid'
        if self.verify():
            valid = 'Valid'
        return self.key.upper() + ':' + valid

if __name__ == '__main__':
    key = Key()
    code = key.generate()
    
    clave = str(code)
    
    print("key", clave)
    