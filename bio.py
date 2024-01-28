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

frame_ids = ["botanika", "anatomy", "cytology", "task_1_1", "task_1_2", "task_1_3",
             "task_2_1", "task_2_2", "task_2_3", "task_3_1", "task_3_2", "task_3_3", "result"]
tasks = ["task_1_1", "task_1_2", "task_1_3", "task_2_1",
         "task_2_2", "task_2_3", "task_3_1", "task_3_2", "task_3_3", "landing_result"]

total_tasks = sum(len(cat["tasks"]) for cat in data.content.values())
active_task_number = 0
score = 0
active_audio = None


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

    if btn_home is None:
        make_home_btn()

    if active_audio is not None:
        active_audio.destroy()


def reset_score():
    global score
    global active_task_number

    score = 0
    active_task_number = 0
    lbl_score.config(text=f"{score}/{total_tasks}")


def increase_score():
    global score

    score += 1
    lbl_score.config(text=f"{score}/{total_tasks}")


def go_home():
    global btn_home
    global score

    frm_landing.grid()
    for frame_id in frame_ids:
        clear_frame_content(frames[frame_id])
    clear_frame_content(btn_home)

    lbl_main.config(text=data.project_title)
    btn_home = None
    lbl_score.config(text="")

    if active_audio is not None:
        active_audio.destroy()

    for btn in menu_btns:
        btn.config(highlightbackground=CONFIG["bg"]["main"])


def left_panel_ui():
    global menu_btns
    global btn_home
    global frm_menu_buttons
    global lbl_score

    frm_panel = Frame(window, bg=CONFIG["bg"]["main"], relief=RAISED, bd=2)
    frm_panel.grid(row=0, sticky=NSEW)
    frm_panel.rowconfigure(2, weight=1)

    Label(frm_panel, text="Выберите раздел:",
          bg=CONFIG["bg"]["main"]).grid(padx=5, pady=(25, 5))
    frm_menu_buttons = Frame(frm_panel, bg=CONFIG["bg"]["main"])
    frm_menu_buttons.grid(row=1, padx=10)

    menu_btns = []

    for idx, (slug, name, _) in enumerate(data.menu_buttons):
        btn_menu = Button(frm_menu_buttons,
                          text=name,
                          highlightbackground=CONFIG["bg"]["main"],
                          font=font.Font(size=CONFIG["font_size"]["title"]),
                          command=lambda slug=slug, name=name: choose_topic(slug, name))
        btn_menu.grid(row=idx, pady=5, sticky=EW)
        menu_btns.append(btn_menu)

    btn_home = None

    Label(frm_panel,
          text=data.copyrights,
          bg=CONFIG["bg"]["main"],
          font=font.Font(size=10)).grid(row=2, sticky=N)

    lbl_score = Label(window, text="",
                      font=font.Font(size=CONFIG["font_size"]["heading"]),
                      bg=CONFIG["bg"]["main"])
    lbl_score.place(x=50, y=400)

    make_image(window, "images/sunflower.png", 125, 142, x=18, y=840)


frm_main = Frame(bg=CONFIG["bg"]["main"])
frm_main.grid(column=1, sticky=NSEW)
frm_main.columnconfigure(0, weight=1)
lbl_main = Label(frm_main,
                 text=data.project_title,
                 bg=CONFIG["bg"]["main"],
                 font=font.Font(size=CONFIG["font_size"]["heading"]))
lbl_main.grid(columnspan=3, pady=(20, 20), sticky=EW)
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
          text="Выберите раздел для ознакомления или нажмите \"Начать игру\"",
          font=font.Font(size=CONFIG["font_size"]["title"]),
          bg=CONFIG["bg"]["main"]).grid(pady=(0, 10), columnspan=4)

    for idx, (slug, name, frm_img) in enumerate(data.menu_buttons):
        frm = Frame(frame, borderwidth=2, relief=GROOVE, cursor="hand2")
        frm.grid(row=1, column=idx, padx=10, pady=10)
        image = PhotoImage(file=frm_img)
        lbl_image = Label(frm, image=image)
        lbl_image.image = image
        lbl_image.grid()
        lbl_image.bind("<Button-1>", lambda _, slug=slug,
                       name=name: choose_topic(slug, name))
        Label(frm, text=name).grid(row=1)

    lbl_start = Label(frame,
                      text="Начать игру",
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

    get_page_title(frames[topic_name], info["intro"])

    for i, detail in enumerate(info["details"]):
        Label(frames[topic_name],
              bg=CONFIG["bg"]["main"],
              wraplength=600,
              text=detail,
              font=font.Font(size=CONFIG["font_size"]["text"])).grid(row=i+1, pady=(0, 10))

    make_image(frames[topic_name], info["preview"]["img_path"],
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

    make_image(frames["result"], result["msg_image_path"], 600, 600, row=3)

    MusicPlayer(frm_main, result["msg_audio_path"], autoplay=True)


def task_audio(audio):
    global active_audio
    player = MusicPlayer(frm_main, audio, autoplay=True)
    player.make_button(x=775, y=10)
    active_audio = player


def task_1_1():

    task_name = func_name()
    row_entries = []
    task = data.content["botanika"]["tasks"][0]
    lbl_main.config(text=data.menu_buttons[0][1])
    frames[task_name].grid()

    get_page_title(frames[task_name], task["name"])
    task_audio(task["audio"])

    frm_options = make_frame(task_name, 1)
    frm_task = make_frame(task_name, 2)

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
        entry.grid(row=3, column=i, pady=15)
        row_entries.append(entry)
    row_entries[0].focus_set()

    def check_task():
        result = ""
        for i, variant in enumerate(row_entries):
            result += variant.get()
            variant.config(bg=CONFIG["bg"]["ok"] if variant.get(
            ) == task["answer"][i] else CONFIG["bg"]["error"], fg="white")

        frames[task_name].after(
            100, lambda: show_message(result == task["answer"]))
        active_audio.destroy()

    make_check_result_button(frames[task_name], check_task, 4)


def task_1_2():
    global active_audio

    task_name = func_name()
    answers = []
    keyword = []
    KEYWORD_COLUMN = 8
    task = data.content["botanika"]["tasks"][1]
    lbl_main.config(text=data.menu_buttons[0][1])
    frames[task_name].grid()

    get_page_title(frames[task_name], task["name"])
    task_audio(task["audio"])

    frm_options = make_frame(task_name, 1)
    frm_crossword = make_frame(task_name, 2, 20)

    for i, option in enumerate(task["options"]):
        Label(frm_options,
              anchor=W,
              wraplength=750,
              bg=CONFIG["bg"]["main"],
              width=75,
              text=f"{i+1}. {option["question"]}").grid(row=i)

    for row, option in enumerate(task["options"]):
        for i in range(0, option["padLeft"]):
            Label(frm_crossword, width=2, bg=CONFIG["bg"]["main"]).grid(
                row=row+3, column=i)

        Label(frm_crossword, width=2, text=row+1,
              bd=1, highlightthickness=1, relief=SOLID).grid(row=row+2, column=option["padLeft"])

        row_entries = []

        for i in range(option["padLeft"] + 1, option["padLeft"] + 1 + len(option["answer"])):
            var = StringVar()
            var.trace_add("write", lambda *args,
                          var=var: check_only_letter(var))
            entry = Entry(frm_crossword,
                          bg="yellow" if i == KEYWORD_COLUMN else "white",
                          width=2,
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
                if (entry.get() != task["options"][i]["answer"][k]):
                    entry.config(bg=CONFIG["bg"]["error"], fg="white")
                    valid = False
                else:
                    entry.config(bg=CONFIG["bg"]["ok"], fg="white")

        word = "".join(char.get() for char in keyword)

        frames[task_name].after(
            100, lambda: show_message(word == task["answer"]))
        active_audio.destroy()

    make_check_result_button(frames[task_name], check_task, 20)


def task_1_3():
    global botanika_photos
    global active_audio

    task_name = func_name()
    lbl_main.config(text=data.menu_buttons[0][1])
    task = data.content["botanika"]["tasks"][2]
    frames[task_name].grid()

    get_page_title(frames[task_name], task["name"])
    task_audio(task["audio"])

    frm_wrapper = Frame(frames[task_name],
                        height=650,
                        width=650,
                        bd=0)
    frm_wrapper.grid(row=1)

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    botanika_photos = [
        ImageTk.PhotoImage(PilImage.open(img_path))
        for img_path in image_paths
    ]

    draggable_texts = [name for (name, _) in task["options"]]

    make_image(frm_wrapper, task["bg"], 650, 650, bg="white")

    valid_options = []

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

        frames[task_name].after(
            100, lambda: show_message(len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frames[task_name], check_task, 20)


def task_2_1():
    global active_audio

    task_name = func_name()
    lbl_main.config(text=data.menu_buttons[1][1])
    task = data.content["anatomy"]["tasks"][0]
    frames[task_name].grid()

    get_page_title(frames[task_name], task["name"])
    task_audio(task["audio"])

    entry_answer = Entry(frames[task_name], font=font.Font(
        size=CONFIG["font_size"]["title"]))
    entry_answer.grid(row=1, pady=10, sticky=EW)
    entry_answer.focus_set()

    def btn_click(index):
        current_text = entry_answer.get()
        updated_text = f"{current_text} {index}"
        entry_answer.config(bg="white")
        entry_answer.delete(0, END)
        entry_answer.insert(0, updated_text)

    for (idx, option) in task["options"]:
        row_frame = Frame(frames[task_name], bg=CONFIG["bg"]["main"])
        row_frame.grid(row=idx+1, sticky=EW)
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
               highlightthickness=0,
               bd=0,
               font=font.Font(size=CONFIG["font_size"]["text"]),
               command=lambda i=idx: btn_click(i)).grid(row=0, column=1, pady=5, sticky=EW)

    def check_task():
        result = entry_answer.get()
        formatted_result = ''.join(result.split())
        is_ok = formatted_result == task["answer"]

        entry_answer.config(
            bg=CONFIG["bg"]["ok"] if is_ok else CONFIG["bg"]["error"], fg="white")

        frames[task_name].after(100, lambda: show_message(is_ok))
        active_audio.destroy()

    make_check_result_button(frames[task_name], check_task, 10)


def task_2_2():
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[1][1])
    task = data.content["anatomy"]["tasks"][1]
    frames[task_name].grid()

    get_page_title(frames[task_name], task["name"])
    task_audio(task["audio"])

    frm_wrapper = Frame(frames[task_name],
                        height=650,
                        width=650,
                        bd=0)
    frm_wrapper.grid(row=1)

    make_image(frm_wrapper, task["bg"], 650, 650)

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
            frames[task_name], cursor="hand2", relief=SOLID, bd=1, text=name, on_release_callback=check_position)
        draggable_label.place(x=5, y=50 + idx * 25)
        draggable_labels.append(draggable_label)

    def check_task():
        valid_element_names = [lbl.cget("text") for lbl in valid_options]
        for el in draggable_labels:
            el.config(bg=CONFIG["bg"]["ok"] if el.cget(
                "text") in valid_element_names else CONFIG["bg"]["error"])

        frames[task_name].after(
            100, lambda: show_message(len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frames[task_name], check_task, 2)
    make_link(frames[task_name], task, 3)


def task_2_3():
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[1][1])
    frames[task_name].grid()
    task = data.content["anatomy"]["tasks"][2]

    get_page_title(frames[task_name], task["name"])
    task_audio(task["audio"])

    container = Frame(frames[task_name], height=300, bd=2, relief=SOLID)
    container.grid(sticky=EW)
    frames[task_name].grid_rowconfigure(0, weight=1)
    frames[task_name].grid_columnconfigure(0, weight=1)
    frames[task_name].update_idletasks()

    Frame(container, bd=2, highlightthickness=5,
          highlightbackground="white", relief=SOLID, height=250).grid(row=1, sticky=EW)
    Frame(container, bd=2, highlightthickness=5,
          highlightbackground="white", relief=SOLID, height=250).grid(row=1, column=1, sticky=EW)
    Frame(container, bd=0, highlightthickness=0,
          highlightbackground="white", height=250).grid(row=2, columnspan=2, sticky=EW)

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

        frames[task_name].after(
            100, lambda: show_message(len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frames[task_name], check_task, 3)
    make_link(frames[task_name], task, 4)


def task_3_1():
    global cytology_photos
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[2][1])
    task = data.content["cytology"]["tasks"][0]

    frames[task_name].grid()

    get_page_title(frames[task_name], task["name"])
    task_audio(task["audio"])

    frm_wrapper = Frame(frames[task_name], height=750, width=464, bd=0)
    frm_wrapper.grid(row=1)

    make_image(frm_wrapper, task["bg"], 464, 750, bg="white")

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    cytology_photos = [
        ImageTk.PhotoImage(PilImage.open(img_path))
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
        rand_y = randint(460, 600)
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

        frames[task_name].after(
            100, lambda: show_message(len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frames[task_name], check_task, 2)


def task_3_2():
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[2][1])
    task = data.content["cytology"]["tasks"][1]
    frames[task_name].grid()

    get_page_title(frames[task_name], task["name"], columnspan=4)
    task_audio(task["audio"])

    choice_values = list(set(value for _, value in task["options"]))
    task_options = []

    for i, (name, answer) in enumerate(task["options"]):
        var = StringVar(value="")
        label = Label(frames[task_name],
                      text=name,
                      font=font.Font(size=CONFIG["font_size"]["text"]),
                      bg=CONFIG["bg"]["main"])
        label.grid(row=i+1, sticky=E)

        for j, choice in enumerate(choice_values):
            rad_button = Radiobutton(frames[task_name],
                                     text=choice,
                                     variable=var,
                                     value=choice,
                                     bg=CONFIG["bg"]["main"])
            rad_button.grid(row=i+1, column=j+1)

        task_options.append((name, answer, var, label))

    def check_task():
        correct_answers = 0
        for _, correct, var, label in task_options:
            if var.get() == correct:
                label.config(bg=CONFIG["bg"]["ok"], fg="white")
                correct_answers += 1
            else:
                label.config(bg=CONFIG["bg"]["error"], fg="white")

        frames[task_name].after(
            100, lambda: show_message(correct_answers == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(
        frames[task_name], check_task, i+2, pady=50, columnspan=4)


def task_3_3():
    global cytology_photos
    global active_audio
    task_name = func_name()

    lbl_main.config(text=data.menu_buttons[2][1])
    task = data.content["cytology"]["tasks"][2]
    frames[task_name].grid()

    get_page_title(frames[task_name], task["name"])
    task_audio(task["audio"])

    frm_wrapper = Frame(frames[task_name], height=508, width=700, bd=0)
    frm_wrapper.grid(row=1)
    frm_wrapper.grid_propagate(0)

    frm_tips = Frame(frm_wrapper, highlightthickness=0, width=125, height=508)
    frm_tips.grid(column=2, sticky=E)
    frm_tips.grid_remove()

    make_image(frm_wrapper, task["bg"], 414, 508, bg="white")

    frm_wrapper.grid_columnconfigure(1, weight=1)
    frm_wrapper.grid_columnconfigure(2, weight=1)

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    cytology_photos = [
        ImageTk.PhotoImage(PilImage.open(img_path))
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

        frames[task_name].after(
            100, lambda: show_message(len(valid_options) == len(task["options"])))
        active_audio.destroy()

    make_check_result_button(frames[task_name], check_task, 3)

    def show_tips():
        frm_tips.grid()
        btn_tip.grid_remove()
        frm_tips.after(5000, frm_tips.grid_remove)

    btn_tip = Button(frames[task_name],
                     text="Показать подсказку на 5 секунд",
                     highlightbackground=CONFIG["bg"]["main"],
                     command=show_tips)
    btn_tip.grid()


if __name__ == "__main__":
    left_panel_ui()
    landing(frm_landing)
    window.mainloop()
