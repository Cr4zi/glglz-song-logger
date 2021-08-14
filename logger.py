import requests
import xml.etree.ElementTree as ET
import youtube_dl
import datetime
import os

def main():
    glglz = requests.get("https://glzxml.blob.core.windows.net/dalet/glglz-onair/onair.xml")
    data = ET.fromstring(glglz.text)
    titleName = data[2][5].text
    artistName = data[2][6].text

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "outtmpl": f"./songs/{artistName} - {titleName}.mp3",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
        }],
    }
    def write_to_file():
        with open("songs.txt", "a") as f:
            f.write("\n" + f"{artistName} - {titleName}")

    with open("songs.txt", "r") as f:
        lines = f.readlines()
        if f"{artistName} - {titleName}" in lines:
            main()
        else:
            write_to_file()

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Downloading audio now\n")
                ydl.download([f"ytsearch1:{artistName} - {titleName}"])
        print(f"[{datetime.datetime.now()}] Found song {artistName} - {titleName}.")
        main()

    except Exception as e:
        print(f"[{datetime.datetime.now()}] {artistName} - {titleName} not found in youtube.")
        print(e)
        main()


if __name__ == '__main__':
    main()