import os
import sys
from pytube import YouTube
from pytube.exceptions import RegexMatchError

previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        os.system('cls')
        sys.stdout.write("\r{0}% Completed".format(liveprogress))

def func_folder():
    folderName = 'youtube-videos'
    return {
        'folderName':folderName,
        'folderPath':os.path.join(os.path.abspath(os.sep),folderName)
    }

def pytube(videolink):
    yt = YouTube(videolink)
    yt.register_on_progress_callback(on_progress)
    try:
        folderPath = func_folder()
        title = yt.title+'.mp4'
        if not os.path.exists(os.path.join(folderPath.get('folderPath'),title)):
            print("Downloading in progresss...\n",title)
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(createFolder('youtube-videos'))
            return {
                "Download_status" : "Successfull",
                "video_title": title
            }
        else:
            return {
                "Download_status" : "Ignored",
                "video_title": title
            }

    except:
        if FileExistsError:
            folderpath = func_folder()
            reason = "File Exists at location :"+ folderpath.get('folderPath')
            return {
                "Download_status" : "Failed!",
                "video_title": title,
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
    print('---pytube CLI---')
    link = input("Enter the youtube video link: ")
    try:
         download_status = pytube(link)
         print('Status: ', download_status.get('Download_status'))
         folderPath = func_folder()
         if download_status.get('Download_status') == 'Successfull':
             print("Download Location: ", folderPath.get('folderPath'))
         else:
             print("File already exists at :", folderPath.get('folderPath'))
    except:
         if RegexMatchError:
             print("invalid url!")


if __name__ == "__main__":
    main()