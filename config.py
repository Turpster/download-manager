from configparser import *
import os

class Config:
    def __init__(self, fileloc):
        self.config = ConfigParser()
        self.fileloc = fileloc

        if not os.path.isfile(fileloc):
            with open(fileloc, "w") as file:
                self.config.write(file)

        print ("s")
        self.config.read(fileloc)
    def save(self):
        with open(self.fileloc, "w") as file:
            self.config.write(file)