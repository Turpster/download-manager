from tkinter import *
from downloadmanager import *

class DownloadWindow:
    def __init__(self, name=None, width=None, height=None):
        if (name != None):
            self.name = name
        else:
            name = "Download Manager"

        self.root = Tk(name)
        self.root.title(name)

        if (width == None): width = 200;
        if (height == None): height = 200;

        scrwidth = self.root.winfo_screenwidth()
        scrheight = self.root.winfo_screenheight()

        x = (scrwidth / 2) - (width / 2)
        y = (scrheight / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.setup_window()

        self.DownloadManager = DownloadManager(updatefunc=self.download_update)

        self.root.mainloop()

    def load_downloads(self):
        # TODO LOAD DOWNLOADS FROM DOWNLOADMANAGER
        pass
    def setup_window(self):
        self.download_pane_grid = Frame(self.root)
        self.menubar = Menu(self.root)

        self.root.config(menu=self.menubar)

        self.fileMenu = Menu(self.menubar)
        self.fileMenu.add_command(label="Download...", underline=0)
        self.fileMenu.add_command(label="Remove Download...", underline=0)

        self.viewMenu = Menu(self.menubar)

        self.menubar.add_cascade(label="File", underline=0, menu=self.fileMenu)
        self.menubar.add_command(label="Exit", command=lambda: quit(0))

        self.download_pane_grid.pack()

        self.download_update()

    """ICON | FILENAME | PERCENT | PROGRESS BAR | SIZE | URL"""

    def download_update(self):
        pass