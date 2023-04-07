import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_258=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_258["font"] = ft
        GLabel_258["fg"] = "#333333"
        GLabel_258["justify"] = "center"
        GLabel_258["text"] = "label"
        GLabel_258.place(x=60,y=70,width=134,height=107)

        GButton_204=tk.Button(root)
        GButton_204["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_204["font"] = ft
        GButton_204["fg"] = "#000000"
        GButton_204["justify"] = "center"
        GButton_204["text"] = "Button"
        GButton_204.place(x=260,y=280,width=70,height=25)
        GButton_204["command"] = self.GButton_204_command

        GMessage_653=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_653["font"] = ft
        GMessage_653["fg"] = "#333333"
        GMessage_653["justify"] = "center"
        GMessage_653["text"] = "Message"
        GMessage_653.place(x=200,y=370,width=164,height=75)

        GRadio_80=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_80["font"] = ft
        GRadio_80["fg"] = "#333333"
        GRadio_80["justify"] = "center"
        GRadio_80["text"] = "RadioButton"
        GRadio_80.place(x=400,y=130,width=85,height=25)
        GRadio_80["command"] = self.GRadio_80_command

        GCheckBox_849=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_849["font"] = ft
        GCheckBox_849["fg"] = "#333333"
        GCheckBox_849["justify"] = "center"
        GCheckBox_849["text"] = "CheckBox"
        GCheckBox_849.place(x=30,y=210,width=70,height=25)
        GCheckBox_849["offvalue"] = "0"
        GCheckBox_849["onvalue"] = "1"
        GCheckBox_849["command"] = self.GCheckBox_849_command

        GLineEdit_763=tk.Entry(root)
        GLineEdit_763["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_763["font"] = ft
        GLineEdit_763["fg"] = "#333333"
        GLineEdit_763["justify"] = "center"
        GLineEdit_763["text"] = "Entry"
        GLineEdit_763.place(x=280,y=200,width=70,height=25)

    def GButton_204_command(self):
        print("command")


    def GRadio_80_command(self):
        print("command")


    def GCheckBox_849_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
