import os
from yt_dlp import YoutubeDL


def download_yt(playlist_id, download_folder_string):
    playlist_url = f"{playlist_id}"

    download_folder = f"{str(download_folder_string)}"

    os.makedirs(download_folder, exist_ok=True)

    ydl_opts = {
        'format': 'best[height<=720]/best[height<=480]',  
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'playlistend': None,  
        'noplaylist': False,  
        'age_limit': 18,  
        'username': 'YOUR_EMAIL',  
        'password': 'YOUR_PASSWORD'  
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

    print("Playlist download completed!")