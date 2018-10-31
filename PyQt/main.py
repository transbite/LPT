import mainwindow
from PyQt5 import QtCore,  QtWidgets
import sys

QtCore.qInstallMessageHandler(mainwindow.myQtMsgHandler)

str = f"\n__name__ = {__name__}"
#print(str)
QtCore.qDebug(str)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()

