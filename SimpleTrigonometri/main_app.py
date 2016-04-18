import sys
from PyQt4 import QtGui
from ctrls.MainController import MainController

class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_ctrl = MainController()

if __name__ == '__main__':
    app = App(sys.argv)
    returnCode = app.exec_()
    app.main_ctrl.announce_close()
    sys.exit(returnCode)
