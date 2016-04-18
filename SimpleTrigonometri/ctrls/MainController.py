import numpy as np
from PyQt4 import QtCore
from models.Model import Model
from views.MainView import MainView
from views.PlotWidget import MplFigureCanvas

class MainController(object):

    def __init__(self):
        self._close_funcs = []
        self.model = Model()
        self.fig_widget = None
        self.main_view = MainView(self)
        self.main_view.show()

    # subscribe a function for closing on program exit
    def subscribe_close_func(self, func):
        if func not in self._close_funcs:
            self._close_funcs.append(func)

    # unsubscribe a function from closing on program exit
    def unsubscribe_close_func(self, func):
        if func in self._close_funcs:
            self._close_funcs.remove(func)

    # call all close functions on close.
    def announce_close(self):
        # call this function from main application
        for func in self._close_funcs:
            func()
            
    def main_view_init(self, **kwargs):
        self.main_line_edits = kwargs.pop('lineEdits',None)
        self.main_combo_boxes = kwargs.pop('comboBoxes',None)
        self.main_fig_widget = kwargs.pop('fig_widget',None)
        self.main_deg_rad = kwargs.pop('deg_rad',None)
        self.main_statusbar = kwargs.pop('statusbar',None)

        
        self.set_line_edits(self.model.values)
        self.set_combo_boxes(self.model.comboBoxItems, self.model.comboBoxIndexes)
        self.update_combo_boxes()
        
        self.fig_widget = MplFigureCanvas(self)
        self.set_result(self.model.status, self.model.triangle, self.model.deg_rad)
        self.main_fig_widget.addWidget(self.fig_widget)

    def set_line_edits(self, values):
        for n in range(len(self.main_line_edits)):
            if values[n]:
                self.main_line_edits[n].setText(str(values[n]))
                
    def set_combo_boxes(self, comboBoxItems, comboBoxIndexes):
        for n in range(len(self.main_combo_boxes)):
            self.main_combo_boxes[n].clear()
            self.main_combo_boxes[n].addItems(comboBoxItems[n])
            self.main_combo_boxes[n].setCurrentIndex(comboBoxIndexes[n])
            
    def update_combo_boxes(self):
        keys = []
        for cb in self.main_combo_boxes:
            keys.append(cb.currentText())
        self.set_combo_boxes(*self.model.update_combo_boxes(keys))

    def update_deg_rad(self):
        deg_rad = True if self.main_deg_rad.currentIndex() == 0 else False
        values = self.model.update_deg_rad(deg_rad)
        self.set_line_edits(values)
        self.calculate()

    def calculate(self):
        keys = []
        for cb in self.main_combo_boxes:
            keys.append(cb.currentText())

        values = []
        for le in self.main_line_edits:
            values.append(le.text())
            try:
                values[-1] = float(values[-1])
            except ValueError:
                values[-1] = None

        deg_rad = True if self.main_deg_rad.currentIndex() == 0 else False
        
        status, triangle = self.model.triangle_calc(keys, values, deg_rad)
        self.set_result(status, triangle, deg_rad)
        
    def set_result(self, status, triangle, deg_rad):
        msg = self.model.status_msg(status)
        self.main_statusbar.showMessage(msg)
        
        if self.fig_widget.animation_is_running:
            self.fig_widget.stop_animation()
            
        if status==0:
            self.fig_widget.plot(self.model.draw_triangle, triangle, deg_rad)
        elif status==1:
            list_of_args = [(t, deg_rad) for t in triangle]
            self.fig_widget.start_animation(self.model.draw_triangle, list_of_args, 2000)
        elif status==2:
            list_of_args = self.model.path_list_calc(triangle, deg_rad)
            self.fig_widget.start_animation(self.model.draw_path, list_of_args, 100)
        else:
            self.fig_widget.fig.clf()
            self.fig_widget.draw()
        
    
