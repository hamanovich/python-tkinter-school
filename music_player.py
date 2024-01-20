from tkinter import Button, font
from pygame import mixer

from config import CONFIG


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        mixer.init()
        self.state = 0

        mixer.music.load('audio/Fountains.mp3')

    def make_button(self):
        self.play_button = Button(
            self.root,
            text="🔉",
            font=font.Font(size=CONFIG["font_size"]["title"]),
            cursor="hand2",
            highlightthickness=0,
            bd=1,
            pady=5,
            command=self.play_music)
        self.play_button.place(x=10, y=800)

    def play_music(self):
        if self.state == 0:
            mixer.music.play()
            self.play_button.config(text="🔇")
            self.state = 1
        elif self.state == 1:
            mixer.music.pause()
            self.play_button.config(text="🔉")
            self.state = 0
