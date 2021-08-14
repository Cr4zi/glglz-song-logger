import requests
from xml.dom import minidom
import youtube_dl
import datetime

def main():
    glglz = requests.get("https://glzxml.blob.core.windows.net/dalet/glglz-onair/onair.xml")
    with open("data.xml", "w") as f:
        f.write(glglz.text)

if __name__ == '__main__':
    main()