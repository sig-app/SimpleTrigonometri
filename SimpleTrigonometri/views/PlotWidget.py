##import sys
##import random
##from numpy import arange, sin, pi

from PyQt4 import QtGui, QtCore

##import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
##from matplotlib.path import Path
##import matplotlib.patches as patches

class MplFigureCanvas(FigureCanvas):
    def __init__(self, main_ctrl, parent=None, width=None, height=None, dpi=None):
        self.main_ctrl = main_ctrl
        
        if width and height and dpi:
            self.fig = Figure(figsize=(width, height), dpi=dpi)
        elif width and height:
            self.fig = Figure(figsize=(width, height))
        elif dpi:
            self.fig = Figure(dpi=dpi)
        else:
            self.fig = Figure()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.animation)
        self.animation_is_running = False
        self.animation_func = None
        self.animation_list_of_args = []
        self.animation_frame_length = 0
        self.animation_frame_number = 0

    def plot(self, func, *args):
        func(self.fig, *args)
        self.draw()

    def start_animation(self, func, list_of_args, interval):
        self.animation_is_running = True
        self.animation_func = func
        self.animation_list_of_args = list_of_args
        self.animate_frame_length = len(list_of_args)
        self.animation_frame_number = 0
        self.animation()
        self.timer.start(interval)
        self.main_ctrl.subscribe_close_func(self.stop_animation)
        
    def stop_animation(self):
        self.timer.stop()
        self.animation_is_running = False
        self.animation_func = None
        self.animation_list_of_args = []
        self.animation_frame_length = 0
        self.animation_frame_number = 0
        self.main_ctrl.unsubscribe_close_func(self.stop_animation)

    def animation(self):
        self.animation_func(self.fig,*self.animation_list_of_args[self.animation_frame_number])
        self.draw()
        self.animation_frame_number+=1
        if self.animation_frame_number >= self.animate_frame_length:
            self.animation_frame_number = 0
        
##class MyMplCanvas(FigureCanvas):
##    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
##
####    def __init__(self, parent=None, width=5, height=4, dpi=100):
####        fig = Figure(figsize=(width, height), dpi=dpi)
##    def __init__(self, parent=None):
##        fig = Figure()
##        self.axes = fig.add_subplot(111)
##        # We want the axes cleared every time plot() is called
##        self.axes.hold(False)
##
##        self.compute_initial_figure()
##
##        FigureCanvas.__init__(self, fig)
##        self.setParent(parent)
##
##        FigureCanvas.setSizePolicy(self,
##                                   QtGui.QSizePolicy.Expanding,
##                                   QtGui.QSizePolicy.Expanding)
##        FigureCanvas.updateGeometry(self)
##
##    def compute_initial_figure(self):
##        pass
##
##class DrawTriangleCanvas(MyMplCanvas):
##    '''Canvas with traiangle drawing.'''
##
##    def __init__(self, *args, **kwargs):
##        self.triangle = kwargs.pop('triangle',None)
##        self.degree = kwargs.pop('degree',None)
##        MyMplCanvas.__init__(self, *args, **kwargs)
##
##    def compute_initial_figure(self):
##        self.compute_figure()
##
##    def update_figure(self, *args, **kwargs):
##        self.triangle = kwargs.pop('triangle',None)
##        self.degree = kwargs.pop('degree',None)
##        self.axes.cla()
##        self.compute_figure()
##        self.draw()
##        
##
##    def compute_figure(self):
##        A = self.triangle.pop('A',None)
##        B = self.triangle.pop('B',None)
##        C = self.triangle.pop('C',None)
##        a = self.triangle.pop('a',None)
##        b = self.triangle.pop('b',None)
##        c = self.triangle.pop('c',None)
##        
##        if not (None in [A,B,C,a,b,c,self.degree]):
##
##            if self.degree:
##                A = A*np.pi/180. if A else A
##                B = B*np.pi/180. if B else B
##                C = C*np.pi/180. if C else C
##
##            # setup path
##            verts = []
##            verts.append((0., 0.))
##            verts.append((c*np.cos(A), c*np.sin(A)))
##            verts.append((b, 0.))
##            verts.append((0., 0.))
##            # scale path to 1 + off set
##            scale = np.max(verts)
##            verts = verts/scale
##            verts[:,0] = verts[:,0]+(1-np.max(verts[:,0]))/2
##            verts[:,1] = verts[:,1]+(1-np.max(verts[:,1]))/2
##            # describe path
##            codes = [Path.MOVETO,
##                     Path.LINETO,
##                     Path.LINETO,
##                     Path.CLOSEPOLY,
##                     ]
##            # build path
##            path = Path(verts, codes)
##
##            patch = patches.PathPatch(path, facecolor='orange', lw=2)
##            self.axes.add_patch(patch)
##        self.axes.set_xlim(-0.2,1.2)
##        self.axes.set_ylim(-0.2,1.2)
##        self.axes.axis('off')
        
##class MyStaticMplCanvas(MyMplCanvas):
##    """Simple canvas with a sine plot."""
##
##    def compute_initial_figure(self):
##        t = arange(0.0, 3.0, 0.01)
##        s = sin(2*pi*t)
##        self.axes.plot(t, s)


##class MyDynamicMplCanvas(MyMplCanvas):
##    """A canvas that updates itself every second with a new plot."""
##
##    def __init__(self, *args, **kwargs):
##        MyMplCanvas.__init__(self, *args, **kwargs)
##        timer = QtCore.QTimer(self)
##        timer.timeout.connect(self.update_figure)
##        timer.start(1000)
##
##    def compute_initial_figure(self):
##        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')
##
##    def update_figure(self):
##        # Build a list of 4 random integers between 0 and 10 (both inclusive)
##        l = [random.randint(0, 10) for i in range(4)]
##
##        self.axes.plot([0, 1, 2, 3], l, 'r')
##        self.draw()
            
##class ApplicationWindow(QtGui.QMainWindow):
##    def __init__(self):
##        QtGui.QMainWindow.__init__(self)
##        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
##        self.setWindowTitle("application main window")
##
##        self.file_menu = QtGui.QMenu('&File', self)
##        self.file_menu.addAction('&Quit', self.fileQuit,
##                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
##        self.menuBar().addMenu(self.file_menu)
##
##        self.help_menu = QtGui.QMenu('&Help', self)
##        self.menuBar().addSeparator()
##        self.menuBar().addMenu(self.help_menu)
##
##        self.help_menu.addAction('&About', self.about)
##
##        self.main_widget = QtGui.QWidget(self)
##
##        l = QtGui.QVBoxLayout(self.main_widget)
##        sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
##        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
##        l.addWidget(sc)
##        l.addWidget(dc)
##
##        self.main_widget.setFocus()
##        self.setCentralWidget(self.main_widget)
##
##        self.statusBar().showMessage("All hail matplotlib!", 2000)
##
##    def fileQuit(self):
##        self.close()
##
##    def closeEvent(self, ce):
##        self.fileQuit()
##
##    def about(self):
##        QtGui.QMessageBox.about(self, "About",
##                                """embedding_in_qt4.py example
##Copyright 2005 Florent Rougon, 2006 Darren Dale
##
##This program is a simple example of a Qt4 application embedding matplotlib
##canvases.
##
##It may be used and modified with no restriction; raw copies as well as
##modified versions may be distributed without limitation."""
##                                )
##
##
##qApp = QtGui.QApplication(sys.argv)
##
##aw = ApplicationWindow()
##aw.setWindowTitle('test')
##aw.show()
##sys.exit(qApp.exec_())
###qApp.exec_()
