import webbrowser
import sys

from config import CONFIG
from tkinter import *
from tkinter import font
from PIL import Image as PilImage, ImageTk

def func_name(): 
    return sys._getframe(1).f_code.co_name


def check_only_digit(var):
    value = var.get()
    if len(value) > 1:
        var.set(value[:1])
    elif not value.isdigit() and value != "":
        var.set("")


def check_only_letter(var):
    value = var.get()
    if len(value) > 1:
        var.set(value[:1])
    elif value.isdigit() and value != "":
        var.set("")


def find_coordinates(options, search_term):
    for option in options:
        if option[0] == search_term:
            return option[1]["x"], option[1]["y"]
    return None, None


def get_value(key, options):
    for element, category in options:
        if element == key:
            return category


global_images = []


def make_image(frame, img_path, width, height, **kwargs):
    img = PilImage.open(img_path)
    img_tk = ImageTk.PhotoImage(img)
    global_images.append(img_tk)
    img_canvas = Canvas(frame,
                        width=width,
                        height=height,
                        bg=kwargs.get("bg", CONFIG["bg"]["main"]),
                        highlightthickness=0)
    img_canvas.create_image(0, 0, anchor=NW, image=img_tk)

    if "x" in kwargs and "y" in kwargs:
        img_canvas.place(x=kwargs.get("x"), y=kwargs.get("y"))
    else:
        img_canvas.grid(row=kwargs.get("row", 0))


def get_page_title(frame, text, columnspan=1):
    Label(frame, anchor=W, wraplength=750,
          bg=CONFIG["bg"]["main"],
          font=font.Font(size=CONFIG["font_size"]["title"]),
          text=text).grid(row=0, pady=(0, 15), columnspan=columnspan)


def clear_frame_content(frame):
    frame.grid_remove()
    for widget in frame.winfo_children():
        widget.destroy()


frames = {}


def make_frame(frame_id, row, pady=0):
    frame = Frame(frames[frame_id], bg=CONFIG["bg"]["main"])
    frame.grid(row=row, pady=pady)
    return frame


def make_check_result_button(frame_id, command, row, pady=10, columnspan=1):
    frame_id.bind_all('<Return>', lambda _: command())
    Button(
        frame_id,
        text="Проверить результат",
        font=font.Font(size=CONFIG["font_size"]["title"]),
        highlightthickness=0,
        relief=SOLID,
        bg="white",
        activebackground="white",
        bd=1,
        pady=10,
        command=command).grid(row=row, columnspan=columnspan, pady=pady, sticky=EW)


def make_link(frame_id, task, row):
    link_label = Label(
        frame_id, text=task["meta"]["link_text"], padx=5, pady=3, font=font.Font(underline=True), cursor="hand2")
    link_label.grid(row=row, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open(task["meta"]["link"]))
