from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv
import re
import ntcore
from os.path import basename

class ConnectionIndicator:

    hasString = re.compile("[A-Za-z]")

    def __init__(self,parent,graphs=None,data=None,variablesToLog=None):
        self.variablesToLog = variablesToLog
        self.protocol = 3
        self.ip = "10.0.68.2"
        self.data = data
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.grid(column=0,row=0,columnspan=2,sticky=(N,W))
        self.graphs = graphs
        self.reconnectButton = ttk.Button(self.frame, text="reconnect", command=self.connectToRobot )
        self. ipAddress = Label(self.frame,
                            text = self.ip,
                            fg = "blue")

        self.reconnect = BooleanVar(value=True)
        self.reconnectButton.grid(column = 0, row = 0,sticky=(W))
        self.ipAddress.grid(column = 1, row = 0,sticky=(W))
        self.inst = ntcore.NetworkTableInstance.getDefault()
        identity = basename(__file__)
        if self.protocol == 4:
            self.inst.startClient3(identity)
        else:
            self.inst.startClient4(identity)

        self.inst.setServer(self.ip)
        self.sd = self.inst.getTable("SmartDashboard")
        self.FMS = self.inst.getTable("FMSInfo")
        self.robotModePrev = ""


    def connectToRobot(self):
        if not self.inst.isConnected:
            identity = basename(__file__)
            if self.protocol == 3:
                self.inst.startClient3(identity)
            else:
                self.inst.startClient4(identity)

            self.inst.setServer(self.ip)

            self.sd = self.inst.getTable("SmartDashboard")
            self.FMS = self.inst.getTable("FMSInfo")
        robotMode = self.sd.getValue("Robot Mode","")
        print(robotMode)
        
        if (self.robotModePrev != robotMode and self.robotModePrev == "Disabled"):
            for variable in self.data:
                self.data[variable] = []
        elif robotMode != "Disabled":
            for variable in self.variablesToLog:
                if variable != "Robot Mode":
                    self.data[variable].append(self.sd.getValue(variable,0.0))
                else:
                    self.data[variable].append(robotMode)
            for graph in self.graphs:
                graph.draw()
        self.robotModePrev = robotMode
        self.parent.after(10,self.connectToRobot)