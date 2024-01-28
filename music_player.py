from tkinter import Button, font
from pygame import mixer

from config import CONFIG


class MusicPlayer:
    def __init__(self, root, audio_file, **kwargs):
        self.root = root
        mixer.init()
        self.state = 0
        self.autoplay = kwargs.get("autoplay")

        mixer.music.load(audio_file)

        if (self.autoplay):
            mixer.music.play()
            self.state = 1

    def make_button(self, **kwargs):
        self.play_button = Button(
            self.root,
            text=kwargs.get("button_play", "🔇" if self.autoplay else "🔉"),
            font=font.Font(size=CONFIG["font_size"]["title"]),
            cursor="hand2",
            highlightbackground=CONFIG["bg"]["main"],
            pady=5,
            width=kwargs.get("width", 3),
            command=self.play_music)
        if "x" in kwargs and "y" in kwargs:
            self.play_button.place(x=kwargs.get("x"), y=kwargs.get("y"))
        else:
            self.play_button.grid(row=kwargs.get("row", 0))
        

    def play_music(self, **kwargs):
        if self.state == 0:
            mixer.music.play()
            self.play_button.config(text=kwargs.get("button_play", "🔇"))
            self.state = 1
        elif self.state == 1:
            mixer.music.pause()
            self.play_button.config(text=kwargs.get("button_pause", "🔉"))
            self.state = 0

    def destroy(self):
        mixer.music.stop()
        try:
            self.play_button.destroy()
        except AttributeError:
            pass