import mainwindow
from PyQt5 import QtWidgets
import sys

print("__name__ = ",  __name__)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()

