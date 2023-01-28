from pytube import YouTube
import os
def pytube(videolink):
    yt = YouTube(videolink)
    try:
        title = yt.title+'.mp4'
        print("Downloading in progresss...\n",title)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(createFolder('youtube-videos'))
        return {
            "Download_status" : "Successfull",
            "video_title": title
        }
    except:
        return {
            "Download_status" : "Failed!",
            "video_title": title
        }


def createFolder(folderName):
    _path=os.path.abspath(os.sep),folderName
    try:
        if os.path.exists(os.path.join(os.path.abspath(os.sep),folderName)):
            _path=os.path.join(os.path.abspath(os.sep),folderName)
        else:
            os.makedirs(os.path.abspath(os.sep)+folderName)
            _path = os.path.abspath(os.sep)+folderName

    except FileExistsError:
        pass
    return _path

def main():
    print('---pytube CLI---')
    link = input("Enter the youtube video link: ")
    folderName = 'youtube-videos'
    download_status = pytube(link)
    print(download_status.get('Download_status'))
    print("Download Location: ", os.path.join(createFolder(folderName),download_status.get('video_title')))

if __name__ == "__main__":
    main()