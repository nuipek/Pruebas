'''
Created on 7 dic. 2018

@author: saparicio
'''

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


if __name__ == '__main__':
   
    key = get_random_bytes(32)
    data='Prueba'.encode(encoding='utf_8', errors='strict')
    
    print(key)
    cipher = AES.new(key, AES.MODE_EAX, mac_len=16)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    with open("encrypted.bin", "wb") as file_out:
        #file_out = open("encrypted.bin", "wb")
        [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    
        

    with open("encrypted.bin", "rb") as file_in:
        #file_in = open("encrypted.bin", "rb")
        nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    # let's assume that the key is somehow available again
        cipher = AES.new(key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        print((data).decode())