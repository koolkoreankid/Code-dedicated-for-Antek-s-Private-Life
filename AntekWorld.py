import tkinter as tk                
from tkinter import font  as tkfont
import os
import random
import webbrowser
import tkinter.messagebox
from PIL import Image, ImageTk 
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as toradora
from matplotlib import style

style.use("ggplot")
file =open('AntekQuotes1.2018.txt', 'r')
quotes = file.readlines()

LARGE_FONT= ("Times", 12)

class KKK(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.winfo_toplevel().title("All about MC Shrimp")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menu=tk.Menu(container)
        tk.Tk.config(self, menu=menu)

        subMenu = tk.Menu(container)
        menu.add_cascade(label="Stalk!", menu=subMenu) # drops down the list once pressed.
        subMenu.add_command(label="Emma", command=lambda: re.search(emma))
        subMenu.add_command(label="Joanna", command=lambda: re.search(joanna))
        subMenu.add_command(label="Karolina", command=lambda: re.search(karolina))
        subMenu.add_command(label="agata", command=lambda: re.search(agata))
        subMenu.add_command(label="nicole", command=lambda: re.search(nicole))
        subMenu.add_separator()
                
        editMenu=tk.Menu(menu)
        menu.add_cascade(label="BBB", menu=editMenu)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageGraph):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Antek World!", font=LARGE_FONT)
        label.pack(side="top", fill="x", pady=10)

        image = Image.open("dil.png") 
        photo = ImageTk.PhotoImage(image)

        label=tk.Label(self, image=photo)
        label.image = photo # very important!
        label.pack()
        
        printC=tk.Button(self, text="generate random antek quote", command=lambda: re.quote(self))
        printC.pack(side="bottom")

        button1 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Page Three",
                            command=lambda: controller.show_frame("PageGraph"))
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Come back Emma!",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Come back Emma!",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageGraph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="antek's prey graph", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Come back Emma!",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.get_tk_widget().pack(side="bottom", fill=tk.BOTH, expand=True)



class re():
        def __init__(self, name, website):
                self.name=name
                self.website=website           

        def search(self):
                webbrowser.open(self.website)

        def quote(self):
            random.shuffle(quotes)
            tkinter.messagebox.showinfo('Trust me it is the best quote you will find', quotes[0])

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
            
def animation(i):
    Data = open("datadata.txt", "r+").read()
    dataList = Data.split('\n')
    xList=[]
    yList=[]
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y =eachLine.split(',')
            xList.append(float(x))
            yList.append(float(y))
    a.clear()
    a.plot(xList, yList)
# you have to put "re" so that it is used in the class called "re"
emma=re("emma", "https://www.facebook.com/profile.php?id=100012066510291")
joanna=re("joana", "https://www.facebook.com/joanna.sobkow.3")
karolina=re("karolina", "https://www.facebook.com/karolina.rzuchowska.7")
agata=re("agata", "https://www.facebook.com/agata.zur")
nicole=re("joana", "https://www.facebook.com/nicole.saliba.520")
       

# global (constant) - allows to change the constant in different classses

app = KKK()
app.geometry("600x500")
ani = toradora.FuncAnimation(f, animation, interval=1000)
app.mainloop()