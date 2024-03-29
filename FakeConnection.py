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

        self.screenType = "Drivetrain"

        self.frame = Frame(parent)
        self.frame.grid(column=0,row=0,columnspan=2,sticky=(N,W))
        self.graphs = graphs
        self.reconnectButton = ttk.Button(self.frame, text="reconnect", command=self.fakeRobot)
        self.reconnectButton.grid(column = 0, row = 0,sticky=(W))
        self.changeButton = ttk.Button(self.frame, text="changeMode", command=self.changeMode)
        self.changeButton.grid(column = 1, row = 0,sticky=(W))
        self.ipAddress = Label(self.frame, text = "Test Fake Robot", fg = "blue")
        self.ipAddress.grid(column = 2, row = 0,sticky=(W))
        self.drivetrainButton = ttk.Button(self.frame, text="Drivetrain", command=self.drivetrainButton)
        self.drivetrainButton.grid(column=0, row=1, sticky=(W))
        self.elbowButton = ttk.Button(self.frame, text="Elbow", command=self.setElbow)
        self.elbowButton.grid(column=1, row=1, sticky=(W))
        self.shoulderButton = ttk.Button(self.frame, text="Shoulder", command=self.setShoulder)
        self.shoulderButton.grid(column=1, row=1, sticky=(W))
        self.extensionButton = ttk.Button(self.frame, text="Etension", command=self.setExtension)
        self.extensionButton.grid(column=1, row=1, sticky=(W))
        self.intakeButton = ttk.Button(self.frame, text="Intake", command=self.intakeButton)
        self.intakeButton.grid(column=2, row=1, sticky=(W))
        self.getScreenButton = ttk.Button(self.frame, text="Get Screen Type", command=self.getScreenType)
        self.getScreenButton.grid(column=3, row=1, sticky=(W))

        self.robotMode = "Disabled"
        self.robotModePrev = ""

        self.dataStuff = ['Elbow FeedForward', "Elbow Proportional", "Elbow Integral", "Elbow Derviative", "Elbow Total Command"]

        self.time = 0
        self.varSmall = 0
        self.var = 0

    def fakeRobot(self):
        # print(self.robotMode)
        
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
                        self.data[variable].append(self.varSmall)
                        self.varSmall += .005
                    else:
                        self.data[variable].append(self.var)
                        self.var += .1
                else:
                    self.data[variable].append(self.robotMode)
            for graph in self.graphs:
                if(graph.graphType == self.screenType):
                    graph.draw()
                    graph.replace()
                else:
                    graph.parent.grid_remove()
                
        self.robotModePrev = self.robotMode
        self.parent.after(10,self.fakeRobot)

    def changeMode(self):
        if(self.robotMode == "Disabled"):
            self.robotMode = "Fake"
            self.varSmall = 0
            self.var = 0
        else:
            self.robotMode = "Disabled"
            self.varSmall = 0
            self.var = 0

    def drivetrainButton(self):
        self.screenType = "Drivetrain"

    def setElbow(self):
        self.screenType = "Elbow"

    def setShoulder(self):
        self.screenType = "Shoulder"

    def setExtension(self):
        self.screenType = "Extension"

    def intakeButton(self):
        self.screenType = "Intake"

    def getScreenType(self):
        print(self.screenType)