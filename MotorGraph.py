import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.style as mplstyle
import VarManager

class MotorGraph:
    def __init__(self,parent,data,addVarManager=False,title=None,xAxisName=None,leftFront=None,rightFront=None,leftRear=None,rightRear=None, 
                 row=None, column=None, graphType=None) -> None:
        mplstyle.use('fast')
        self.title = title
        self.row = row
        self.graphType = graphType
        self.column = column
        self.xAxisName = xAxisName
        self.leftFront = leftFront
        self.rightFront = rightFront
        self.leftRear = leftRear
        self.rightRear = rightRear
        self.parent = parent
        self.fig = Figure(dpi = 50)
        self.data = data
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        if addVarManager:
            self.varManager = VarManager.VarManager(self.parent,self.data)
            self.parent.columnconfigure(0, weight=1)
            self.parent.rowconfigure(0, weight=1)
        else:
            self.parent.columnconfigure(0, weight=1)
            self.parent.rowconfigure(0, weight=1)
        self.canvas = FigureCanvasTkAgg(self.fig,master = self.parent)
        self.canvas.get_tk_widget().grid(row = 0, column=0 , sticky=(N,E,S,W))

        self.replace()

    def replace(self):
        self.parent.grid(row=self.row,column=self.column,sticky=(N, W, S,E),padx=10, pady=10)

    def reset(self):
        self.startTime = self.data[self.xAxisName]

    def draw(self):
        self.ax.clear()
        time = self.data[self.xAxisName]
        leftFront = self.data[self.leftFront]
        rightFront = self.data[self.rightFront]
        leftRear = self.data[self.leftRear]
        rightRear = self.data[self.rightRear]

        self.ax.tick_params(axis='both', which='major', labelsize=16)

        self.ax.plot(time, leftFront, 'b-+',label="leftFront")
        self.ax.plot(time, rightFront, 'r-h',label="rightFront")
        self.ax.plot(time, leftRear, 'g-o',label="leftRear")
        self.ax.plot(time, rightRear, 'k-p',label="rightRear")

        # if max(time) > 20:
            # self.ax.set_xlim([max(time)-20, max(time)])

        # if max(time) > self.startTime+20:
        #     self.ax.set_xlim([max(time)-20, max(time)])

        plt.xticks(np.arange(max(time), max(time), 1.0))

        self.ax.set_ylim([-1.1,1.1])

        self.ax.legend(fontsize=16)
        self.fig.suptitle(self.title, fontsize=16)
        self.canvas.draw_idle()
        # self.canvas.figure.tight_layout()
        # self.canvas.get_tk_widget().grid(row = 0, column=0 , sticky=(N,E,S,W))

    def resize(self,event):
        print(self.title,self.parent.winfo_width(),self.parent.winfo_height())

