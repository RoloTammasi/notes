from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

# Manually set OS variable.
# TODO: Automate this so check what OS is being used
OS = 'linux'

# Set initial directory for system file dialog
if OS == 'linux':
    initial_dir = "/"
elif OS == 'windows':
    initial_dir = "C:\\"

class TkinterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tkinter Test")

        self.label = Label(master, text="Testing out Tkinter!")
        self.label.pack()

        self.label = Label(master, text="Browse to a file...")
        self.label.pack()

        self.text_box_browse = Text(root, height=2, width=60, background="white")
        self.text_box_browse.pack()

        self.browse_button = Button(master, text="Browse", command=self.getFiles)
        self.browse_button.pack()

        self.run_button = Button(master, text="Run", command=self.runProgram)
        self.run_button.pack()

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack()

    def getFiles(self):
        '''
        Opens up a file dialog window and allows user to select one or many HTML files. Prints file path(s) to
        text_box_browse text widget.
        '''

        # Open file dialog window
        self.files = tkFileDialog.askopenfilenames(initialdir = initial_dir,
                                                     title = "Select file",
                                                     filetypes = (("html files","*.htm"),
                                                                  ("html files","*.html"),
                                                                  ("all files","*.*"))
                                                   )

        # Store file name(s) in a readable string
        files_string = ''
        for f in self.files:
            files_string += str(f) + ', '
        files_string = files_string[:-2]

        # Print file name(s) in text_box_browse
        self.text_box_browse.delete(1.0, END)
        self.text_box_browse.insert(INSERT, files_string)

    def runProgram(self):
        '''
        Sends list of file(s) to parsing script.
        TODO: Literally everything.
        '''
        print "Send files to parsing script..."

root = Tk()
main_window = TkinterGUI(root)
root.mainloop()