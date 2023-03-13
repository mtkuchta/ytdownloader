from urllib.parse import urlencode
from pytube import YouTube
import moviepy.editor
import os

def createFileName(defaultFileName):
    invalidCharacters = '<>()[]/'
    fileName=defaultFileName
    for char in invalidCharacters:
       fileName= fileName.replace(char,"")
    return fileName

def downloadAudioStream(link):
    yt=YouTube(link)
    audio_streams = yt.streams.filter(only_audio=True)
    stream_to_download = audio_streams.filter(abr="160kbps")[0]
    downloadedFileName=createFileName((yt.title + ".webm"))
    stream_to_download.download(filename=downloadedFileName)
    return downloadedFileName



def convertFileToMP3(fileName):   
    converted_file_name = fileName.replace(".webm", ".mp3")
    video = moviepy.editor.AudioFileClip(fileName)
    video.write_audiofile(converted_file_name)

def deleteSourceAfterConversion(fileName):
    if os.path.isfile(fileName):
        os.remove(fileName)
    

link =input("Podaj link:") 
downloadedAudioName = downloadAudioStream(link)
convertFileToMP3(downloadedAudioName)
deleteSourceAfterConversion(downloadedAudioName)


# linkList =open("linki.txt","r", encoding="utf-8")
# with open("linki.txt","r", encoding="utf-8") as linkList:   

#     for line in linkList:
#         try:
#             downloadedAudioName = downloadAudioStream(line)
#             convertFileToMP3(downloadedAudioName)
#             deleteSourceAfterConversion(downloadedAudioName)
#         except:
#             print("Something went wrong")