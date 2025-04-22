import yt_dlp as youtube

def download_video(url, output_path):

    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }

    with youtube.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(f"Preparing to download: {info['title']}")
        ydl.download([url])
        print(f"Download concluído: {info['title']}")

def download_playlist(url, output_path):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': False
    }

    with youtube.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        print(f"Playlist Title: {info['title']}")
        ydl.download([url])
        print(f"Download da playlist concluído: {info.get('title', 'Playlist')}")