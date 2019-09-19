'''
Created on 24 dic. 2018

@author: saparicio
'''
import time,sys,random
from multiproceso import Process, Pipe
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread
import timeit

def tick():
    print ('tick')
    

def hello(n):
    #time.sleep(random.randint(1,300))
    l = 0
    while (l<10000000):
        l+=1
    with open("fichero_"+n,"w") as file:
        file.write(str(l))    
  
    
class Prueba():
    def __init__(self,n,remote_pipe):
        self.n = n
        self.pipe = remote_pipe
        self.run()
        
    def run(self):
        l = 0
        while (l<10000000):
            l+=1
        with open("fichero_"+self.n,"w") as file:
            file.write(str(self.n))    
  
        

class ClockThread(QThread):
    """ Interface Clock for worker thread """



    def __init__(self):

        QThread.__init__(self)
        try:
            self.timeStart = None
            self.timer = None
            self.pìpe  = None
        except Exception as e:
            print(str(e))

    def run(self):
        
        try:
            self.pipe, remote_pipe = Pipe()
            timeStart = time.time()
            processes = []
            for i in range(16):
                #hello(str(i))
                #t = Process(target=hello, args=(str(i),))
                t = Process(target=Prueba, args=(str(i),remote_pipe,))
                processes.append(t)
                t.start()
  
            for one_process in processes:
                one_process.join()
   
                #print("Done!")

            timeEnd = time.time()
            print(str(timeEnd-timeStart))
#             self.timer = QtCore.QTimer()
#             self.timeStart = time.time()
#             time.sleep(1)
#             self.timer.timeout.connect(self.timeClock)
#             self.timer.setInterval(1)
#             self.timer.start()
#             
#             self.exec_()
        except Exception:
            pass
            

        
    def timeClock(self):
        try:
            value = int(time.time() - self.timeStart)
            print("value",str(value))  
            
#             with open("value","a")as file:
#                 file.write(str(value)) 
#              
        except Exception as e:
                print (str(e))









if __name__ == '__main__':
    print(QThread.idealThreadCount())
    app = QApplication(sys.argv)
    
    clockThread = ClockThread()
    clockThread.start()
    print(clockThread.isRunning())
    #clockThread.exit()
    
    app.exec_()
 
    
  
    
#     