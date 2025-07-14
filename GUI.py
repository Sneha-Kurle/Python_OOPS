import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,700,500)
        self.setWindowTitle('Its my first GUI')
        self.setWindowIcon(QIcon('sabha.jpeg'))

        label=QLabel('Hello..GM',self)
        label.setFont(QFont('Areal', 12))
        label.setGeometry(0,0,700,500)
        label.setStyleSheet('color:blue;'
                            'background-color:yellow;'
                            'font-weight:bold;'
                            'font-style:italic;'
                            'text-decoration:underline;')
        label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignBottom)
        label.setAlignment(Qt.AlignVCenter)
        label.setAlignment(Qt.AlignRight)
        label.setAlignment(Qt.AlignLeft)
        label.setAlignment(Qt.AlignHCenter)
        label.setAlignment(Qt.AlignCenter)
        

def main():
    app=QApplication(sys.argv)
    window=main_window()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()

