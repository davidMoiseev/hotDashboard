from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv
import re
import ntcore
from os.path import basename

class FakeConnection:
    def __init__(self,parent,graphs=None,data=None,variablesToLog=None, controlVariables=None):
        self.parent = parent
        self.graphs = graphs
        self.data = data
        self.variablesToLog = variablesToLog
        self.controllableVariables = controlVariables

        self.frame = Frame(parent)
        self.frame.grid(column=0,row=0,columnspan=2,sticky=(N,W))
        self.graphs = graphs
        self.reconnectButton = ttk.Button(self.frame, text="reconnect", command=self.fakeRobot)
        self.reconnectButton.grid(column = 0, row = 0,sticky=(W))
        self.changeButton = ttk.Button(self.frame, text="changeMode", command=self.changeMode)
        self.changeButton.grid(column = 2, row = 0,sticky=(W))
        self.ipAddress = Label(self.frame, text = "Test Fake Robot", fg = "blue")
        self.ipAddress.grid(column = 1, row = 0,sticky=(W))

        self.robotMode = "Disabled"
        self.robotModePrev = ""

        self.dataStuff = ['Elbow FeedForward', "Elbow Proportional", "Elbow Integral", "Elbow Derviative", "Elbow Total Command"]

        self.time = 0
        self.var = 0

    def fakeRobot(self):
        print(self.robotMode)
        
        if (self.robotModePrev != self.robotMode and self.robotModePrev == "Disabled"):
            for variable in self.data:
                self.data[variable] = []
        elif self.robotMode != "Disabled":
            for variable in self.variablesToLog:
                if variable != "Robot Mode":
                    if variable == "FPGA Time":
                        self.data[variable].append(self.time)
                        self.time += 2
                    elif variable in self.dataStuff:
                        self.data[variable].append(self.var)
                        self.var += .01
                    else:
                        self.data[variable].append(self.var)
                        self.var += .1
                else:
                    self.data[variable].append(self.robotMode)
            for graph in self.graphs:
                graph.draw()
        self.robotModePrev = self.robotMode
        self.parent.after(10,self.fakeRobot)

    def changeMode(self):
        if(self.robotMode == "Disabled"):
            self.robotMode = "Fake"
            self.time = 0
            self.var = 0
        else:
            self.robotMode = "Disabled"
            self.time = 0
            self.var = 0

    