from config import playlist
from config import output_dir
from modules.downloader import download_playlist

if __name__=="__main__":
    download_playlist(output_dir, playlist)