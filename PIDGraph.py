import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.style as mplstyle
import VarManager

class PIDGraph:
    def __init__(self,parent,data,addVarManager=False,title=None,xAxisName=None,feedForward=None,p=None,i=None,d=None,total=None, 
                 row=None, column=None, graphType=None) -> None:
        mplstyle.use('fast')
        self.title = title
        self.row = row
        self.graphType = graphType
        self.column = column
        self.xAxisName = xAxisName
        self.feedForward = feedForward
        self.p = p
        self.i = i
        self.d = d
        self.total = total
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

    def draw(self):
        self.ax.clear()
        time = self.data[self.xAxisName]
        feedForward = self.data[self.feedForward]
        p = self.data[self.p]
        i = self.data[self.i]
        d = self.data[self.d]
        total = self.data[self.total]

        self.ax.tick_params(axis='both', which='major', labelsize=16)

        self.ax.plot(time, feedForward, 'b-+',label="feedForward")
        self.ax.plot(time, p, 'r-h',label="p")
        self.ax.plot(time, i, 'g-o',label="i")
        self.ax.plot(time, d, 'k-p',label="d")
        self.ax.plot(time, total, 'm-',label="total")

        # if max(time) > 20:
            # self.ax.set_xlim([max(time)-20, max(time)])

        plt.xticks(np.arange(max(time), max(time), 1.0))

        self.ax.set_ylim([-1.1,1.1])

        self.ax.legend(fontsize=16)
        self.fig.suptitle(self.title, fontsize=16)
        self.canvas.draw_idle()
        # self.canvas.figure.tight_layout()
        # self.canvas.get_tk_widget().grid(row = 0, column=0 , sticky=(N,E,S,W))

    def resize(self,event):
        print(self.title,self.parent.winfo_width(),self.parent.winfo_height())

