from tkinter import *
from tkinter import messagebox
from Knight_Tour import *
from Rat_In_The_Maze import *
import StartProcess

class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('750x300')
        self.root.resizable(False, False)
        self.root.title('Backtracking Algorithm')
        self.AlgoTypeVar = StringVar()
        self.AlgoTypeVar = "Backtracking Algorithm"
        self.MainWindow()
    
    def Exit(self):
        self.root.destroy()


    def run(self):
        if self.AlgoNameVar.get() == "Select Algorithm Name":
            messagebox.showerror("Incomplete Data!", "Please fill all the Fields to Start Visualization.")
        else:
            self.temp1 = self.DimensionOfBoard.get()
            self.temp2 = self.SpeedSlider.get()

            if self.AlgoNameVar.get() == "Knight Tour":
                self.root.destroy()
                Knight(self.temp1, self.temp2)
                

            if self.AlgoNameVar.get() == "Rat in the Maze":
                self.root.destroy()
                Rat_in_Maze(self.temp1, self.temp2)


    def MainWindow(self):
        self.AlgoNameLabel = Label(self.root, text='Select Algorithm Name:- ', pady=5, font=('Courier', 10))
        self.AlgoNameLabel.grid(row= 0, column= 1)
        self.AlgoNameVar = StringVar()
        self.AlgoNameVar.set("Select Algorithm Name")
        self.AlgoNameList = ["Select Algorithm Name", 'Knight Tour', 'Rat in the Maze']
        self.AlgoNameDrop = OptionMenu(self.root, self.AlgoNameVar, *self.AlgoNameList)
        self.AlgoNameDrop.grid(row=1, column=1)
        self.fill6 = Label(self.root, text='')
        self.fill6.grid(row=2, column=0)
        
        self.NoOfElementsLabel1 = Label(self.root, text="   Select the Dimension of Board:-", font=("Courier", 10))
        self.NoOfElementsLabel1.grid(row=3, column=0)
        self.NoOfElementsLabel2 = Label(self.root, text="(from 4x4 to 50x50)")
        self.NoOfElementsLabel2.grid(row=4, column=0)

        self.DimensionOfBoard = Scale(self.root, from_=4, to=50, orient=HORIZONTAL, sliderlength=20, width=10)
        self.DimensionOfBoard.grid(row=5, column=0)

        self.SpeedLabel1 = Label(self.root, text="Select Speed of Visualization:-", font=("Courier", 10))
        self.SpeedLabel1.grid(row=3, column=2)
        self.SpeedLabel2 = Label(self.root, text="(in Operations per sec.)")
        self.SpeedLabel2.grid(row=4, column=2)

        self.SpeedSlider = Scale(self.root, from_=1, to=100, orient=HORIZONTAL, sliderlength=20, width=10)
        self.SpeedSlider.grid(row=5, column=2)

        self.fill1 = Label(self.root, text="")
        self.fill1.grid(row=7, column=0)
        self.StartButton = Button(self.root, text="Start Visualization>", padx=5, command=self.run)
        self.StartButton.grid(row=8, column=1)
        self.fill2 = Label(self.root, text="")
        self.fill2.grid(row=9, column=0)

            