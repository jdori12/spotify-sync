import subprocess

def download_playlist(music_directory: str, playlist: str):
    """
    Download spotify playlist to a certain directory
    :param music_directory: directory to download music to
    :param playlist: link to spotify playlist
    """
    subprocess.run([
        "spotdl",
        "--output",
        f"{music_directory}{{title}}",
        playlist
    ])