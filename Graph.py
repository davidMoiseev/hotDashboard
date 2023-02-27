import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import matplotlib.style as mplstyle
import VarManager

class Graph:
    def __init__(self,parent,data,addVarManager=False,title=None,xAxisName=None,estimatedDataName=None,commandDataname=None, actualCommandDataName=None,
                 graphType = None, row=None, column=None) -> None:
        mplstyle.use('fast')
        self.title = title
        self.row = row
        self.column = column
        self.graphType = graphType
        self.xAxisName = xAxisName
        self.estimatedDataName = estimatedDataName
        self.commandDataname = commandDataname
        self.actualCommandDataName = actualCommandDataName
        self.parent = parent
        self.fig = Figure(dpi = 50)
        self.data = data
        self.fig.clear()
        self.ax = self.fig.add_subplot(111)
        self.startTime = 0
        self.addVarManager = addVarManager
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
        yCommaand = self.data[self.commandDataname]
        yEsitmated = self.data[self.estimatedDataName]
        self.ax.tick_params(axis='both', which='major', labelsize=16)

        if self.actualCommandDataName == None:
            self.ax.plot(time, yCommaand, 'b-',label="Command")
            self.ax.plot(time, yEsitmated,'r-',label="Estimate")
        else:
            actualCommand = self.data[self.actualCommandDataName]
            self.ax.plot(time, yCommaand, 'b-o',label="Command")
            self.ax.plot(time, yEsitmated,'r-',label="Estimate")
            self.ax.plot(time, actualCommand, 'k-x', label = "Actual")

        # if max(time) > self.startTime+20:
        #     self.ax.set_xlim([max(time)-20, max(time)])
            
        plt.xticks(np.arange(max(time), max(time), 1.0))
        
        if self.addVarManager:
            ymax = max([max(yEsitmated),max(yCommaand),max(actualCommand)])
            ymin = min([min(yEsitmated),min(yCommaand),min(actualCommand)])
        else:
            ymax = max([max(yEsitmated),max(yCommaand)])
            ymin = min([min(yEsitmated),min(yCommaand)])
        
        if self.title == 'ThetaGraph' or self.title == "ArmGraph":
            self.ax.set_ylim([ymin-10,ymax+10])
            # plt.yticks(np.arange(-1, 370, 45.0), fontsize=16)
        else:
            self.ax.set_ylim([ymin-.5,ymax+.5])
            # plt.yticks(np.arange(-1, 8, 1.0), fontsize=16)

        self.ax.legend(fontsize=16)
        self.fig.suptitle(self.title, fontsize=16)
        self.canvas.draw_idle()
        # self.canvas.figure.tight_layout()
        # self.canvas.get_tk_widget().grid(row = 0, column=0 , sticky=(N,E,S,W))

    def resize(self,event):
        print(self.title,self.parent.winfo_width(),self.parent.winfo_height())

