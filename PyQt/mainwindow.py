from PyQt5 import QtCore,  QtWidgets,  uic
#from PyQt5.Qt import QtMsgType
 
qtCreatorFile = "mainwindow.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
textWindow = None
textBuffer = []

def myQtMsgHandler( msg_type, msg_log_context, msg_string ) :
    #print(msg_string)
    if(textWindow != None):
        textWindow.appendPlainText(msg_string)
    else:
        textBuffer.append(msg_string)

def emptyTextBuffer():
    if(textWindow != None):
        if(len(textBuffer) != 0):
            for x in textBuffer:
                textWindow.appendPlainText(x)
            textBuffer.clear()
 
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
        self.clear.clicked.connect(self.on_clearclicked)
        global textWindow
        textWindow = self.text
        emptyTextBuffer()
        
    def on_helloclicked(self):
        """ Doc string for MainWindow::on_helloclicked
    
        MainWindow::on_helloclicked documentation
        """ 
        #print(self._counter, ". Hello, World!")
        #no QString in PyQt5!?
        #str = QtCore.QString("%1. Hello, World!")#.arg(self.counter)
        str = f"{self._counter}. Hello, World!"
        QtCore.qDebug(str)
        self._counter += 1
        
    def on_action_Quittriggered(self):
        #print("Application is quitting...")
        QtCore.qDebug("Application is quitting...")
        self.hide()
        QtWidgets.qApp.quit()

    def on_clearclicked(self):
        self.text.clear()

