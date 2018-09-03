from download import Download
from config import Config

import os

class DownloadManager:
    def __init__(self, updatefunc):
        self.updatefunc = updatefunc

        self.downloads = []
        self.config = Config("config/config.ini")
        self.downloadfile = Config("config/downloads.ini")
        if not "DownloadManager" in self.config.config.sections():
            self.config.config["DownloadManager"] = {'DownloadLocation': get_download_path()}
            self.config.save()

        for downl in self.downloadfile.config.get("files"):
            
    def add_download(self, turl):

        if self.get_download(url=turl) == None:
            self.downloads.append(Download(turl, self.config.config["DownloadManager"]["DownloadLocation"] + "\\" + turl.strip('/')[-1]))
        else:
            raise Exception("Download url is already being downloaded")

        self.updatefunc()
    def remove_download(self):
        self.updatefunc()
        pass
    def pause_download(self, download):
        if download in self.downloads:
            download.thread.status = Download.Status.PAUSED

            print("Download has been paused")
        else:
            raise Exception("Download is not apart of the download list.")
    def get_download(self, url=None, saveloc=None, name=None):
        for download in self.downloads:
            if url == download.url or saveloc == download.saveloc or name == download.name:
                return download
            else:
                return None
def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg

        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')
    # TODO Add more platforms
