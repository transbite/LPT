from PyQt5 import QtWidgets,  uic
 
qtCreatorFile = "mainwindow.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ Doc string for MainWindow
    
    MainWindow class documentation
   """ 
    
    def __init__(self,  parent = None):
        QtWidgets.QMainWindow.__init__(self,  parent)
        #Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self._counter = 0
        self.hello.clicked.connect(self.on_helloclicked)
        self.action_Quit.triggered.connect(self.on_action_Quittriggered)
        self.action_Hello.triggered.connect(self.on_helloclicked)
        
    def on_helloclicked(self):
        """ Doc string for MainWindow::on_helloclicked
    
        MainWindow::on_helloclicked documentation
        """ 
        print(self._counter, ". Hello, World!")
        #no QString in PyQt5!?
        #str = QtCore.QString("%1. Hello, World!")#.arg(self.counter)
        #QtCore.qDebug(str)
        self._counter += 1
        
    def on_action_Quittriggered(self):
        print("Application is quitting...")
        self.hide()
        QtWidgets.qApp.quit()

    
