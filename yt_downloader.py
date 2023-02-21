from pytube import YouTube
import os

def get_usr_input():

    usr_given_video_link = input('give us the link to the video you want to download: ')

    return usr_given_video_link


def download_only_audio(yt_link):

    yt = YouTube(yt_link)

    stream = yt.streams.get_audio_only()

    audio_file = stream.download()

    base, ext = os.path.splitext(audio_file)
    audio_converted = base + '.mp3'
    os.rename(audio_file, audio_converted)
    
    print("Audio from chosen video downloaded to current working directory!")


def download_by_high_res(yt_link):

    yt = YouTube(yt_link)

    stream = yt.streams.get_highest_resolution()

    stream.download()

    print("Chosen video in the highest resolution downloaded to current working directory!")

def menu():
    submenu_selection = int(input("Choose video download classification: \n1. Audio\n2. Resolution\n\n"))

    if submenu_selection == 1:
        download_only_audio(get_usr_input())
        
    elif submenu_selection == 2:
        download_by_high_res(get_usr_input())
    else:
        raise KeyError("Choose 1 or 2")

# class Menu:
#     def __init__(self) -> None:
#         pass

# class Resolution:
#     def __init__(self) -> None:

        

if __name__ == '__main__':
    menu()