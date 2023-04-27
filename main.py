import os
from requests import get
SERVER_FOLDER = os.path.abspath("./server/")
PAPER_URL = "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/519/downloads/paper-1.19.4-519.jar"
JDK_URL = "https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.7%2B7/OpenJDK17U-jdk_x64_linux_hotspot_17.0.7_7.tar.gz"

def download_paper() -> None:
    with open(SERVER_FOLDER + "paper.jar",mode="wb") as paper_jar:
        data = get(PAPER_URL).content
        paper_jar.write(data)
        paper_jar.close()

def download_jdk() -> None:
    with open(SERVER_FOLDER + "jdk.tar.gz", mode="wb") as jdk_tar:
        data = get(JDK_URL)
        jdk_tar.write(data)
        jdk_tar.close()

if __name__ == "__main__":
    if(not os.path.exists(SERVER_FOLDER)):
        os.makedirs(SERVER_FOLDER)
    download_jdk()
    download_paper()