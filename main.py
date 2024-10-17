from tkinter import Label, Tk
import time

class Clock:
    def __init__(self, window):
        self.window = window
        self.window.title('py-gui-clock')
        app_window.geometry('420x150') # Window size (fixed due to value below).
        app_window.resizable(0, 0) # 0, 0 = False which means non resizable.

        self.text_font = ('Boulder', 72, 'bold')
        self.background = 'black'
        self.foreground = 'white'
        self.border_width = 20

        # Pre-created variables above are assigned to a Label widget which is then stored in a new variable.
        self.label = Label(app_window, font=self.text_font, bg=self.background, fg=self.foreground, bd=self.border_width) 
        self.label.grid(row=0, column=1) # Place label in a grid view.

        self.digital_clock()

    # A method fetching the current time in a configured format from "strftime", loops every 200ms to update the clock.
    def digital_clock(self):
        time_display = time.strftime('%H:%M:%S') # Grab strftime from "import time" module.
        self.label.config(text=time_display)
        self.label.after(200, self.digital_clock)

if __name__ == '__main__':
    app_window = Tk() # Create main app window.
    clock = Clock(app_window) # Create instance of "Clock" and initialize the clock.
    app_window.mainloop() #Start the Tkinter loop.
