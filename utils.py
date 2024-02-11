import webbrowser
import sys
import os
import data

from config import CONFIG
from tkinter import *
from tkinter import font
from PIL import Image as PilImage, ImageTk


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


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


def get_menu_item_name(section):
    for item in data.menu_buttons:
        if item[0] == section:
            return item[1]
    return data.menu_buttons[0][1]


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


def make_label(frame, text, **kwargs):
    Label(frame,
          anchor=W,
          wraplength=kwargs.get("wraplength", 750),
          bg=CONFIG["bg"]["main"],
          font=font.Font(size=kwargs.get(
              "font_size", CONFIG["font_size"]["title"])),
          text=text).grid(row=kwargs.get("row", 0),
                          pady=(0, 10),
                          columnspan=kwargs.get("columnspan", 1))


def clear_frame_content(frame):
    frame.grid_remove()
    for widget in frame.winfo_children():
        widget.destroy()


frames = {}


def make_frame(frame_id, row, pady=0):
    frame = Frame(frames[frame_id], bg=CONFIG["bg"]["main"])
    frame.grid(row=row, pady=pady)
    return frame


def make_check_result_button(frame_id, command, row, pady=10, columnspan=1, text="Проверить результат"):
    frame_id.bind_all('<Return>', lambda _: command())
    Button(
        frame_id,
        text=text,
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
