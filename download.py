import urllib2
import threading
import os
import requests

class Download:
    class Status:
        DOWNLOADING = 0,
        DOWNLOADED = 1,
        PAUSED = 2,
        STOPPED = 3,
        ERROR = 4

    def __init__(self, url, saveloc, name=None, chunksize=1024):
        self.thread = threading.Thread(name=url.strip('/')[-1],target=self.run, args= (url, saveloc, name, chunksize))
        self.thread.start()
    def run(self, url, saveloc, name, chunksize):
        self.url = url
        print(url)
        if not os.path.exists(saveloc):
            self.saveloc = saveloc
        else: raise Exception("File already exists") # Maybe be change this to a do while if the user hasn't selected a Download?
        self.chunksize = chunksize
        self.progress = float(0.0)
        self.status = Download.Status.DOWNLOADING
        if (name == None):
            self.name = url.strip('/')[-1]
        else:
            self.name = name
        print(url)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
        request = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'})
        self.response = urllib2.urlopen(request)
        try:
            self.size = int(self.response.info().getheader('Content-Length').strip())
        except Exception:
            self.size = None
            raise Exception
            # TODO Handle error

        print(self.size)
        self.bytessofar = 0

        if self.download():
            self.file.close()
            os.rename(self.saveloc + ".download", self.saveloc[::-9]) # Might be wrong
            print(self.saveloc[::-9]) # TODO Delete this line after testing
            self.change_status(Download.Status.DOWNLOADED)
            pass
        else:
            # TODO HANDLE ERROR
            # Rename file extension
            pass
        # TODO FINISHED DOWNLOAD
    def download(self):
        self.file = open(self.saveloc + ".download", "w") # TODO make sure to close file
        while True:
            try:
                chunk = self.response.read(self.chunksize)
            except:
                # TODO HANDLE ERROR
                return False
            self.bytessofar += len(chunk)
            self.file.write(chunk)


            if not chunk:
                return True

            self.progress = self.size / self.bytessofar
            continue


    def change_status(self, mode):
        self.status = mode
        # TODO Change the mode of the download
        pass