from typing import Any

from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, Qt, QVariant, qDebug, QTime, QTimer, QObject, QMetaObject, \
    pyqtSignal
from PyQt5.QtGui import QFont, QBrush, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QTableView, QItemDelegate

from qgis.PyQt import QtWidgets


def qt_message_handler(mode, context, message):
    if mode == QtCore.QtInfoMsg:
        mode = 'INFO'
    elif mode == QtCore.QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCore.QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtCore.QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))


class MyDelegate(QItemDelegate):

    def setEditorData(self,editor,index):
        editor.setAutoFillBackground(True)
        editor.setText(index.data())

class PruebaQStandardModel(QStandardItemModel):


class TablaModel(QAbstractTableModel):
    editCompleted = pyqtSignal(str, name='editCompleted')

    def __init__(self, parent=None):
        super().__init__(parent)

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timerHit)
        self.timer.start()
        self.datatable = None
    #     self.item_model = QStandardItemModel()
    #
    #     for (int row = 0; row < model.rowCount(); ++row) {
    #     for (int column = 0; column < model.columnCount(); ++column) {
    #     QStandardItem * item = new QStandardItem(QString("row %0, column %1").arg(row).arg(column));
    #     model.setItem(row, column, item);
    #     }
    #     }
    # def setItem(self, row, column, data):
    #     setItem(row_position, 6, comments_text)

    def timerHit(self):
        try:
            topLeft: QModelIndex = self.createIndex(0,0)
            # emit a signal to make the view reread identified data
            self.dataChanged.emit(topLeft, topLeft, {Qt.DisplayRole})
        except Exception as e:
            print(repr(e))

    def rowCount(self, parent_model: QModelIndex = QModelIndex()):
        return len(self.datatable)

    def columnCount(self, parent_model: QModelIndex = QModelIndex()):
        return len(self.datatable[0])

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
         if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section == 0:
                return "first"
            elif section == 1:
                return "second"
            elif section == 2:
                return "third"
         return QVariant()

    def flags(self, index: QModelIndex):
        try:
            # value = self.flags(index)
            # print(index.row(), index.column())
            model_index = self.index(index.row(), index.column(), index)
            return Qt.ItemIsEditable | QAbstractTableModel.flags(self, index)
        except Exception as e:
            print(repr(e))

    def setData(self, index: QModelIndex, value: Any, role: int = Qt.DisplayRole):
        if not self.checkIndex(index):
            return False
        if role == Qt.EditRole:
            self.editCompleted.emit(value)
            lista = self.datatable[index.row()]
            lista[index.column()] = value
        # if (!checkIndex(index))
        #     return false;
        # //save value from editor to member m_gridData
        # m_gridData[index.row()][index.column()] = value.toString();
        # //for presentation purposes only: build and emit a joined string
        # QString result;
        # for (int row = 0; row < ROWS; row++) {
        #     for (int col= 0; col < COLS; col++)
        #         result += m_gridData[row][col] + ' ';
        # }
        #
        return True

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        row: int = index.row()
        column: int = index.column()

        if role == Qt.DisplayRole:
            lista = self.datatable[row]
            return lista[column]
        else:
            return QVariant()

        # qDebug("row:{} column:{} role:{}".format(row, column, role))

        # if role == Qt.DisplayRole:
        #     if row == 0 and column == 0:
        #         # return "row:{0} column:{1}".format(index.row()+1, index.column()+1)
        #         return QTime.currentTime().toString()
        # elif role == Qt.FontRole:
        #     if row == 0 and column == 0:
        #         boldFont: QFont = QFont()
        #         boldFont.setBold(True)
        #         return boldFont
        # elif role == Qt.BackgroundRole:
        #     if row == 1 and column == 2:  # change background only for cell(1,2)
        #         return QBrush(Qt.red)
        # elif role == Qt.TextAlignmentRole:
        #     if row == 1 and column == 1:  # change background only for cell(1,2)
        #         return Qt.AlignRight + Qt.AlignVCenter
        # elif role == Qt.CheckStateRole:
        #     if row == 1 and column == 0:  # add a checkbox to cell(1, 0)
        #         return Qt.Checked
        # else:
        #     return QVariant()


class Tabla(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        misdatos = [['a','b','c'],['1','2','3']]
        self.tableview = QTableView()
        self.mi_modelo = TablaModel()
        self.mi_delegate = MyDelegate()
        self.mi_modelo.datatable = misdatos
        #self.tableview.setModel(self.mi_modelo)
        standardmodel = PruebaQStandardItemModel(2,2)
        standardmodel.setHorizontalHeaderItem(0, QStandardItem("Time"))
        standardmodel.insertRow(0,[QStandardItem("Time"), QStandardItem("Date")])
        self.tableview.setModel(standardmodel)
        self.tableview.setItemDelegate(self.mi_delegate)

        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.tableview)

        self.setWindowTitle('Model/View ')
        self.setGeometry(300, 300, 280, 150)


if __name__ == '__main__':
    import sys

    QtCore.qInstallMessageHandler(qt_message_handler)
    app = QApplication(sys.argv)
    tabla = Tabla()
    tabla.show()
    sys.exit(app.exec_())