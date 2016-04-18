from PyQt4 import QtGui, QtCore
from .gen.ui_main_view import Ui_MainWindow

class MainView(QtGui.QMainWindow):

    def __init__(self, main_ctrl):
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        
        self.lineEdits = []
        self.comboBoxes = []
        self.fig_widget = None
        self.deg_rad = None
        self.statusbar = None

        self.build_ui()

        self.main_ctrl.main_view_init(lineEdits = self.lineEdits,
                                      comboBoxes = self.comboBoxes,
                                      fig_widget = self.fig_widget,
                                      deg_rad = self.deg_rad,
                                      statusbar = self.statusbar)

    def build_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.lineEdits = [self.ui.lineEdit_1,
                          self.ui.lineEdit_2,
                          self.ui.lineEdit_3]
        self.comboBoxes = [self.ui.comboBox_1,
                           self.ui.comboBox_2,
                           self.ui.comboBox_3]
        self.fig_widget = self.ui.widget_verticalLayout
        self.deg_rad = self.ui.comboBox_deg_rad
        self.statusbar = self.ui.statusbar
        
        # set Validators
        double_validator = QtGui.QDoubleValidator()
        for le in self.lineEdits:
            le.setValidator(double_validator)
        
        # connect signal to method 
        self.ui.pushButton_Calculate.clicked.connect(self.calculate)
        self.setEnterAction=QtGui.QAction("Set Enter", self, shortcut=QtCore.Qt.Key_Return, triggered=self.calculate)
        self.addAction(self.setEnterAction)
        self.setEnterAction=QtGui.QAction("Set Enter", self, shortcut=QtCore.Qt.Key_Enter, triggered=self.calculate)
        self.addAction(self.setEnterAction)
        
        for cb in self.comboBoxes:
            self.connect(cb,
                         QtCore.SIGNAL('activated(const QString&)'),
                         self.update_combo_boxes)
        
        self.connect(self.ui.comboBox_deg_rad,
                     QtCore.SIGNAL('activated(const QString&)'),
                     self.update_deg_rad)

    def update_deg_rad(self):
        self.main_ctrl.update_deg_rad()
        
    def calculate(self):
        self.main_ctrl.calculate()

    def update_combo_boxes(self):
        self.main_ctrl.update_combo_boxes()
