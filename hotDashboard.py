from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import FileHandler
import ConnectionIndicator
import Graph
import ctypes

variablesToLog=['FPGA Time', "Match Time","Commanded X","Estimated X","Commanded Y","Estimated Y","Commanded Theta","Estimated Theta",'Robot Mode',]

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
root.geometry(f"{user32.GetSystemMetrics(0)}x{user32.GetSystemMetrics(1)-500}+0+0")
content = ttk.Frame(root)
xFrame = Frame(root)
yFrame = Frame(root)
thetaFrame = Frame(root)

xGraph = Graph.Graph(xFrame,data,title="XGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[2],estimatedDataName=variablesToLog[3])
xFrame.grid(row=1,column=0,sticky=(N, W, S,E),padx=5, pady=5)
yGraph = Graph.Graph(yFrame,data,title="YGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[4],estimatedDataName=variablesToLog[5])
yFrame.grid(row=2,column=0,sticky=(N, W, S,E),padx=10, pady=10)
thetaGraph = Graph.Graph(thetaFrame,data,title="ThetaGraph",xAxisName=variablesToLog[0],commandDataname=variablesToLog[6],estimatedDataName=variablesToLog[7])
thetaFrame.grid(row=1,column=1,sticky=(N, W, S,E),padx=10, pady=10)
namelbl = ttk.Label(root, text="Hot Dashboard")
name = ttk.Entry(root)

# fileHandler = FileHandler.FileHandler(root,graphs=[xGraph,yGraph,thetaGraph],data = data)
connectionIndication = ConnectionIndicator.ConnectionIndicator(root,graphs=[xGraph,yGraph,thetaGraph],data=data,variablesToLog=variablesToLog)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.mainloop()

exit(0)
