from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import FileHandler
import ConnectionIndicator
import Graph
import PIDGraph
import ctypes
import FakeConnection

import MotorGraph

test = True

variablesToLog=['FPGA Time', "Match Time","Commanded X","Estimated X","Commanded Y","Estimated Y","Commanded Theta","Estimated Theta",'Robot Mode',
                'Elbow Command', 'Elbow Angle', 'Elbow FeedForward', "Elbow Proportional", "Elbow Integral", "Elbow Derviative", "Elbow Total Command",
                'Elbow Command Actual',
                'Shoulder Command', 'Shoulder Angle', 'Shoulder FeedForward', "Shoulder Proportional", "Shoulder Integral", "Shoulder Derviative", "Shoulder Total Command",
                'Shoulder Command Actual',
                'Extension Command', 'Extension', 'Extension FeedForward', "Extension Proportional", "Extension Integral", "Extension Derviative", "Extension Total Command",
                'Extension Command Actual',
                'Left Front', 'Right Front', 'Left Rear', 'Right Rear']

controlVariables = ["Commanded X","Estimated X","Commanded Y", "Robot Mode"]

data = dict()

for variableName in variablesToLog:
    data[variableName]=[]

root = Tk()
root.minsize(900,500)
ctypes.windll.shcore.SetProcessDpiAwareness(2)
user32 = ctypes.windll.user32
ws = user32.GetSystemMetrics(0)
hs = user32.GetSystemMetrics(1)
print(f"{ws}x{hs}+0+0")
root.geometry(f"{user32.GetSystemMetrics(0)}x{user32.GetSystemMetrics(1)-280}+0+0")
root.title("Hot Dashboard")
content = ttk.Frame(root)
xFrame = Frame(root)
yFrame = Frame(root)
thetaFrame = Frame(root)
motorFrame = Frame(root)
elbowFrame = Frame(root)
elbowPidFrame = Frame(root)
shoulderFrame = Frame(root)
shoulderPidFrame = Frame(root)
extensionFrame = Frame(root)
extensionPidFrame = Frame(root)

xGraph = Graph.Graph(xFrame,data,title="XGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[2],estimatedDataName=variablesToLog[3], graphType="Drivetrain",
                     row=1,column=0)
yGraph = Graph.Graph(yFrame,data,title="YGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[4],estimatedDataName=variablesToLog[5], graphType="Drivetrain",
                        row=2,column=0)
thetaGraph = Graph.Graph(thetaFrame,data,title="ThetaGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[6],estimatedDataName=variablesToLog[7], graphType="Drivetrain",
                          row=1,column=1)
motorGraph = MotorGraph.MotorGraph(motorFrame,data,title="MotorGraph",xAxisName=variablesToLog[0], leftFront=variablesToLog[33], rightFront=variablesToLog[34],
                                   leftRear=variablesToLog[35], rightRear=variablesToLog[36], graphType="Drivetrain", row=2, column=1)

elbowGraph = Graph.Graph(elbowFrame,data,title="ElbowGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[9],estimatedDataName=variablesToLog[10],actualCommandDataName=variablesToLog[16], graphType="Elbow",
                       row=1,column=0)

elbowPidGraph = PIDGraph.PIDGraph(elbowPidFrame, data, title="ElbowPIDGraph", xAxisName=variablesToLog[0],
                             feedForward=variablesToLog[11], p=variablesToLog[12], i=variablesToLog[13], d=variablesToLog[14], total=variablesToLog[15],
                             graphType="Elbow", row=1,column=1)

shoulderGraph = Graph.Graph(shoulderFrame,data,title="ShoulderGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[17],estimatedDataName=variablesToLog[18],actualCommandDataName=variablesToLog[24], graphType="Shoulder",
                       row=1,column=0)

shoulderPidGraph = PIDGraph.PIDGraph(shoulderPidFrame, data, title="ShoulderPIDGraph", xAxisName=variablesToLog[0],
                             feedForward=variablesToLog[19], p=variablesToLog[20], i=variablesToLog[21], d=variablesToLog[22], total=variablesToLog[23],
                             graphType="Shoulder", row=1,column=1)

extensionGraph = Graph.Graph(extensionFrame,data,title="ExtensionGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[25],estimatedDataName=variablesToLog[26],actualCommandDataName=variablesToLog[32], graphType="Extension",
                       row=1,column=0)

extensionPidGraph = PIDGraph.PIDGraph(extensionPidFrame, data, title="ExtensionPIDGraph", xAxisName=variablesToLog[0],
                             feedForward=variablesToLog[27], p=variablesToLog[28], i=variablesToLog[29], d=variablesToLog[30], total=variablesToLog[31],
                             graphType="Extension", row=1,column=1)

namelbl = ttk.Label(root, text="Hot Dashboard")
name = ttk.Entry(root)

if not test:
    # fileHandler = FileHandler.FileHandler(root,graphs=[xGraph,yGraph,thetaGraph],data = data)
    connectionIndication = ConnectionIndicator.ConnectionIndicator(root,graphs=[xGraph,yGraph,thetaGraph,motorGraph, elbowGraph,elbowPidGraph, shoulderGraph, shoulderPidGraph, extensionGraph, extensionPidGraph],data=data,variablesToLog=variablesToLog)
else:
    connectionIndication = FakeConnection.FakeConnection(root,graphs=[xGraph,yGraph,thetaGraph,elbowGraph,elbowPidGraph, shoulderGraph, shoulderPidGraph, extensionGraph, extensionPidGraph],data=data,variablesToLog=variablesToLog, controlVariables=controlVariables)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.mainloop()

exit(0)
