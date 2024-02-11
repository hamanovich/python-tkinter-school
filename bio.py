import data
import sys
import os

from random import randint
from tkinter import *
from tkinter import font, messagebox
from PIL import Image as PilImage, ImageTk
from music_player import MusicPlayer

from config import CONFIG
from utils import *
from draggable import DraggableWidget


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


window = Tk()
window.geometry(f"{CONFIG["window"]["width"]}x{
                CONFIG["window"]["height"]}+{(window.winfo_screenwidth() - CONFIG["window"]["width"]) // 2}+{(window.winfo_screenheight() - CONFIG["window"]["height"]) // 2}")
window.resizable(0, 0)
window.title(data.project_title)
window.rowconfigure(0, minsize=CONFIG["window"]["width"], weight=1)
window.columnconfigure(1, minsize=CONFIG["window"]["height"]-200, weight=1)

window.option_add("*Label.background", "white")
window.option_add("*Label.foreground", "black")
window.option_add("*Entry.background", "white")
window.option_add("*Entry.foreground", "black")
window.option_add("*Entry.highlightBackground", "white")
window.option_add("*Entry.highlightThickness", 1)
window.option_add("*Canvas.background", "white")
window.option_add("*Frame.background", "white")
window.option_add("*Button.cursor", "hand2")
window.option_add("*Button.background", "white")
window.option_add("*Button.foreground", "black")
window.option_add("*Radiobutton.foreground", "black")

frame_ids = ["intro", "botanika", "anatomy", "cytology", "task_1_1", "task_1_2", "task_1_3",
             "task_2_1", "task_2_2", "task_2_3", "task_3_1", "task_3_2", "task_3_3", "result"]
tasks = ["intro", "task_1_1", "task_1_2", "task_1_3", "task_2_1",
         "task_2_2", "task_2_3", "task_3_1", "task_3_2", "task_3_3", "landing_result"]

total_tasks = sum(len(cat["tasks"]) for cat in data.content.values())
active_task_number = 0
score = 0
active_audio = None


def task_audio(audio):
    global active_audio
    player = MusicPlayer(frm_main, resource_path(audio), autoplay=True)
    player.make_button(x=775, y=10)
    active_audio = player


def make_home_btn():
    global btn_home

    btn_home = Button(frm_menu_buttons,
                      text="🏠",
                      highlightbackground=CONFIG["bg"]["main"],
                      font=font.Font(size=CONFIG["font_size"]["title"]),
                      command=go_home)
    btn_home.grid(row=5, pady=5, sticky=EW)


def choose_topic(slug, name):
    global active_task_number
    global btn_home
    global score

    if active_audio is not None:
        active_audio.destroy()

    for btn in menu_btns:
        btn.config(highlightbackground=CONFIG["bg"]["main"], fg="black")
    btn_index = [index for index, (slug_name, _, _) in enumerate(
        data.menu_buttons) if slug_name == slug]

    btn = menu_btns[btn_index[0]]
    btn.config(highlightbackground=CONFIG["bg"]["ok"], fg=CONFIG["bg"]["ok"])

    clear_content()
    landing_by_topic(slug)
    reset_score()

    lbl_main.config(text=name)
    lbl_score.config(text="")
    lbl_score_caveat.config(text="")

    if btn_home is None:
        make_home_btn()


def reset_score():
    global score
    global active_task_number

    score = 0
    active_task_number = 8
    lbl_score.config(text=f"{score}/{total_tasks}")
    lbl_score_caveat.config(text=data.messages["game_score_caveat"])


def increase_score():
    global score

    score += 1
    lbl_score.config(text=f"{score}/{total_tasks}")


def go_home():
    global btn_home
    global score
    global active_audio

    frm_landing.grid()
    for frame_id in frame_ids:
        clear_frame_content(frames[frame_id])
    clear_frame_content(btn_home)

    lbl_main.config(text=data.project_title)
    btn_home = None
    lbl_score.config(text="")
    lbl_score_caveat.config(text="")

    for btn in menu_btns:
        btn.config(highlightbackground=CONFIG["bg"]["main"], fg="black")

    if active_audio is not None:
        active_audio.destroy()


def left_panel_ui():
    global menu_btns
    global btn_home
    global frm_menu_buttons
    global frm_score
    global lbl_score
    global lbl_score_caveat

    frm_panel = Frame(window,
                      bg=CONFIG["bg"]["main"],
                      relief=SOLID,
                      bd=1,
                      width=150)
    frm_panel.grid(row=0, column=0, sticky=NSEW)
    frm_panel.grid_propagate(False)
    frm_panel.grid_columnconfigure(0, weight=1)

    frm_score = Frame(window,
                      bg=CONFIG["bg"]["main"],
                      width=140,
                      height=140)
    frm_score.place(x=5, y=350)

    Label(frm_panel, text="Выберите раздел:",
          bg=CONFIG["bg"]["main"]).grid(column=0, row=0, padx=5, pady=(25, 5), sticky=EW)
    frm_menu_buttons = Frame(frm_panel, bg=CONFIG["bg"]["main"])
    frm_menu_buttons.grid(row=1, padx=10, sticky=EW)
    frm_menu_buttons.grid_columnconfigure(0, weight=1)

    menu_btns = []

    for idx, (slug, name, _) in enumerate(data.menu_buttons):
        btn_menu = Button(frm_menu_buttons,
                          text=name,
                          highlightbackground=CONFIG["bg"]["main"],
                          font=font.Font(size=CONFIG["font_size"]["text"]),
                          command=lambda slug=slug, name=name: choose_topic(slug, name))
        btn_menu.grid(row=idx, pady=5, sticky=EW)
        menu_btns.append(btn_menu)

    btn_home = None

    Label(frm_panel,
          text=data.copyrights,
          bg=CONFIG["bg"]["main"],
          font=font.Font(size=10)).grid(row=2, sticky=N)

    lbl_score = Label(frm_score,
                      text="",
                      font=font.Font(size=CONFIG["font_size"]["heading"]),
                      bg=CONFIG["bg"]["main"])
    lbl_score.place(x=40, y=0)
    lbl_score_caveat = Label(frm_score,
                             text="",
                             wraplength=120,
                             font=font.Font(
                                 size=CONFIG["font_size"]["text_small"]),
                             justify=LEFT,
                             bg=CONFIG["bg"]["main"])
    lbl_score_caveat.place(x=10, y=45)

    make_image(window, resource_path(
        "images/sunflower.png"), 125, 142, x=12, y=740)


frm_main = Frame(window, bg=CONFIG["bg"]["main"], relief=SOLID, bd=1)
frm_main.grid(column=1, sticky=NSEW)
frm_main.columnconfigure(0, weight=1)
lbl_main = Label(frm_main,
                 text=data.project_title,
                 bg=CONFIG["bg"]["main"],
                 font=font.Font(size=CONFIG["font_size"]["heading"]))
lbl_main.grid(columnspan=3, pady=10, sticky=EW)
frm_content = Frame(frm_main, padx=5, pady=5, bg=CONFIG["bg"]["main"])
frm_content.grid(row=1)
frm_landing = Frame(frm_content, bg=CONFIG["bg"]["main"])
frm_landing.grid()

for frame_id in frame_ids:
    frame = Frame(frm_content, bg=CONFIG["bg"]["main"])
    frame.grid()
    frames[frame_id] = frame


def clear_content():
    frm_landing.grid_remove()
    for frame_id in frame_ids:
        clear_frame_content(frames[frame_id])


def start_game():
    clear_content()
    reset_score()
    make_home_btn()
    globals()[tasks[active_task_number]]()


def next_task():
    global active_task_number

    active_task_number += 1
    clear_content()
    globals()[tasks[active_task_number]]()


def show_message(success):
    if (success):
        messagebox.showinfo(
            data.messages["task_success_title"], data.messages["task_success_text"])
        increase_score()
    else:
        messagebox.showerror(
            data.messages["task_error_title"], data.messages["task_error_text"])

    next_task()


def landing(frame):
    Label(frame,
          text=f"Выберите раздел или нажмите \"{data.messages["play_button"]}\"",
          font=font.Font(size=CONFIG["font_size"]["title"]),
          bg=CONFIG["bg"]["main"]).grid(pady=(0, 10), columnspan=4)

    for idx, (slug, name, frm_img) in enumerate(data.menu_buttons):
        frm = Frame(frame, borderwidth=2, relief=GROOVE, cursor="hand2")
        frm.grid(row=1, column=idx, padx=10, pady=10)
        image = PhotoImage(file=resource_path(frm_img))
        lbl_image = Label(frm, image=image)
        lbl_image.image = image
        lbl_image.grid()
        lbl_image.bind("<Button-1>", lambda _, slug=slug,
                       name=name: choose_topic(slug, name))
        Label(frm, text=name, font=font.Font(
            size=CONFIG["font_size"]["text_small"])).grid(row=1)

    lbl_start = Label(frame,
                      text=data.messages["play_button"],
                      font=font.Font(size=CONFIG["font_size"]["heading"]),
                      anchor=CENTER,
                      bg="darkblue",
                      fg="white",
                      borderwidth=2,
                      relief=SOLID,
                      height=3,
                      cursor="hand2")
    lbl_start.grid(row=2, columnspan=4, padx=10, pady=25, sticky=EW)
    lbl_start.bind("<Button-1>", lambda _: start_game())


def landing_by_topic(topic_name):
    info = data.content[topic_name]
    frames[topic_name].grid()

    make_label(frames[topic_name], info["title"])
    task_audio(info["audio"])

    for i, detail in enumerate(info["details"]):
        Label(frames[topic_name],
              bg=CONFIG["bg"]["main"],
              wraplength=700,
              text=detail,
              font=font.Font(size=CONFIG["font_size"]["text"])).grid(row=i+1, pady=(0, 10))

    make_image(frames[topic_name], resource_path(info["preview"]["img_path"]),
               info["preview"]["width"], info["preview"]["height"], row=5, bg="white")
    make_link(frames[topic_name], info, 6)


def landing_result():
    result = None

    frames["result"].grid()
    lbl_main.config(text="Игра завершена!")

    Label(frames["result"],
          bg=CONFIG["bg"]["main"],
          wraplength=600,
          text=f"Ваш результат: {score}/{total_tasks}",
          font=font.Font(size=CONFIG["font_size"]["title"])).grid(row=1)

    if (score <= 4):
        result = data.results["bad"]
    if (score > 4 and score < 7):
        result = data.results["ok"]
    if (score >= 7):
        result = data.results["great"]
    if (score == 9):
        result = data.results["awesome"]
    if (score == 0):
        result = data.results["awfull"]

    Label(frames["result"],
          bg=CONFIG["bg"]["main"],
          wraplength=600,
          text=result["msg_result"],
          font=font.Font(size=CONFIG["font_size"]["title"])).grid(row=2, pady=(0, 20))

    make_image(frames["result"], resource_path(
        result["msg_image_path"]), 600, 600, row=3)

    MusicPlayer(frm_main, resource_path(
        result["msg_audio_path"]), autoplay=True)


def intro():
    info = data.intro
    frm = frames["intro"]
    frm.grid()

    make_label(frm, info["title"])
    make_image(frm, resource_path(info["image_path"]), 500, 333, row=1)

    for i, rule in enumerate(info["rules"]):
        Label(frames["intro"],
              bg=CONFIG["bg"]["main"],
              anchor=W,
              wraplength=700,
              text=rule,
              font=font.Font(size=CONFIG["font_size"]["text"])).grid(row=i+2, pady=(0, 5))

    make_check_result_button(frm, next_task, 10, text="Поехали!")


def task_1_1():
    task_name = func_name()
    row_entries = []
    task = data.content["botanika"]["tasks"][0]
    lbl_main.config(text=data.menu_buttons[0][1])
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"])
    make_label(frm, task["rule"], row=1,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    frm_options = make_frame(task_name, 2)
    frm_task = make_frame(task_name, 3)

    for i, option in enumerate(task["options"]):
        Label(frm_options,
              anchor=W,
              wraplength=750,
              bg=CONFIG["bg"]["main"],
              font=font.Font(size=CONFIG["font_size"]["text"]),
              text=f"{option[0]}. {option[1]}").grid(row=i)

    for i in range(len(task["answer"])):
        var = StringVar()
        var.trace_add("write", lambda *args, var=var: check_only_digit(var))
        entry = Entry(frm_task,
                      font=font.Font(size=CONFIG["font_size"]["heading"]),
                      width=2,
                      bd=2,
                      justify="center",
                      relief=SOLID,
                      textvariable=var)
        entry.grid(row=4, column=i, pady=15)
        row_entries.append(entry)
    row_entries[0].focus_set()

    def check_task():
        result = ""
        for i, variant in enumerate(row_entries):
            result += variant.get()
            variant.config(bg=CONFIG["bg"]["ok"] if variant.get(
            ) == task["answer"][i] else CONFIG["bg"]["error"], fg="white")

        frm.after(100, lambda: show_message(result == task["answer"]))
        active_audio.destroy()

    make_check_result_button(frm, check_task, 5)


def task_1_2():
    global active_audio

    task_name = func_name()
    answers = []
    keyword = []
    KEYWORD_COLUMN = 8
    task = data.content["botanika"]["tasks"][1]
    lbl_main.config(text=data.menu_buttons[0][1])
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"])
    make_label(frm, task["rule"], row=1,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    frm_options = make_frame(task_name, 2)
    frm_crossword = make_frame(task_name, 3, 20)

    for i, option in enumerate(task["options"]):
        Label(frm_options,
              anchor=W,
              wraplength=750,
              bg=CONFIG["bg"]["main"],
              width=75,
              font=font.Font(size=CONFIG["font_size"]["text_small"]),
              text=f"{i+1}. {option["question"]}").grid(row=i)

    for row, option in enumerate(task["options"]):
        for i in range(0, option["padLeft"]):
            Label(frm_crossword,
                  width=2,
                  bg=CONFIG["bg"]["main"]).grid(row=row+3, column=i)

        Label(frm_crossword,
              width=3,
              text=row+1,
              bd=1,
              background="lightblue",
              highlightthickness=1,
              relief=SOLID).grid(row=row+2, column=option["padLeft"])

        row_entries = []

        for i in range(option["padLeft"] + 1, option["padLeft"] + 1 + len(option["answer"])):
            var = StringVar()
            var.trace_add("write", lambda *args,
                          var=var: check_only_letter(var))
            entry = Entry(frm_crossword,
                          bg="yellow" if i == KEYWORD_COLUMN else "white",
                          width=3,
                          bd=1,
                          justify=CENTER,
                          relief=SOLID,
                          textvariable=var)
            entry.grid(row=row+2, column=i)
            row_entries.append(entry)

            if (i == KEYWORD_COLUMN):
                keyword.append(entry)

        answers.append(row_entries)

    def check_task():
        for i, crossword_answer in enumerate(answers):
            result = ""
            for k, entry in enumerate(crossword_answer):
                result += entry.get()
                entry.config(bg=CONFIG["bg"]["error"] if entry.get().lower(
                ) != task["options"][i]["answer"][k].lower() else CONFIG["bg"]["ok"], fg="white")

        word = "".join(char.get() for char in keyword)

        print(word, word.lower())

        frm.after(100, lambda: show_message(
            word.lower() == task["answer"].lower()))
        active_audio.destroy()

    make_check_result_button(frm, check_task, 5)


def task_1_3():
    global botanika_photos
    global active_audio

    task_name = func_name()
    lbl_main.config(text=data.menu_buttons[0][1])
    task = data.content["botanika"]["tasks"][2]
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"])
    make_label(frm, task["rule"], row=1,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    frm_wrapper = Frame(frm,
                        height=650,
                        width=650,
                        bd=0)
    frm_wrapper.grid(row=2)

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    botanika_photos = [
        ImageTk.PhotoImage(PilImage.open(resource_path(img_path)))
        for img_path in image_paths
    ]

    valid_options = []
    draggable_texts = [name for (name, _) in task["options"]]

    make_image(frm_wrapper, resource_path(task["bg"]), 650, 650, bg="white")

    def check_position(name, x, y):
        diff = 35
        xx, yy = find_coordinates(task["options"], name)

        if (abs(xx - x) < diff and abs(yy - y) < diff):
            if (name not in valid_options):
                valid_options.append(name)
        else:
            if (name in valid_options):
                valid_options.remove(name)

    draggable_lbls = []
    for i, text in enumerate(draggable_texts):
        lbl = DraggableWidget(
            frm_wrapper,
            cursor="hand2",
            bd=1,
            text=text,
            relief=SOLID,
            image=botanika_photos[i],
            on_release_callback=check_position
        )
        lbl.place(x=randint(100, 350), y=randint(100, 350))
        draggable_lbls.append(lbl)

    def check_task():
        for el in draggable_lbls:
            el.config(bg=CONFIG["bg"]["ok"] if el.cget(
                "text") in valid_options else CONFIG["bg"]["error"])

        frm.after(100, lambda: show_message(
            len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frm, check_task, 5)


def task_2_1():
    global active_audio

    task_name = func_name()
    lbl_main.config(text=data.menu_buttons[1][1])
    task = data.content["anatomy"]["tasks"][0]
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"])
    make_label(frm, task["rule"], row=1,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    entry_answer = Entry(frm, font=font.Font(
        size=CONFIG["font_size"]["heading"]))
    entry_answer.grid(row=2, pady=10, sticky=EW)
    entry_answer.focus_set()

    opts_frm = Frame(frm, bg=CONFIG["bg"]["main"])
    opts_frm.grid(row=3)

    def btn_click(index):
        current_text = entry_answer.get()
        updated_text = f"{current_text} {index}"
        entry_answer.config(bg="white")
        entry_answer.delete(0, END)
        entry_answer.insert(0, updated_text)

    for (idx, option) in task["options"]:
        row_frame = Frame(opts_frm, bg=CONFIG["bg"]["main"])
        row_frame.grid(row=idx, sticky=EW)
        row_frame.columnconfigure(1, weight=1)

        Label(row_frame,
              text=f"{idx}.",
              width=2,
              borderwidth=1,
              relief=SOLID,
              font=font.Font(size=CONFIG["font_size"]["text"])).grid(sticky=NSEW, pady=5)

        Button(row_frame,
               text=f" {option}",
               anchor=W,
               relief=SOLID,
               activebackground="white",
               highlightthickness=1,
               bd=0,
               font=font.Font(size=CONFIG["font_size"]["text"]),
               command=lambda i=idx: btn_click(i)).grid(row=0, column=1, pady=5, sticky=EW)

    def check_task():
        result = entry_answer.get()
        formatted_result = ''.join(result.split())
        is_ok = formatted_result == task["answer"]

        entry_answer.config(
            bg=CONFIG["bg"]["ok"] if is_ok else CONFIG["bg"]["error"], fg="white")

        frm.after(100, lambda: show_message(is_ok))
        active_audio.destroy()

    make_check_result_button(frm, check_task, 5)


def task_2_2():
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[1][1])
    task = data.content["anatomy"]["tasks"][1]
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"])
    make_label(frm, task["rule"], row=1,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    frm_wrapper = Frame(frm,
                        height=650,
                        width=650,
                        bd=0)
    frm_wrapper.grid(row=2)

    make_image(frm_wrapper, resource_path(task["bg"]), 650, 650)

    valid_options = []
    draggable_labels = []

    def check_position(name, x, y):
        diff = 35
        match_option = [option for (
            n, option) in task["options"] if n == name][0]
        match_lbl = [
            btn for btn in draggable_labels if btn.cget("text") == name][0]

        if (abs(match_option["x"] - x)) < diff and abs(match_option["y"] - y) < diff:
            valid_options.append(match_lbl)
        elif match_lbl in valid_options:
            valid_options.remove(match_lbl)

    for idx, (name, _) in enumerate(task["options"]):
        draggable_label = DraggableWidget(
            frm_wrapper, cursor="hand2", relief=SOLID, bd=1, text=name, on_release_callback=check_position)
        draggable_label.place(x=5, y=5 + idx * 25)
        draggable_labels.append(draggable_label)

    def check_task():
        valid_element_names = [lbl.cget("text") for lbl in valid_options]
        for el in draggable_labels:
            el.config(bg=CONFIG["bg"]["ok"] if el.cget(
                "text") in valid_element_names else CONFIG["bg"]["error"])

        frm.after(100, lambda: show_message(
            len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frm, check_task, 5)
    make_link(frm, task, 6)


def task_2_3():
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[1][1])
    task = data.content["anatomy"]["tasks"][2]
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"])
    make_label(frm, task["rule"], row=1,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    container = Frame(frm, width=650,
                      height=475, bd=1, relief=SOLID)
    container.grid(sticky=EW)
    container.grid_propagate(False)
    frm.grid_rowconfigure(0, weight=1)
    frm.grid_columnconfigure(0, weight=1)
    frm.update_idletasks()

    frame_1 = Frame(container, bd=1, highlightthickness=5,
                    highlightbackground="white", relief=SOLID, height=250)
    frame_1.grid(row=2, sticky=EW)
    frame_1.grid_propagate(False)
    frame_2 = Frame(container, bd=1, highlightthickness=5,
                    highlightbackground="white", relief=SOLID, height=250)
    frame_2.grid(row=2, column=1, sticky=EW)
    frame_2.grid_propagate(False)
    frame_3 = Frame(container, bd=0, highlightthickness=0,
                    highlightbackground="white", height=250)
    frame_3.grid(row=3, columnspan=2, sticky=EW)
    frame_3.grid_propagate(False)

    for (element, coords) in task["elements"]:
        Label(container,
              relief=SOLID,
              bd=1,
              text=element).place(x=coords["x"], y=coords["y"])

    container.grid_rowconfigure(1, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(1, weight=1)
    container.grid_rowconfigure(2, weight=1)

    valid_options = []
    draggable_labels = []

    def check_position(name, x, y):
        value = get_value(name, task["options"])
        match_lbl = [
            lbl for lbl in draggable_labels if lbl.cget("text") == name][0]

        if ((x < task["answers"][0][0] and y < task["answers"][0][1] and value == task["elements"][0][0])
                or (x > task["answers"][1][0] and y < task["answers"][1][1] and value == task["elements"][1][0])):
            valid_options.append(match_lbl)
        elif match_lbl in valid_options:
            valid_options.remove(match_lbl)

    for (name, _) in task["options"]:
        draggable_label = DraggableWidget(
            container,
            cursor="hand2",
            relief=SOLID,
            font=font.Font(size=CONFIG["font_size"]["title"]),
            width=2,
            pady=2,
            padx=2,
            bd=1,
            text=name,
            on_release_callback=check_position)
        draggable_label.place(x=randint(10, 425), y=randint(275, 425))
        draggable_labels.append(draggable_label)

    def check_task():
        valid_element_names = [lbl.cget("text") for lbl in valid_options]
        for el in draggable_labels:
            el.config(bg=CONFIG["bg"]["ok"] if el.cget(
                "text") in valid_element_names else CONFIG["bg"]["error"])

        frm.after(100, lambda: show_message(
            len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frm, check_task, 5)
    make_link(frm, task, 6)


def task_3_1():
    global cytology_photos
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[2][1])
    task = data.content["cytology"]["tasks"][0]
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"])
    make_label(frm, task["rule"], row=1,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    frm_wrapper = Frame(frm, height=680, width=464, bd=0)
    frm_wrapper.grid(row=2)

    make_image(frm_wrapper, resource_path(task["bg"]), 464, 680, bg="white")

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    cytology_photos = [
        ImageTk.PhotoImage(PilImage.open(resource_path(img_path)))
        for img_path in image_paths
    ]

    draggable_texts = [name for (name, _) in task["options"]]
    draggable_lbls = []
    valid_options = []

    def check_position(name, x, y):
        value = get_value(name, task["options"])
        condition = x > task["answers"][0] and x < task["answers"][1] and y > task["answers"][2] and y < task["answers"][3]

        if (condition and value["required"] == True or (not condition and value["required"] == False)):
            if (name not in valid_options):
                valid_options.append(name)
        else:
            if (name in valid_options):
                valid_options.remove(name)

    for i, text in enumerate(draggable_texts):
        rand_x = randint(5, 310)
        rand_y = randint(460, 550)
        lbl = DraggableWidget(
            frm_wrapper,
            cursor="hand2",
            bd=1,
            text=text,
            bg=CONFIG["bg"]["main"],
            relief=SOLID,
            image=cytology_photos[i],
            on_release_callback=check_position
        )
        lbl.place(x=rand_x, y=rand_y)
        draggable_lbls.append(lbl)
        check_position(text, rand_x, rand_y)

    def check_task():
        for el in draggable_lbls:
            el.config(bg=CONFIG["bg"]["ok"] if el.cget(
                "text") in valid_options else CONFIG["bg"]["error"])

        frm.after(100, lambda: show_message(
            len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frm, check_task, 5)


def task_3_2():
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[2][1])
    task = data.content["cytology"]["tasks"][1]
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"], columnspan=4)
    make_label(frm, task["rule"], row=1, columnspan=4,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    choice_values = list(set(value for _, value in task["options"]))
    task_options = []

    for i, (name, answer) in enumerate(task["options"]):
        var = StringVar(value="")
        label = Label(frm,
                      text=name,
                      font=font.Font(size=CONFIG["font_size"]["text"]),
                      bg=CONFIG["bg"]["main"])
        label.grid(row=i+3, sticky=E)

        for j, choice in enumerate(choice_values):
            rad_button = Radiobutton(frm,
                                     text=choice,
                                     variable=var,
                                     value=choice,
                                     font=font.Font(
                                         size=CONFIG["font_size"]["text_small"]),
                                     bg=CONFIG["bg"]["main"])
            rad_button.grid(row=i+3, column=j+1)

        task_options.append((name, answer, var, label))

    def check_task():
        correct_answers = 0
        for _, correct, var, label in task_options:
            if var.get() == correct:
                label.config(bg=CONFIG["bg"]["ok"], fg="white")
                correct_answers += 1
            else:
                label.config(bg=CONFIG["bg"]["error"], fg="white")

        frm.after(100, lambda: show_message(
            correct_answers == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frm, check_task, i+3, pady=50, columnspan=4)


def task_3_3():
    global cytology_photos
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[2][1])
    task = data.content["cytology"]["tasks"][2]
    frm = frames[task_name]
    frm.grid()

    make_label(frm, task["name"])
    make_label(frm, task["rule"], row=1,
               font_size=CONFIG["font_size"]["text_small"])
    task_audio(task["audio"])

    frm_wrapper = Frame(frm, height=508, width=700, bd=0)
    frm_wrapper.grid(row=2)
    frm_wrapper.grid_propagate(0)

    frm_tips = Frame(frm_wrapper, highlightthickness=0, width=125, height=508)
    frm_tips.grid(column=2, sticky=E)
    frm_tips.grid_remove()

    make_image(frm_wrapper, resource_path(task["bg"]), 414, 508, bg="white")

    frm_wrapper.grid_columnconfigure(1, weight=1)
    frm_wrapper.grid_columnconfigure(2, weight=1)

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    cytology_photos = [
        ImageTk.PhotoImage(PilImage.open(resource_path(img_path)))
        for img_path in image_paths
    ]

    valid_options = []

    def check_position(name, x, y):
        diff = 5
        xx, yy = find_coordinates(task["options"], name)

        if (abs(xx - x) < diff and abs(yy - y) < diff):
            if (name not in valid_options):
                valid_options.append(name)
        else:
            if (name in valid_options):
                valid_options.remove(name)

    draggable_texts = [name for (name, _) in task["options"]]
    draggable_lbs = []
    for i, text in enumerate(draggable_texts):
        lbl = DraggableWidget(
            frm_wrapper,
            cursor="hand2",
            text=text,
            bd=0,
            image=cytology_photos[i],
            on_release_callback=check_position
        )
        lbl.place(x=randint(20, 160), y=randint(70, 260))
        draggable_lbs.append(lbl)

    for (name, option_config) in task["options"]:
        Label(frm_tips, text=f"<-- {name}").place(x=0,
                                                  y=option_config["hint_y"])

    def check_task():
        border_width = 4
        for el in draggable_lbs:
            x = el.winfo_x()
            y = el.winfo_y()
            el.config(bd=border_width, bg=CONFIG["bg"]["ok"] if el.cget(
                "text") in valid_options else CONFIG["bg"]["error"])
            el.place(x=x-border_width, y=y-border_width)

        frm.after(100, lambda: show_message(
            len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frm, check_task, 5)

    def show_tips():
        frm_tips.grid()
        btn_tip.grid_remove()
        frm_tips.after(5000, frm_tips.grid_remove)

    btn_tip = Button(frm,
                     text="Показать подсказку на 5 секунд",
                     highlightbackground=CONFIG["bg"]["main"],
                     command=show_tips)
    btn_tip.grid()


if __name__ == "__main__":
    left_panel_ui()
    landing(frm_landing)
    window.mainloop()
