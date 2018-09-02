from Tkinter import *

class DownloadWindow:
    def __init__(self, name=None, width=None, height=None):
        if (name != None):
            self.name = name
        else:
            name = "Download Manager"

        self.root = Tk(name)

        if (width == None): width = 200;
        if (height == None): height = 200;
        self.root.geometry(str(width) + "x" + str(height))
        self.setup_window()
        self.root.mainloop()

    def setup_window(self):
        self.download_pane_frame = Frame(self.root)
        self.download_options_frame = Frame(self.root)
        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)

        self.fileMenu = Menu(self.menubar)
        self.submenu = Menu(self.fileMenu)
        self.submenu.add_command(label="New feed")
        self.submenu.add_command(label="Bookmarks")
        self.submenu.add_command(label="Mail")
        self.fileMenu.add_cascade(label='Import', menu=self.submenu, underline=0)

        self.fileMenu.add_separator()

        self.fileMenu.add_command(label="Exit", underline=0)
        self.menubar.add_cascade(label="File", underline=0, menu=self.fileMenu)

