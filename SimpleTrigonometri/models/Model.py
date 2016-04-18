##import numpy as np
##from matplotlib.figure import Figure
##from matplotlib.backends.backend_qt4agg import (
##    FigureCanvasQTAgg as FigureCanvas)#,
##    NavigationToolbar2QT as NavigationToolbar)
##from matplotlib.path import Path
##import matplotlib.patches as patches

from models.Calculations import (triangle_calc,
                                 deg_rad_calc,
                                 draw_triangle,
                                 path_list_calc,
                                 draw_path)
import models.Messages as msg

class Model(object):
    def __init__(self):

        # variable placeholders
        self.triangle = {}
        self.status = -1
        self.deg_rad = True
        self.angle_keys = ['A','B','C']
        self.length_keys = ['a','b','c']
        self.comboBoxItemList = self.angle_keys + self.length_keys
        self.comboBoxIndexes = [0,3,4]
        self.comboBoxItems = [self.comboBoxItemList.copy(),self.comboBoxItemList.copy(),self.comboBoxItemList.copy()]
        self.values = [30,5,7]

        keys = [self.comboBoxItems[n][self.comboBoxIndexes[n]] for n in range(len(self.comboBoxIndexes))]
        self.triangle_calc(keys, self.values, self.deg_rad)

    def update_combo_boxes(self, keys):
        for n in range(len(self.comboBoxIndexes)):
            c = keys.copy()
            del c[n]
            self.comboBoxItems[n] = self.comboBoxItemList.copy()
            for cc in c:
                self.comboBoxItems[n].remove(cc)
            self.comboBoxIndexes[n] = self.comboBoxItems[n].index(keys[n])
        return self.comboBoxItems, self.comboBoxIndexes
            
    def update_deg_rad(self,deg_rad):
        if deg_rad != self.deg_rad:
            keys = [self.comboBoxItems[n][self.comboBoxIndexes[n]] for n in range(len(self.comboBoxIndexes))]
            for n in range(len(keys)):
                if keys[n] in self.angle_keys:
                    self.values[n] = deg_rad_calc(deg_rad,self.values[n])
            self.deg_rad = deg_rad
        return self.values
    
    def triangle_calc(self, keys, values, deg_rad):
        self.comboBoxIndexes = [self.comboBoxItems[n].index(keys[n]) for n in range(len(keys))]
        self.values = values
        self.deg_rad = deg_rad
        
        triangle = {}
        for i in range(len(keys)):
            triangle[keys[i]] = self.values[i]
        self.status, self.triangle = triangle_calc(triangle, deg_rad)
        
        return self.status, self.triangle

    def status_msg(self, *args):
        return msg.status_triangle(*args)

    def draw_triangle(self, fig, triangle, deg_rad):
        draw_triangle(fig, triangle, deg_rad)

    def path_list_calc(self,triangle, deg_rad):
        return path_list_calc(triangle, deg_rad)
        
    def draw_path(self, fig, path, triangle):
        draw_path(fig, path, triangle)
