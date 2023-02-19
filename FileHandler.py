from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv
import re

class FileHandler:

    hasString = re.compile("[A-Za-z]")

    def __init__(self,parent,graphs,data):
        self.data = data
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.grid(column=0,row=0,columnspan=2,sticky=(N,W))
        self.graphs = graphs
        self.loadFileButton = ttk.Button(self.frame, text="Load File", command=self.browseFiles )
        self. label_file_explorer = Label(self.frame,
                            text = "No file loaded",
                            fg = "blue")

        self.recordDataVar = BooleanVar(value=True)
        self.recordData = ttk.Checkbutton(self.frame, text="Record Data", variable=self.recordDataVar, onvalue=True, command=self.fileLoadCheck)
        self.loadFileButton.grid(column = 0, row = 0,sticky=(W))
        self.label_file_explorer.grid(column = 1, row = 0,sticky=(W))  
        self.recordData.grid(column = 2, row = 0,sticky=(W))

    def loadCSV(self,fileName):
        varMap = []
        with open(fileName) as f:
            parsedCSV = csv.reader(f,delimiter=',')
            firstRow = parsedCSV.__next__()
            index = 0
            varMap = [None] * firstRow.__sizeof__()
            for var in firstRow:
                self.data[var] = []
                varMap[index] = var
                index = index + 1
            for row in parsedCSV:
                index = 0
                for dataElement in row:
                    if (self.hasString.match(dataElement) or dataElement == ""):
                        self.data[varMap[index]].append(dataElement)
                    else:
                        self.data[varMap[index]].append(float(dataElement))
                    index = index + 1
        self.data

    def loadFile(self,fileName):
        self.label_file_explorer.configure(text = f"File Opened: {fileName}")
        self.recordDataVar.set(False)
        self.loadCSV(fileName)
        for graph in self.graphs:
            graph.draw()

    def browseFiles(self):
        fileName = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("csv files",
                                                        "*.csv*"),
                                                        ("log files",
                                                        "*.log*"),
                                                       ("all files",
                                                        "*.*")))
      
        self.loadFile(fileName)


    def fileLoadCheck(self):
        if "No file loaded" not in self.label_file_explorer.cget("text"):
            self.recordDataVar.set(False)