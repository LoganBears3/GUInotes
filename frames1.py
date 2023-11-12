import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()  # Create main window

        # configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('My GUI')


        self.top_frame = tkinter.Frame(self.main_window)  # Create a frame top
        self.bottom_frame = tkinter.Frame(self.main_window) # Create a frame bottom



        self.label1 = tkinter.Label(self.top_frame, text='John!')
        self.label2 = tkinter.Label(self.top_frame, text='James')
        self.label3 = tkinter.Label(self.top_frame, text='Jack')

        self.label1.pack(side ='left')
        self.label2.pack(side ='left')
        self.label3.pack(side ='left')
        

        self.label4 = tkinter.Label(self.bottom_frame, text='Jill')
        self.label5 = tkinter.Label(self.bottom_frame, text='Jane')
        self.label6 = tkinter.Label(self.bottom_frame, text='Joan')

        self.label4.pack(side ='left')
        self.label5.pack(side ='left')
        self.label6.pack(side ='left')

        self.mybutton = tkinter.Button(self.main_window, text='Click Me', command=self.do_something)
        self.quitbutton = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        self.mybutton.pack()
        self.quitbutton.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()
        
        self.label1.pack(side = 'left')  ### top left right bottom (assign where you want lebel 1 and 2 in the display)
        self.label2.pack(side = 'right')
     

        tkinter.mainloop()  # Enter the tkinter main loop

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button!')

my_gui = MyGUI()  # Create an instance of the MyGUI class

print("moving...on")