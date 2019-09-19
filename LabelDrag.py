import json

import jsonpickle
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt, QMimeData, QByteArray
from PyQt5.QtGui import QDrag, QPixmap
import sys

jsonpickle.set_encoder_options('json', sort_keys=True, indent=1)

class LabelDrag(QLabel):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def mouseMoveEvent(self, e):
        try:
            if e.buttons() != Qt.LeftButton:
                return
            print("aqui")

            dicionario = {"text": "Hola"}
            new: str = jsonpickle.encode(dicionario, keys=True)

            mimeData = QMimeData()
            # mimeData.setText(new)
            mimeData.setData('datos', QByteArray(new.encode('UTF-8')))

            drag = QDrag(self)
            drag.setDragCursor(QPixmap('apply_all_32.png'), Qt.MoveAction)
            drag.setMimeData(mimeData)
            print(mimeData.text())
            dropAction = drag.exec_(Qt.MoveAction)
            self.setAcceptDrops(True)
        except Exception as e:
            print(str(e))

    def mousePressEvent(self, e):
        self.setAcceptDrops(False)
        super().mousePressEvent(e)


        if e.button() == Qt.LeftButton:
            print('press')

    def dragEnterEvent(self, e):
        try:
            mimedata: QMimeData = e.mimeData()
            if mimedata.hasFormat('datos'):
                e.accept()
            else:
                e.ignore()
        except Exception as e:
            print(str(e))

    def dropEvent(self, e):
        position = e.pos()
        mimedata: QMimeData = e.mimeData()
        data = mimedata.data('datos')
        new = data.data()
        valor = new.decode('UTF-8')
        datos = jsonpickle.decode(valor)
        print(datos)

        self.setText(str(datos))

        e.setDropAction(Qt.MoveAction)
        e.accept()

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.label1 = LabelDrag('Button1', self)
        self.label2 = LabelDrag('Button2', self)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.label1)
        lay.addWidget(self.label2)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()