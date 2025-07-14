import sys
from PyQt5.QtWidgets import  QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,700,500)
        self.initUI()
    def initUI(self):
        new_widget=QWidget()
        self.setCentralWidget(new_widget)
        label1=QLabel('#1', self)
        label2=QLabel('#2', self)
        label3=QLabel('#3', self)
        label4=QLabel('#4', self)
        label5=QLabel('#5', self)

        label1.setStyleSheet('background-color:Blue;')
        label2.setStyleSheet('background-color:yellow;')
        label3.setStyleSheet('background-color:red;')
        label4.setStyleSheet('background-color:black;')
        label5.setStyleSheet('background-color:green;')
        
        verti=QVBoxLayout()
        verti.addWidget(label1)
        verti.addWidget(label2)
        verti.addWidget(label3)
        verti.addWidget(label4)
        verti.addWidget(label5)
        new_widget.setLayout(verti)
     

def main():
    app=QApplication(sys.argv)
    window=main_window()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()