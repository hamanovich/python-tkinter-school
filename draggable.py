import tkinter as tk


class DraggableWidget(tk.Label):
    def __init__(self, master, on_release_callback=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>",
                  lambda event: self.on_release(event, on_release_callback))
        self.start_x = 0
        self.start_y = 0

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        x, y = self.winfo_x() + (event.x - self.start_x), self.winfo_y() + \
            (event.y - self.start_y)
        self.place(x=x, y=y)

    def on_release(self, _, on_release_callback):
        if on_release_callback:
            on_release_callback(self.cget("text"),
                                self.winfo_x(), self.winfo_y())
