import sys
import traceback

def my_hook(type, value, tb):
    traceback.print_exception(type, value, tb)
    print("FATAL EXCEPTION!")

sys.excepthook = my_hook

from PyQt5.QtWidgets import QApplication
from main import MainWindow

app = QApplication(sys.argv)
w = MainWindow()
w.show()
print("isVisible:", w.isVisible())
app.exec_()
print("app.exec_() returned!")
