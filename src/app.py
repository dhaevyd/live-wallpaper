import tkinter as tk
from tkinter import filedialog
import vlc
import sys
import os

class LiveWallpaper:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Live Wallpaper")
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("400x200")
        self.root.configure(bg="#1a1a1a")

        # Title
        tk.Label(
            self.root,
            text="Live Wallpaper",
            font=("Arial", 20, "bold"),
            bg="#1a1a1a",
            fg="white"
        ).pack(pady=20)

        # Pick video button
        tk.Button(
            self.root,
            text="Pick Video",
            command=self.pick_video,
            bg="#4a4a4a",
            fg="white",
            padx=20,
            pady=10
        ).pack(pady=10)

        # Stop button
        tk.Button(
            self.root,
            text="Stop Wallpaper",
            command=self.stop_video,
            bg="#8b0000",
            fg="white",
            padx=20,
            pady=10
        ).pack(pady=5)

    def pick_video(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.mov *.avi *.mkv")]
        )
        if file_path:
            self.play_video(file_path)

    def play_video(self, path):
        media = self.instance.media_new(path)
        media.add_option("input-repeat=999999")  # loop
        self.player.set_media(media)
        self.player.play()

    def stop_video(self):
        self.player.stop()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = LiveWallpaper()
    app.run()
