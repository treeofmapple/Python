import yt_dlp as youtube

def download_music(url, output_path):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(f"Preparing to download audio: {info['title']}")
        ydl.download([url])
        print(f"Download concluído: {info['title']}.mp3")


def download_music_playlist(url, output_path):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'noplaylist': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(f"Playlist Title: {info['title']}")
        ydl.download([url])
        print(f"Download da playlist concluído: {info.get('title', 'Playlist')}")
