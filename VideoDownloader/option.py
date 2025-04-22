from win10toast import ToastNotifier
import videoDownloader as vd
import musicDownloader as ms
import os, sys, ctypes, subprocess

OPTION = ""
URL = ""
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'downloads')
os.makedirs(OUTPUT_DIR, exist_ok= True)

if sys.platform.startswith("win"):
    toaster = ToastNotifier()

def notify_user(message):
    if(sys.platform.startswith("win")):
        toaster.show_toast("YouTube Downloader", message, duration=5)
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True)

def open_new_instance(option, url):
    subprocess.Popen([sys.executable, __file__, option, url])

def select_options(mode):
    attempts = 3

    while attempts > 0:
        option = input("Choose an option (Solo/Playlist/Exit): ").strip().lower()
        if option in ["solo", "playlist", "exit"]:
            break
        print("Invalid option. Please enter 'Solo' or 'Playlist'.")
        attempts -= 1
    else:
        print("Too many invalid attempts. Exiting...")
        exit()

    url = input("Enter YouTube URL: ").strip()

    if mode == "video":
        if option == "solo":
            vd.download_video(url, OUTPUT_DIR)
        elif option == "playlist":
            vd.download_playlist(url, OUTPUT_DIR)

    elif mode == "music":
        if option == "solo":
            ms.download_music(url, OUTPUT_DIR)
        elif option == "playlist":
            ms.download_music_playlist(url, OUTPUT_DIR)

    notify_user("Download finished!")

def select_music_or_video():
    attempts = 3

    while attempts > 0:
        option = input("Choose an option (Music/Video/Exit): ").strip().lower()
        if option in ["music", "video", "exit"]:
            break
        print("Invalid option. Please enter 'Music' or 'Video'.")
        attempts -= 1
    else:
        print("Too many invalid attempts. Exiting...")
        exit()

    if option == "music":
        select_options("music")
    elif option == "video":
        select_options("video")
    elif option == "exit":
        exit()