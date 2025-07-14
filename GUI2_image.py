import sys
from PyQt5.QtWidgets import  QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap
class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,700,500)
        label=QLabel(self)
        label.setGeometry(0,0,700,500)
        pixmap=QPixmap('lord krishna full hd wallpaper 1080X1920.jpg')
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry(self.width()-label.width()//2,
                          self.height()-label.height()//2,
                          label.width(),
                          label.height())

def main():
    app=QApplication(sys.argv)
    window=main_window()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()