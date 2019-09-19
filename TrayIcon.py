'''
Created on 23 feb. 2019

@author: saparicio
'''
import sys    
from PyQt5.QtWidgets import QStyleFactory, QApplication, QMainWindow,QPushButton,QSplashScreen, QMenu, QSystemTrayIcon,QDialog
from PyQt5 import QtCore,QtGui    
from PyQt5.QtGui import QIcon 
    
class App():
  def __init__(self):
    # Create a Qt application
    self.app = QApplication(sys.argv)
    
    icon = QIcon("icono-hoja.png")
    menu = QMenu()
    settingAction = menu.addAction("setting")
    settingAction.triggered.connect(self.setting)
    exitAction = menu.addAction("exit")
    exitAction.triggered.connect(sys.exit)
    
    self.tray = QSystemTrayIcon()
    self.tray.setIcon(icon)
    self.tray.setContextMenu(menu)
    self.tray.show()
    self.tray.setToolTip("unko!")
    self.tray.showMessage("hoge", "moge")
    self.tray.showMessage("fuga", "moge")
    
  def run(self):
    # Enter Qt application main loop
    self.app.exec_()
    sys.exit()

  def setting(self):
    self.dialog = QDialog()
    self.dialog.setWindowTitle("Setting Dialog")
    self.dialog.show()    
    
if __name__ == '__main__':
    app=App()
    app.run()