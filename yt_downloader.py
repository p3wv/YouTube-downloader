from pytube import YouTube


def get_usr_input():

    usr_given_video_link = input('give us the link to the video you want to download: ')

    return usr_given_video_link

def video_download_by_high_res(yt_link):

    yt = YouTube(yt_link)

    stream = yt.streams.get_highest_resolution()

    stream.download()


if __name__ == '__main__':

    video_download_by_high_res(get_usr_input())