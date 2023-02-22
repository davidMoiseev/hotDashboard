from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import FileHandler
import ConnectionIndicator
import Graph
import PIDGraph
import ctypes
import FakeConnection

test = True

variablesToLog=['FPGA Time', "Match Time","Commanded X","Estimated X","Commanded Y","Estimated Y","Commanded Theta","Estimated Theta",'Robot Mode',
                'Elbow Command', 'Elbow Angle', 'Elbow FeedForward', "Elbow Proportional", "Elbow Integral", "Elbow Derviative", "Elbow Total Command",
                'Elbow Command Actual']

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
content = ttk.Frame(root)
xFrame = Frame(root)
yFrame = Frame(root)
thetaFrame = Frame(root)
armFrame = Frame(root)
pidFrame = Frame(root)

xGraph = Graph.Graph(xFrame,data,title="XGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[2],estimatedDataName=variablesToLog[3])
xFrame.grid(row=1,column=0,sticky=(N, W, S,E),padx=5, pady=5)
yGraph = Graph.Graph(yFrame,data,title="YGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[4],estimatedDataName=variablesToLog[5])
yFrame.grid(row=2,column=0,sticky=(N, W, S,E),padx=10, pady=10)
# thetaGraph = Graph.Graph(thetaFrame,data,title="ThetaGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[6],estimatedDataName=variablesToLog[7])
# thetaFrame.grid(row=1,column=1,sticky=(N, W, S,E),padx=10, pady=10)
armGraph = Graph.Graph(armFrame,data,title="ArmGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[9],estimatedDataName=variablesToLog[10],actualCommandDataName=variablesToLog[16])
armFrame.grid(row=2,column=1,sticky=(N, W, S,E), padx=10, pady=10)
pidGraph = PIDGraph.PIDGraph(pidFrame, data, title="PIDGraph", xAxisName=variablesToLog[0],
                             feedForward=variablesToLog[11], p=variablesToLog[12], i=variablesToLog[13], d=variablesToLog[14], total=variablesToLog[15])
pidFrame.grid(row=1,column=1,sticky=(N, W, S,E),padx=10, pady=10)
xFrame.grid(row=1,column=0,sticky=(N, W, S,E),padx=5, pady=5)

namelbl = ttk.Label(root, text="Hot Dashboard")
name = ttk.Entry(root)

if not test:
    # fileHandler = FileHandler.FileHandler(root,graphs=[xGraph,yGraph,thetaGraph],data = data)
    connectionIndication = ConnectionIndicator.ConnectionIndicator(root,graphs=[xGraph,yGraph,pidGraph,armGraph],data=data,variablesToLog=variablesToLog)
else:
    connectionIndication = FakeConnection.FakeConnection(root,graphs=[xGraph,yGraph,pidGraph,armGraph],data=data,variablesToLog=variablesToLog, controlVariables=controlVariables)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.mainloop()

exit(0)
