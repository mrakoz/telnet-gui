import sys
import traceback
try:
    import main
    app = main.QApplication(sys.argv)
    window = main.MainWindow()
    window.show()
    # Don't start exec loop, just initialize to see if it crashes
except Exception as e:
    with open('err.log', 'w') as f:
        traceback.print_exc(file=f)
