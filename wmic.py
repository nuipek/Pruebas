'''
Created on 7 dic. 2018

@author: saparicio
'''
import subprocess
import os

if __name__ == '__main__':
    x = subprocess.check_output('wmic csproduct get UUID')
    print(x)
    print(os.popen("wmic csproduct get UUID").read().split()[-1])
    
    #Linux    
    #import os
    #os.popen("hdparm -I /dev/sda | grep 'Serial Number'").read().split()[-1]

    #Windows:

    
    print(os.popen("wmic diskdrive get serialnumber").read().split()[-1])