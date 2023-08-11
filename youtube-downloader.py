import os
import sys
from pytube import YouTube
from pytube.exceptions import RegexMatchError

def func_folder():
    folderName = 'youtube-videos'
    return {
        'folderName':folderName,
        'folderPath':os.path.join(os.path.abspath(os.sep),folderName)
    }



def pytube(videolink):
    yt = YouTube(videolink)
    try:
        folderPath = func_folder()
        _title = yt.title+".mp4"
        if not os.path.exists(os.path.join(folderPath.get('folderPath'),_title)):
            print("Download in progresss...\n",_title)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(createFolder('youtube-videos'))
            return {
                "Download_status" : "Successfull",
                "video_title": _title
            }
        else:
            return {
                "Download_status" : "Ignored",
                "video_title": _title
            }

    except Exception as err:
        if Exception:
            print(err)
            folderpath = func_folder()
            reason = "File Exists at location :"+ folderpath.get('folderPath')
            return {
                "Download_status" : "Failed!",
                "video_title": _title,
                "Reason":""
            }
        else:
            print(Exception)

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
    print('---Youtube Downloader CLI---')
    link = input("Enter the youtube video link: ")
    try:
         download_status = pytube(link)
         print('Status: ', download_status.get('Download_status'))
         folderPath = func_folder()
         if download_status.get('Download_status') == 'Successfull':
             print("Download Location: ", folderPath.get('folderPath'))
         else:
             print("File already exists at :", folderPath.get('folderPath'))
         input()
    except Exception as err:
        print(err)
        if RegexMatchError:
             print("invalid url!")


if __name__ == "__main__":
    main()