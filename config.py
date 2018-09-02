from ConfigParser import *
import os

class Config:
    def __init__(self, fileloc):
        self.config = ConfigParser()
        self.fileloc = fileloc

        if not os.path.isfile(fileloc):
            open(fileloc, "w").close()
            self.config.write(fileloc)
        self.config.read(fileloc)
    def save(self):
        self.config.write(self.fileloc)