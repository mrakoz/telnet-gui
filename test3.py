import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
w = QMainWindow()
w.show()
print("Visible?", w.isVisible())
ret = app.exec_()
print("Exec returned", ret)
