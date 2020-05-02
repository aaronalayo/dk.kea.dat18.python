import tkinter as tk
from tkinter import Frame, Tk, BOTH, Text, Menu, END, filedialog, Label
from PIL import ImageTk, Image



class PhotoEditor(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent        
        self.initUI()

    def initUI(self):

        self.parent.title("Photo Editor")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.open_img)
        menubar.add_cascade(label="File", menu=fileMenu)        

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)
    
    def openfn(self):
        filename = filedialog.askopenfilename(title='open')
        return filename

    def open_img(self):
        x = self.openfn()
        img = Image.open(x)
        img = img.resize((800, 800), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(root, image=img)
        panel.image = img
        panel.pack(fill = BOTH)
        return x


if __name__ == '__main__':

    root=Tk()
    ph=PhotoEditor(root)
    root.geometry("800x800+500+500")
    root.mainloop()
