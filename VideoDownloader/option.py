from win10toast import ToastNotifier
import videoDownloader as vd
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
        ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True)

def open_new_instance(option, url):
    subprocess.Popen([sys.executable, __file__, option, url])

def select_options():
    attempts = 3

    while attempts > 0:
        OPTION = input("Choose an option (Solo/Playlist/Exit): ").strip().lower()
        if OPTION in ["solo", "playlist", "exit"]:
            break
        print("Invalid option. Please enter 'Solo' or 'Playlist'.")
        attempts -= 1
    else:
        print("Too many invalid attempts. Exiting...")
        exit()

    if OPTION == "Solo":
        URL = str(input("Enter Youtube URL to download: ")).strip()
        DATA = vd.download_video(URL, OUTPUT_DIR)
        notify_user("Download finished!")
        open_new_instance("Solo", URL) 

    elif OPTION == "Playlist":
        URL = str(input("Enter Youtube playlist URL to download: ")).strip()
        DATA = vd.download_playlist(URL, OUTPUT_DIR)
        notify_user("Download finished!")
        open_new_instance("Playlist", URL)

    elif OPTION == "EXIT":
        exit()