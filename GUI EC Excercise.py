import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
    
        self.main_window.title("Test average tool")

        self.main_window.configure(bg='green')

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_labels = []
        self.entry_widgets = []

        for i in range(1, 4):
            label = tkinter.Label(self.top_frame, text=f'Enter the score for test {i}:', fg='yellow', bg='green')
            entry = tkinter.Entry(self.top_frame, width=10, highlightbackground='black', highlightcolor='black') 
            self.prompt_labels.append(label)
            self.entry_widgets.append(entry)

        for i in range(3):
            self.prompt_labels[i].grid(row=i, column=0, sticky='w')
            self.entry_widgets[i].grid(row=i, column=1, sticky='e')

        self.calc_button = tkinter.Button(self.bottom_frame, text='Average', command=self.average)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def average(self):
        test_scores = [float(entry.get()) for entry in self.entry_widgets if entry.get()]
        
        if len(test_scores) == 3:
            average = sum(test_scores) / 3
            tkinter.messagebox.showinfo('Average', f'The average test score is: {average}')
        else:
            tkinter.messagebox.showinfo('oops there is an error!', 'Please enter all three test scores.')

my_gui = MyGUI()







        
