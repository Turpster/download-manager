from windows import downloadwindow
import download

if __name__ == '__main__':
    #dwindow = downloadwindow.DownloadWindow("Download Window", 1000, 500)
    download = download.Download("https://www.google.com/", "D:\\Downloads\\Download.zip")
