import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter


sys.excepthook = lambda *a: sys.__excepthook__(*a)

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.initUi()

    def initUi(self):
        self.drawCycle = False
        self.drawBtn.clicked.connect(self.draw)

    def draw(self):
        self.drawCycle = True
        self.repaint()

    def paintEvent(self, event):
        if self.drawCycle:
            qp = QPainter(self)
            qp.setPen(QColor("yellow"))
            qp.setBrush(QColor("yellow")) # Рисую круги, т.к жёлтую окружность невозможно рассмотреть на белом экране

            r = random.randint(10, 100)
            x = random.randint(r, abs(self.drawLbl.rect().width() - r))
            y = random.randint(r, abs(self.drawLbl.rect().height() - r))
            qp.drawEllipse(x, y, r, r)

            qp.end()
            self.drawCycle = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWidget()
    win.show()
    sys.exit(app.exec_())