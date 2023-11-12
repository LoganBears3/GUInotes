import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()  # Create main window

        # configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('My GUI')


        self.label1 = tkinter.Label(self.main_window, text='Hello World!')
        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program.')
        self.label1.pack(side = 'left')  ### top left right bottom (assign where you want lebel 1 and 2 in the display)
        self.label2.pack(side = 'right')

        tkinter.mainloop()  # Enter the tkinter main loop

my_gui = MyGUI()  # Create an instance of the MyGUI class

print("moving...on")
