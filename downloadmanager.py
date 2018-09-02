from download import Download
from config import Config

import os

class DownloadManager:
    def __init__(self):
        self.downloads = []
        self.config = Config("config.ini")
        if not "DownloadManager" in self.config.config.sections():
            self.config.config["DownloadManager"] = {"DownloadLocation": get_download_path()}
            self.config.save()
    def download(self, url):
        self.downloads.append(Download(url, self.config.config["DownloadManager"]["DownloadLocation"] + "\\" + url.strip('/')[-1]))

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
