import tkinter as tk
from tkinter import Entry, Frame, Label
from tkinter.constants import  HORIZONTAL, RAISED, SUNKEN


class Colorpicker:
    def __init__(self,root):
        self.root = root
        self.root.title("Color Picker")
        self.root.geometry("300x520")
        self.root.resizable(0,0)
        self.root.iconbitmap(r'icon.ico')

        self.R = tk.IntVar()
        self.G = tk.IntVar()
        self.B = tk.IntVar()

        self.color_canvas = Label(self.root,bg="#8400ff",width=40,height=10,bd=2,relief=RAISED)
        self.color_canvas.place(x=7,y=2)
        self.color_canvas.bind("<Double-1>",self.copy_color)

        frame = Frame(self.root,bd=2,relief=SUNKEN)
        frame.place(x=7,y=170,height=180,width=285)

        r_label = Label(frame,text="Red",width=5,fg="#ff0000",font=('arial',10,'bold'))
        r_label.place(x=5,y=24)

        self.R_Scale = tk.Scale(frame,from_=0,to=255,length=210,fg="#ff0000",orient=HORIZONTAL,command=self.scaleMove)
        self.R_Scale.set(132)
        self.R_Scale.place(x=50,y=6)

        g_label = Label(frame,text="Green",width=5,fg="#00a200",font=('arial',10,'bold'))
        g_label.place(x=5,y=68)

        self.G_Scale = tk.Scale(frame,from_=0,to=255,length=210,fg="#00a200",orient=HORIZONTAL,command=self.scaleMove)
        self.G_Scale.place(x=50,y=50)

        b_label = Label(frame,text="Blue",width=5,fg="#0000ff",font=('arial',10,'bold'))
        b_label.place(x=5,y=122)

        self.B_Scale = tk.Scale(frame,from_=0,to=255,length=210,fg="#0000ff",orient=HORIZONTAL,command=self.scaleMove)
        self.B_Scale.set(255)
        self.B_Scale.place(x=50,y=105)

        hex_label = Label(self.root,text="Hex Code :",font=('arial',10,'bold'))
        hex_label.place(x=7,y=360)

        self.hex_entry = Entry(self.root,width=12,font=('arial',10))
        self.hex_entry.insert(tk.END,'##8400ff')
        self.hex_entry.place(x=90,y=360)

        rbg_label = Label(self.root,text="RGB Code :",font=('arial',10,'bold'))
        rbg_label.place(x=7,y=390)

        self.rgb_entry = Entry(self.root,width=12,font=('arial',10))
        self.rgb_entry.place(x=90,y=390)

        suggested_label = Label(self.root,text="Basic Colors:",font=('arial',10,'bold'))
        suggested_label.place(x=7,y=420)

        self.color = Label(self.root,bg="#000000",width=2,height=1,bd=2,)
        self.color.place(x=10,y=450)
        self.color.bind("<Double-1>",self.copy_color)

        self.color2 = Label(self.root,bg="#FF0000",width=2,height=1,bd=2,)
        self.color2.place(x=40,y=450)
        self.color2.bind("<Double-1>",self.copy_color)

        self.color3 = Label(self.root,bg="#00FF00",width=2,height=1,bd=2,)
        self.color3.place(x=70,y=450)
        self.color3.bind("<Double-1>",self.copy_color)

        
        self.color4 = Label(self.root,bg="#0000FF",width=2,height=1,bd=2,)
        self.color4.place(x=100,y=450)
        self.color4.bind("<Double-1>",self.copy_color)

        self.color5 = Label(self.root,bg="#FFFF00",width=2,height=1,bd=2,)
        self.color5.place(x=130,y=450)
        self.color5.bind("<Double-1>",self.copy_color)

        self.color6 = Label(self.root,bg="#00FFFF",width=2,height=1,bd=2,)
        self.color6.place(x=10,y=480)
        self.color6.bind("<Double-1>",self.copy_color)

        self.color7 = Label(self.root,bg="#FF00FF",width=2,height=1,bd=2,)
        self.color7.place(x=40,y=480)
        self.color7.bind("<Double-1>",self.copy_color)

        
        self.color8 = Label(self.root,bg="#808080",width=2,height=1,bd=2,)
        self.color8.place(x=70,y=480) #ff6Ab6
        self.color8.bind("<Double-1>",self.copy_color)

        
        self.color9 = Label(self.root,bg="#800000",width=2,height=1,bd=2,)
        self.color9.place(x=100,y=480)
        self.color9.bind("<Double-1>",self.copy_color)

        
        self.color10 = Label(self.root,bg="#808000",width=2,height=1,bd=2,)
        self.color10.place(x=130,y=480)
        self.color10.bind("<Double-1>",self.copy_color)

    def scaleMove(self,*args):
        self.R = int(self.R_Scale.get())
        self.G = int(self.G_Scale.get())
        self.B = int(self.B_Scale.get())
        rgb = f"{self.R},{self.G},{self.B}"

        self.hex =  "#%02x%02X%02x"%(self.R,self.G,self.B)
        self.color_canvas.config(bg=self.hex)

        self.hex_entry.delete(0,tk.END)
        self.hex_entry.insert(0,self.hex)

        self.rgb_entry.delete(0,tk.END)
        self.rgb_entry.insert(0,rgb)

    def copy_color(self,*args):
        root.clipboard_clear()  
        root.clipboard_append(self.hex) 
        

root = tk.Tk()
Colorpicker(root)
root.mainloop()