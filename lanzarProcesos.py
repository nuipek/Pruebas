'''
Created on 4 feb. 2019

@author: saparicio
'''

import subprocess
import time 
import sys
from  PyQt5.QtCore import QProcess 
if __name__ == '__main__':
    process = QProcess()
    #process.setWorkingDirectory("D:/Qgis34/bin/")
    #process.setProgram()
    #process.setProgram("calc.exe")
    process.startDetached("D:/Qgis34/bin/qgis-bin-g7.exe")
    #process.waitForFinished(3000)
    print("HOLA")
    sys.exit()
    
    
    