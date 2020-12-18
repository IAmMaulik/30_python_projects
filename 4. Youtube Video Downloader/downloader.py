print("Welcome to Maulik Shah's YouTube Downloader")
print("Loading...")

import pytube

video_list = []

a = int(input("Enter your Choice\n(1)Download manually\n(2)Download entire playlist\n"))

if a==1:
    print("Enter the urls. Write STOP to terminate")

    while True:
        url = input("Enter the URL: ")        
        if url.lower()=='stop':
            break
        video_list.append(url)

    for x, video in enumerate(video_list):
        v = pytube.YouTube(video)
        stream = v.streams.get_by_itag(134)
        print(f"Downloading video {x}")
        stream.download()
        print("Done!\n")

if a==2:
    playlist = input("Enter the playlist link: ")
    p = pytube.Playlist(playlist)

    for i in p:
        video = pytube.YouTube(playlist)
        print(f"Downloading video {x+1}")
        stream = video.streams.get_by_itag(134)
        stream.download()
        print("Done")

if a>2 or a<1:
    print("Invalid request")