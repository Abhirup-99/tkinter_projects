from tkinter import *
import time
import tkinter.scrolledtext as sc
from tkinter.filedialog import *
import tkinter.messagebox
import tkinter.colorchooser
import tkinter.font


root=Tk()
class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.filename = 'Untitled'
        self.text = sc.ScrolledText(self.master,height=40,width=100)
        self.text.pack(expand=True,fill=BOTH)
        self.default()
        self.menu_bar()
    def default(self):
        self.text['insertbackground'] = 'black'
        self.text['bg'] = 'white'
        self.text['fg'] = 'black'		

    def saveas(self,event=None):
        file=str(asksaveasfilename(title="Save as File",defaultextension=".txt",filetypes=[("all files","*.*"),('CSS','.css'),('HTML','.html'),('PYTHON','.py')]))
        if len(file)>0:
            f = open(file,'w')
            text = self.ta.get("1.0",END).encode("utf-8")
            f.write(text)
            f.close()
            self.filename = file 
            

    def statusbar(self):
        self.status=Label(self.master,text="HI",bd=1,relief=SUNKEN,bg="Blue",anchor=S)
        self.status.pack(fill=X)
    def save(self,event=None):
        if self.filename == 'Untitled':
            self.saveas()
        else:
            f = open(self.filename,"w")
            text = self.text.get("1.0",END).encode("utf-8")
            f.write(text)
            f.close()
            

    def NewFile(self,event=None):
        if tkinter.messagebox.askyesno("New","Do you want to save the file..."):
            self.save()
        self.text.delete(0.0, END)
        self.filename = "Untitled"
    def opn(self,event=None):
        File = str(askopenfilename(title="Open File",filetypes=[("all files","*.*"),('CSS','.css'),('HTML','.html'),('PYTHON','.py'),('WORD','.docx')]))
        if len(File) > 0:
            self.text.delete("1.0",END)
            try:
                f = open(File)
                for line in f:
                    self.text.insert(END,line)
                f.close()
                self.filename = str(File)
            except IOError:
                tkinter.messagebox.showwarning("Open file","Cannot open this file...") 
    def undo(self):
        entire=self.text.get("1.0",END)
        l=len(entire)

        if len(entire):
            new_string = entire[0:l-2]
            print(new_string)
            self.text.delete(0.0,END)
            self.text.insert(END,new_string)
    def copy(self):
        entire=self.text.get("1.0",END)
        self.master.clipboard_clear()
        self.master.clipboard_append(entire)
    def cut(self):
        self.copy()
        self.text.delete(0.0,END)
    def ti(self):
        localtime=time.asctime(time.localtime(time.time()))
        self.text.insert(END,localtime)    
    def txtcolor(self):
        color = tkinter.colorchooser.askcolor('black')
        if color:
            self.text['fg'] = color[1]
    def backcolor(self):
        color = tkinter.colorchooser.askcolor('white')
        if color:
            self.text['bg'] = color[1]
    def menu_bar(self):
        mymenu=Menu(self.master)
        self.master.config(menu=mymenu)
        submenu=Menu(mymenu)
        mymenu.add_cascade(label="File",menu=submenu)
        submenu.add_command(label="New",command=self.NewFile)
        submenu.add_command(label="Open",command=self.opn)
        submenu.add_command(label="Save",command=self.save)
        submenu.add_command(label="Save As",command=self.saveas)
        submenu.add_command(label="Exit",command=self.master.destroy)
        editmenu=Menu(mymenu)
        mymenu.add_cascade(label="Edit",menu=editmenu)
        editmenu.add_command(label="Undo",command=self.undo)
        editmenu.add_command(label="Copy",command=self.copy)
        editmenu.add_command(label="Cut",command=self.cut)
        editmenu.add_command(label="clear",command=self.text.delete(0.0,END))
        editmenu.add_separator()
        editmenu.add_command(label="Present Time",command=self.ti)
        formatmenu=Menu(mymenu)
        mymenu.add_cascade(label="Format",menu=formatmenu)
        formatmenu.add_command(label="Background Color",command=self.backcolor)
        formatmenu.add_command(label="Text Color",command=self.txtcolor)
        viewmenu=Menu(mymenu)
        mymenu.add_cascade(label="View",menu=viewmenu)
        viewmenu.add_command(label="Status Bar",command=self.statusbar)
        helpmenu=Menu(mymenu)
        mymenu.add_cascade(label="Help",menu=helpmenu)
        helpmenu.add_command(label="About")
main(root)
root.title("Notepad")
root.geometry("1600x700")
root.mainloop()
