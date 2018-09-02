from windows import downloadwindow
import download

if __name__ == '__main__':
    #dwindow = downloadwindow.DownloadWindow("Download Window", 1000, 500)
    download = download.Download("https://www.google.co.uk/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png", "D:\\Downloads\\Download.zip")
