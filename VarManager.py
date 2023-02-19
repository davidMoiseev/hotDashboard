from tkinter import *
from tkinter import ttk


class VarManager:
    def __init__(self,parent,data) -> None:
        self.data = data
        self.parent = parent
        self.varFrame = Frame(parent)
        self.listBox = Listbox(self.varFrame,
                        bg = "grey",
                        activestyle = 'dotbox',
                        font = "Helvetica",
                        fg = "yellow")

        self.addVariable = ttk.Button(self.varFrame, text="Add from Smartdashboard",command=self.varSelectorDialog)
        self.varFrame.grid(column=1, row=0, sticky=(N,W,E,S))
        self.addVariable.grid(column=0, row=0,sticky=(N,W,E))
        self.listBox.grid(column=0, row=1,sticky=(N,S,E,W))
        self.varFrame.rowconfigure(1, weight=1)

    def varSelectorDialog(self):
        dialog = Toplevel(self.parent)
        listBox = Listbox(dialog,
                        bg = "grey",
                        activestyle = 'dotbox',
                        font = "Helvetica",
                        fg = "yellow")
        count = 0
        for label in self.data:
            listBox.insert(count,label)
            count = count + 1
        listBox.grid(row=0,column=0)