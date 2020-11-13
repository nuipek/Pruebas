# import sys
# import time
#
# import numpy as np
#
# from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
# if is_pyqt5():
#     from matplotlib.backends.backend_qt5agg import (
#         FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
# else:
#     from matplotlib.backends.backend_qt4agg import (
#         FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
# from matplotlib.figure import Figure
#
#
# class ApplicationWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self._main = QtWidgets.QWidget()
#         self.setCentralWidget(self._main)
#         layout = QtWidgets.QVBoxLayout(self._main)
#
#         static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
#         layout.addWidget(static_canvas)
#         self.addToolBar(NavigationToolbar(static_canvas, self))
#
#         dynamic_canvas = FigureCanvas(Figure(figsize=(5, 3)))
#         layout.addWidget(dynamic_canvas)
#         self.addToolBar(QtCore.Qt.BottomToolBarArea,
#                         NavigationToolbar(dynamic_canvas, self))
#
#         self._static_ax = static_canvas.figure.subplots()
#         t = np.linspace(0, 10, 501)
#         self._static_ax.plot(t, np.tan(t), ".")
#
#         self._dynamic_ax = dynamic_canvas.figure.subplots()
#         self._timer = dynamic_canvas.new_timer(
#             100, [(self._update_canvas, (), {})])
#         self._timer.start()
#
#     def _update_canvas(self):
#         self._dynamic_ax.clear()
#         t = np.linspace(0, 10, 101)
#         # Shift the sinusoid as a function of time.
#         self._dynamic_ax.plot(t, np.sin(t + time.time()))
#         self._dynamic_ax.figure.canvas.draw()
#
#
# if __name__ == "__main__":
#     qapp = QtWidgets.QApplication(sys.argv)
#     app = ApplicationWindow()
#     app.show()
#     qapp.exec_()
#
#
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends. backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.setCentralWidget(sc)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()