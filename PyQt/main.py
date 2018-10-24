import mainwindow
from PyQt5 import QtWidgets
import sys

print("__name__ = ",  __name__)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    sys.exit(app.exec_())

