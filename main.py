import data
import webbrowser
import sys
import os

from random import randint
from tkinter import *
from tkinter import font, messagebox
from PIL import Image as PilImage, ImageTk

from utils import *
from draggable import DraggableWidget


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


TITLE = data.project_title


window = Tk()
window_width = 1000
window_height = 1000
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
window.resizable(0, 0)
window.title(TITLE)
window.rowconfigure(0, minsize=1000, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

CONFIG = {
    "bg": "lightgreen",
    "font_size": {
        "heading": font.Font(size=38),
        "title": font.Font(size=20),
        "text": font.Font(size=16)
    }
}

tasks = ["task_1_1", "task_1_2", "task_1_3", "task_2_1",
         "task_2_2", "task_2_3", "task_3_1", "task_3_2", "task_3_3", "landing_result"]


def choose_topic(slug, name):
    global active_task_number
    global btn_home
    global score
    for btn in menu_btns:
        btn.config(highlightbackground=CONFIG["bg"], fg="black")
    btn_index = [index for index, (slug_name, _, _) in enumerate(
        data.menu_buttons) if slug_name == slug]

    btn = menu_btns[btn_index[0]]
    btn.config(highlightbackground="green", fg="green")

    lbl_main.config(text=name)

    frm_landing.grid_remove()
    for frame_id in frame_ids:
        clear_frame_content(frames[frame_id])

    landing_by_topic(slug)

    if btn_home is None:
        btn_home = Button(frm_menu_buttons,
                          text="🏠",
                          cursor="hand2",
                          highlightbackground=CONFIG["bg"],
                          font=CONFIG["font_size"]["title"],
                          command=go_home)
        btn_home.grid(row=5, column=0, pady=5, sticky=EW)

    active_task_number = 0
    # TODO: reset score
    score = 0


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
    lbl_main.config(text=TITLE)
    btn_home = None

    for btn in menu_btns:
        btn.config(highlightbackground=CONFIG["bg"], fg="black")


def left_panel_ui():
    global menu_btns
    global btn_home
    global frm_panel
    global frm_menu_buttons
    global lbl_score
    global score
    frm_panel = Frame(window, bg=CONFIG["bg"], relief=RAISED, bd=2)
    frm_panel.grid(row=0, column=0, sticky=NSEW)
    frm_panel.rowconfigure(2, weight=1)

    print(score)

    lbl_panel = Label(frm_panel, text="Выберите раздел:",
                      bg=CONFIG["bg"], fg="black")
    lbl_panel.grid(row=0, column=0, padx=5, pady=1)
    frm_menu_buttons = Frame(frm_panel, bg=CONFIG["bg"])
    frm_menu_buttons.grid(row=1, column=0, padx=10)

    menu_btns = []

    for idx, (slug, name, _) in enumerate(data.menu_buttons):
        btn_menu = Button(frm_menu_buttons,
                          text=name,
                          cursor="hand2",
                          highlightbackground=frm_panel.cget("bg"),
                          font=CONFIG["font_size"]["title"],
                          command=lambda slug=slug, name=name: choose_topic(slug, name))
        btn_menu.grid(row=idx, column=0, pady=5, sticky=EW)
        menu_btns.append(btn_menu)

    btn_home = None

    frm_copyrights = Frame(frm_panel, bg=frm_panel.cget("bg"))
    frm_copyrights.grid(row=2, column=0, sticky=N)

    lbl_copyrights = Label(frm_copyrights, text=data.copyrights, bg=frm_panel.cget(
        "bg"), fg="black", font=font.Font(size=10))
    lbl_copyrights.grid(row=0, column=0)

    lbl_score = Label(frm_panel, text=f"{
                      score}/{total_tasks}", font=font.Font(size=30), bg=CONFIG["bg"], fg="black")
    lbl_score.grid(row=3, column=0, padx=5, pady=1)

    # TODO: Add Sunflower image
    # tk_image = PhotoImage(file=resource_path("images/sunflower.png"))
    # lbl_image = Label(frm_panel, image=tk_image, bg=CONFIG["bg"])
    # lbl_image.image = tk_image
    # lbl_image.grid(row=10, column=0)


frm_main = Frame(bg=CONFIG["bg"])
frm_main.grid(row=0, column=1, sticky=NSEW)
frm_main.columnconfigure(0, weight=1)
lbl_main = Label(frm_main, text=TITLE, bg=CONFIG["bg"], fg="black",
                 font=CONFIG["font_size"]["heading"], anchor="center")
lbl_main.grid(row=0, column=0, columnspan=3, pady=(20, 20), sticky=EW)
frm_content = Frame(frm_main, padx=5, pady=5, bg=CONFIG["bg"])
frm_content.grid(row=1, column=0)
frm_landing = Frame(frm_content, bg=CONFIG["bg"])
frm_landing.grid(row=0, column=0)

frames = {}
frame_ids = ["botanika", "anatomy", "cytology", "1_1", "1_2", "1_3",
             "2_1", "2_2", "2_3", "3_1", "3_2", "3_3", "result"]
for frame_id in frame_ids:
    frame = Frame(frm_content, bg=CONFIG["bg"])
    frame.grid(row=0, column=0)
    frames[frame_id] = frame


total_tasks = sum(len(cat["tasks"]) for cat in data.content.values())
active_task_number = 0
score = 0


def start_game():
    frm_landing.grid_remove()
    for frame_id in frame_ids:
        clear_frame_content(frames[frame_id])
    print(active_task_number)
    globals()[tasks[active_task_number]]()


def next_task():
    global active_task_number
    active_task_number += 1

    frm_landing.grid_remove()
    for frame_id in frame_ids:
        clear_frame_content(frames[frame_id])
    globals()[tasks[active_task_number]]()


def get_page_title(frame, text, columnspan=1):
    Label(frame, anchor=W, wraplength=600,
          bg=CONFIG["bg"],
          fg="black",
          font=CONFIG["font_size"]["title"],
          text=text).grid(row=0, column=0, pady=(0, 15), columnspan=columnspan)


def landing(frame):
    lbl_landing = Label(frame,
                        text="Выберите раздел",
                        font=CONFIG["font_size"]["title"],
                        bg=CONFIG["bg"],
                        fg="black")
    lbl_landing.grid(row=0, column=0, pady=(0, 10), columnspan=4)

    for idx, (slug, name, frm_img) in enumerate(data.menu_buttons):
        frm = Frame(frame, borderwidth=2, relief=GROOVE, cursor="hand2")
        frm.grid(row=1, column=idx, padx=10, pady=10)
        image = PhotoImage(file=resource_path(frm_img))
        lbl_image = Label(frm, image=image)
        lbl_image.image = image
        lbl_image.grid(row=0, column=0)
        lbl_image.bind("<Button-1>", lambda _,
                       slug=slug, name=name: choose_topic(slug, name))
        lbl_text = Label(frm, text=name)
        lbl_text.grid(row=1, column=0)
        lbl_text.bind("<Button-1>", lambda _,
                      slug=slug, name=name: choose_topic(slug, name))

    lbl_start = Label(frame, text="Начать путешествие", font=font.Font(size=32), anchor=CENTER,
                      cursor="hand2", bg="darkblue", borderwidth=2, relief=GROOVE, height=6, justify=CENTER)
    lbl_start.grid(row=2, column=0, columnspan=4, padx=10, pady=50, sticky=EW)
    lbl_start.bind("<Button-1>", lambda _: start_game())


def landing_by_topic(topic_name):
    frames[topic_name].grid()
    info = data.content[topic_name]

    get_page_title(frames[topic_name], info["intro"])

    for i, detail in enumerate(info["details"]):
        Label(frames[topic_name], bg=CONFIG["bg"], fg="black", wraplength=600,
              text=detail, font=CONFIG["font_size"]["text"]).grid(row=i+1, column=0, pady=10)


def landing_result():
    frames["result"].grid()
    get_page_title(frames["1_1"], "Вы выполнили все задания.")
    Label(frames["result"], bg=CONFIG["bg"], fg="black", wraplength=600,
          text=f"Ваш результат: {score}/{total_tasks}", font=CONFIG["font_size"]["title"]).grid(row=1, column=0)


def task_1_1():
    task = data.content["botanika"]["tasks"][0]
    frames["1_1"].grid()

    get_page_title(frames["1_1"], task["name"])

    frm_options = Frame(frames["1_1"], bg=CONFIG["bg"])
    frm_options.grid(row=1, column=0)

    for i, option in enumerate(task["options"]):
        lbl_option = Label(frm_options, anchor=W, wraplength=750,
                           bg=CONFIG["bg"],
                           fg="black",
                           font=CONFIG["font_size"]["text"],
                           text=f"{option[0]}. {option[1]}")
        lbl_option.grid(row=i, column=0)

    frm_task = Frame(frames["1_1"], bg=CONFIG["bg"])
    frm_task.grid(row=2, column=0, pady=20)

    row_entries = []

    for i in range(len(task["answer"])):
        var = StringVar()
        var.trace_add("write", lambda *args, var=var: check_only_digit(var))
        entry = Entry(frm_task, bg="white", fg="black", font=font.Font(size=48), width=2, highlightthickness=1,
                      highlightbackground="white", bd=2, justify="center", relief=SOLID, textvariable=var)
        entry.grid(row=3, column=i)
        row_entries.append(entry)

        def check_task():
            result = ""
            for i, variant in enumerate(row_entries):
                result += variant.get()
                if (variant.get() != task["answer"][i]):
                    variant.config(bg="red", fg="white")
                else:
                    variant.config(bg="green", fg="white")

            def show_message():
                if (result == task["answer"]):
                    messagebox.showinfo(
                        "Задание пройдено!", "Вы набрали +1 бал и готовы к выполнению следующего задания")
                    increase_score()
                else:
                    messagebox.showerror("Задание пройдено с ошибкой!",
                                         "Вы ошиблись при выполнении задания и не набрали 1 бал. Переходим к выполнению следующего задания")
                next_task()

            frames["1_1"].after(100, show_message)

    check_result_button = Button(
        frames["1_1"], text="Проверить результат", font=CONFIG["font_size"]["title"], cursor="hand2", command=check_task)
    check_result_button.grid(row=4, column=0, pady=10, sticky=EW)


def task_1_2():
    task = data.content["botanika"]["tasks"][1]
    frames["1_2"].grid()

    get_page_title(frames["1_2"], task["name"])

    frm_crossword_questions = Frame(frames["1_2"], bg=CONFIG["bg"])
    frm_crossword_questions.grid(row=1, column=0)

    for i, option in enumerate(task["options"]):
        lbl_crossword_question = Label(frm_crossword_questions, anchor=W, wraplength=750,
                                       bg=CONFIG["bg"],
                                       fg="black",
                                       width=75,
                                       text=f"{i+1}. {option["question"]}")
        lbl_crossword_question.grid(row=i, column=0)

    frm_crossword = Frame(frames["1_2"], bg=CONFIG["bg"])
    frm_crossword.grid(row=2, column=0, pady=20)

    crossword_answers = []
    crossword_keyword = []

    def check_crossword():
        valid = True
        for i, crossword_answer in enumerate(crossword_answers):
            result = ""
            for k, entry in enumerate(crossword_answer):
                result += entry.get()
                if (entry.get() != task["options"][i]["answer"][k]):
                    entry.config(bg="red", fg="white")
                    valid = False
                else:
                    entry.config(bg="green", fg="white")

        keyword = ""
        for char in crossword_keyword:
            keyword += char.get()

        if (keyword == task["answer"] and valid):
            messagebox.showinfo("Кроссворд разгадан",
                                "Поздравляю, вы разгадали кроссворд верно!")

    for row, option in enumerate(task["options"]):
        for i in range(0, option["padLeft"]):
            label = Label(frm_crossword, width=2, bg=frm_panel.cget("bg"))
            label.grid(row=row+3, column=i)

        label = Label(frm_crossword, width=2, text=row+1, bg="white",
                      fg="black", bd=1, highlightthickness=1, relief=SOLID)
        label.grid(row=row+2, column=option["padLeft"])

        row_entries = []

        for i in range(option["padLeft"]+1, option["padLeft"]+1 + len(option["answer"])):
            var = StringVar()
            var.trace_add("write", lambda *args,
                          var=var: check_only_letter(var))
            entry = Entry(frm_crossword, bg="yellow" if i == 8 else "white", fg="black",
                          width=2, highlightthickness=1, highlightbackground="white", bd=1, justify="center", relief=SOLID, textvariable=var)
            entry.grid(row=row+2, column=i)
            row_entries.append(entry)
            if (i == 7):
                crossword_keyword.append(entry)

        crossword_answers.append(row_entries)

    check_result_button = Button(
        frames["1_2"], text="Проверить результат", font=CONFIG["font_size"]["title"], cursor="hand2", command=check_crossword)
    check_result_button.grid(row=20, column=0, pady=10, sticky=EW)


def task_1_3():
    global botanika_photo_1_3_0
    global botanika_photos
    task = data.content["botanika"]["tasks"][2]

    frames["1_3"].grid()

    get_page_title(frames["1_3"], task["name"])

    frm_wrapper = Frame(frames["1_3"],
                        bg="white", height=650, width=650, bd=0)
    frm_wrapper.grid(row=1, column=0)
    frm_wrapper.grid_propagate(0)

    canvas = Canvas(frm_wrapper, width=650, height=650,
                    bg="white", highlightthickness=0)
    canvas.grid(row=0, column=0)

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    botanika_photos = [
        ImageTk.PhotoImage(PilImage.open(img_path))
        for img_path in image_paths
    ]

    draggable_texts = [name for (name, _) in task["options"]]

    img0 = PilImage.open(task["bg"])
    botanika_photo_1_3_0 = ImageTk.PhotoImage(img0)
    canvas.create_image(0, 0, anchor=NW, image=botanika_photo_1_3_0)

    valid_options = []

    def check_position(name, x, y):
        diff = 25
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
            frm_wrapper, cursor="hand2", bd=1, text=text,
            bg="white", relief=SOLID,
            image=botanika_photos[i],
            on_release_callback=check_position
        )
        lbl.place(x=randint(100, 350), y=randint(100, 350))
        draggable_lbls.append(lbl)

    def check_result():
        for el in draggable_lbls:
            if (el.cget("text") in valid_options):
                el.config(bg="green")
            else:
                el.config(bg="red")

        if (len(valid_options) == len(task["options"])):
            messagebox.showinfo(
                "Задание пройдено!", "Вы набрали +1 бал и готовы к выполнению следующего задания")
            increase_score()
        else:
            messagebox.showerror("Задание пройдено с ошибкой!",
                                 "Вы ошиблись при выполнении задания и не набрали 1 бал. Переходим к выполнению следующего задания")

    check_result_button = Button(
        frames["1_3"], text="Проверить результат", font=CONFIG["font_size"]["title"], cursor="hand2", command=check_result)
    check_result_button.grid(row=20, column=0, pady=10, sticky=EW)


def task_2_1():
    global entry_answer
    task = data.content["anatomy"]["tasks"][0]
    frames["2_1"].grid()

    get_page_title(frames["2_1"], task["name"])

    entry_answer = Entry(frames["2_1"], bg="white",
                         fg="black", font=CONFIG["font_size"]["title"])
    entry_answer.grid(row=1, column=0, pady=10, sticky=EW)

    def task_2_1_btn_click(index):
        current_text = entry_answer.get()
        updated_text = f"{current_text} {index}"
        entry_answer.config(bg="white", fg="black")
        entry_answer.delete(0, END)
        entry_answer.insert(0, updated_text)

    for (idx, option) in task["options"]:
        row_frame = Frame(frames["2_1"], bg="white")
        row_frame.grid(row=idx+1, column=0, sticky=EW)
        row_frame.columnconfigure(1, weight=1)

        label = Label(row_frame, text=f"{idx}.", bg="white",
                      fg="black", font=font.Font(size=18))
        label.grid(row=0, column=0, sticky="w")

        button = Button(row_frame,
                        text=option,
                        cursor="hand2",
                        anchor=W,
                        bg="white",
                        fg="black",
                        borderwidth=0,
                        font=font.Font(size=16),
                        command=lambda i=idx: task_2_1_btn_click(i))
        button.grid(row=0, column=1, padx=(5, 0), sticky=EW)

    def check_result():
        result = entry_answer.get()
        formatted_result = ''.join(result.split())

        if formatted_result == task["answer"]:
            entry_answer.config(bg="green", fg="white")
        else:
            entry_answer.config(bg="red", fg="white")

    check_result_button = Button(
        frames["2_1"], text="Проверить результат", font=CONFIG["font_size"]["title"], cursor="hand2", command=check_result)
    check_result_button.grid(row=10, column=0, pady=10, sticky=EW)


def task_2_2():
    task = data.content["anatomy"]["tasks"][1]
    frames["2_2"].grid()

    get_page_title(frames["2_2"], task["name"])

    tk_image = PhotoImage(file=resource_path("images/eye_350.png"))
    lbl_image = Label(frames["2_2"], image=tk_image)
    lbl_image.image = tk_image
    lbl_image.grid(row=1, column=0)

    # TODO: Implement
    def check_result():
        pass

    def check_position(name, x, y):
        diff = 25
        match_option = [option for (
            n, option) in task["options"] if n == name][0]
        match_btn = [
            btn for btn in draggable_labels if btn.cget("text") == name][0]

        # TODO: Update coords
        if (abs(match_option["x"] - x)) < diff and abs(match_option["y"] - y) < diff:
            match_btn.config(highlightbackground="green", fg="green")
        else:
            match_btn.config(highlightbackground="red", fg="red")

    draggable_labels = []
    for idx, (name, _) in enumerate(task["options"]):
        draggable_label = DraggableWidget(
            frames["2_2"], cursor="hand2", relief=RAISED, bd=1, bg="#666", fg="white", text=name, on_release_callback=check_position)
        draggable_label.place(x=5, y=50 + idx * 25)
        draggable_labels.append(draggable_label)

    check_result_button = Button(
        frames["2_2"], text="Проверить результат", font=CONFIG["font_size"]["title"], command=check_result)
    check_result_button.grid(row=2, column=0, pady=10, sticky=EW)

    link_label = Label(
        frames["2_2"], text="Узнать больше на Youtube.com", bg="#333", fg=CONFIG["bg"], cursor="hand2")
    link_label.grid(row=3, column=0, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open(task["meta"]["youtube"]))


def task_2_3():
    frames["2_3"].grid()

    task = data.content["anatomy"]["tasks"][2]

    get_page_title(frames["2_3"], task["name"])

    container = Frame(frames["2_3"], height=300)
    container.grid(sticky=EW)
    frames["2_3"].grid_rowconfigure(0, weight=1)
    frames["2_3"].grid_columnconfigure(0, weight=1)
    frames["2_3"].update_idletasks()

    frame1 = Frame(container, bg="white", bd=3, highlightthickness=5,
                   highlightbackground="white", relief=SOLID, height=250)
    frame2 = Frame(container, bg="white", bd=3, highlightthickness=5,
                   highlightbackground="white", relief=SOLID, height=250)
    frame3 = Frame(container, bg="white", bd=0, highlightthickness=0,
                   highlightbackground="white", height=250)

    frame1.grid(row=1, column=0, sticky=EW)
    frame2.grid(row=1, column=1, sticky=EW)
    frame3.grid(row=2, column=0, columnspan=2, sticky=EW)

    Label(container, relief=SOLID, bd=1, bg="white",
          fg="black", text="Микроэлементы").place(x=55, y=10)
    Label(container, relief=SOLID, bd=1, bg="white",
          fg="black", text="Макроэлементы").place(x=280, y=10)

    container.grid_rowconfigure(1, weight=1)
    container.grid_columnconfigure(0, weight=1)
    container.grid_columnconfigure(1, weight=1)
    container.grid_rowconfigure(2, weight=1)

    all_elements = []
    valid_elements = []

    def check_position(name, x, y):
        value = get_value(name, task["options"])
        match_lbl = [
            lbl for lbl in draggable_labels if lbl.cget("text") == name][0]
        all_elements.append(match_lbl)

        if ((x < 190 and y < 215 and value == "микроэлемент") or (x > 230 and y < 215 and value == "макроэлемент")):
            valid_elements.append(match_lbl)
        elif match_lbl in valid_elements:
            valid_elements.remove(match_lbl)

    def check_result():
        valid_element_names = [lbl.cget("text") for lbl in valid_elements]
        for el in all_elements:
            if (el.cget("text") in valid_element_names):
                el.config(bg="green")
            else:
                el.config(bg="red")

        if (len(valid_elements) == len(task["options"])):
            messagebox.showinfo(
                "Задание пройдено!", "Вы набрали +1 бал и готовы к выполнению следующего задания")
            increase_score()
        else:
            messagebox.showerror("Задание пройдено с ошибкой!",
                                 "Вы ошиблись при выполнении задания и не набрали 1 бал. Переходим к выполнению следующего задания")

    draggable_labels = []
    for (name, _) in task["options"]:
        draggable_label = DraggableWidget(
            container, cursor="hand2", relief=SOLID, font=CONFIG["font_size"]["title"], width=2, bd=1, bg="white", fg="black", text=name, on_release_callback=check_position)
        draggable_label.place(x=randint(10, 400), y=randint(275, 400))
        draggable_labels.append(draggable_label)

    check_result_button = Button(
        frames["2_3"], text="Проверить результат", font=CONFIG["font_size"]["title"], cursor="hand2", command=check_result)
    check_result_button.grid(row=3, column=0, pady=(50, 0), sticky=EW)

    link_label = Label(
        frames["2_3"], text="Узнать больше на Youtube.com", bg="#333", fg=CONFIG["bg"], cursor="hand2")
    link_label.grid(row=4, column=0, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open(task["meta"]["youtube"]))


def task_3_1():
    global cytology_photo_3_1_0
    global cytology_photos

    task = data.content["cytology"]["tasks"][0]

    frames["3_1"].grid()

    get_page_title(frames["3_1"], task["name"])

    frm_wrapper = Frame(frames["3_1"],
                        bg="white", height=750, width=464, bd=0)
    frm_wrapper.grid(row=1, column=0)
    frm_wrapper.grid_propagate(0)

    canvas = Canvas(frm_wrapper, width=464, height=750,
                    bg="white", highlightthickness=0)
    canvas.grid(row=0, column=0)

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    cytology_photos = [
        ImageTk.PhotoImage(PilImage.open(img_path))
        for img_path in image_paths
    ]

    draggable_texts = [name for (name, _) in task["options"]]

    img0 = PilImage.open(task["bg"])
    cytology_photo_3_1_0 = ImageTk.PhotoImage(img0)
    canvas.create_image(0, 0, anchor=NW, image=cytology_photo_3_1_0)

    valid_options = []

    def check_position(name, x, y):
        value = get_value(name, task["options"])

        if (x > 15 and x < 350 and y > 30 and y < 380 and value["required"] == True
                or not (x > 15 and x < 350 and y > 30 and y < 380 and value["required"] == False)):
            if (name not in valid_options):
                valid_options.append(name)
        else:
            if (name in valid_options):
                valid_options.remove(name)

    draggable_lbls = []
    for i, text in enumerate(draggable_texts):
        lbl = DraggableWidget(
            frm_wrapper, cursor="hand2", bd=1, text=text,
            bg=CONFIG["bg"], relief=SOLID,
            image=cytology_photos[i],
            on_release_callback=check_position
        )
        lbl.place(x=randint(10, 310), y=randint(465, 590))
        draggable_lbls.append(lbl)

    def check_result():
        for el in draggable_lbls:
            if (el.cget("text") in valid_options):
                el.config(bg="green")
            else:
                el.config(bg="red")

        if (len(valid_options) == len(task["options"])):
            messagebox.showinfo(
                "Задание пройдено!", "Вы набрали +1 бал и готовы к выполнению следующего задания")
            increase_score()
        else:
            messagebox.showerror("Задание пройдено с ошибкой!",
                                 "Вы ошиблись при выполнении задания и не набрали 1 бал. Переходим к выполнению следующего задания")

    check_button = Button(frames["3_1"], text="Проверить результат", font=font.Font(
        size=20), cursor="hand2", command=check_result)
    check_button.grid(row=2, column=0, pady=20, sticky=EW)


def task_3_2():
    task = data.content["cytology"]["tasks"][1]
    frames["3_2"].grid()

    get_page_title(frames["3_2"], task["name"], columnspan=4)

    def check_result():
        correct_answers = 0
        for _, correct, var, label in task["options"]:
            if var.get() == correct:
                label.config(bg="green", fg="white")
                correct_answers += 1
            else:
                label.config(bg="red", fg="white")
        if correct_answers == len(task["options"]):
            messagebox.showinfo(
                "Задание пройдено!", "Вы набрали +1 бал и готовы к выполнению следующего задания")
            increase_score()
        else:
            messagebox.showerror("Задание пройдено с ошибкой!",
                                 "Вы ошиблись при выполнении задания и не набрали 1 бал. Переходим к выполнению следующего задания")

    choice_values = list(set(value for _, value in task["options"]))

    for i, (name, correct_answer) in enumerate(task["options"]):
        var = StringVar(value="")
        label = Label(frames["3_2"], text=name, font=font.Font(size=16), bg=CONFIG["bg"],
                      fg="black")
        label.grid(row=i+1, column=0)

        for j, choice in enumerate(choice_values):
            rad_button = Radiobutton(frames["3_2"], text=choice, variable=var, value=choice, bg=CONFIG["bg"],
                                     fg="black")
            rad_button.grid(row=i+1, column=j+1)

        # TODO: fix, otherwise next time it's broken
        task["options"][i] = (
            name, correct_answer, var, label)

    check_button = Button(frames["3_2"], text="Проверить результат", font=font.Font(
        size=20), cursor="hand2", command=check_result)
    check_button.grid(row=i+2, column=0, pady=50, sticky=EW,
                      columnspan=4)


def task_3_3():
    global cytology_photo_3_3_1
    global cytology_photos
    task = data.content["cytology"]["tasks"][2]

    get_page_title(frames["3_3"], task["name"])

    frm_wrapper = Frame(frames["3_3"], bg="white", height=508,
                        width=700, bd=0)
    frm_wrapper.grid(row=1, column=0)
    frm_wrapper.grid_propagate(0)

    frm_tips = Frame(frm_wrapper,
                     bg="white", highlightthickness=0, width=125, height=508)
    frm_tips.grid(row=0, column=2, sticky=E)
    frm_tips.grid_remove()

    canvas = Canvas(frm_wrapper, width=414, height=508,
                    bg="white", highlightthickness=0)
    canvas.grid(row=0, column=0)
    frm_wrapper.grid_columnconfigure(1, weight=1)
    frm_wrapper.grid_columnconfigure(2, weight=1)

    img1 = PilImage.open(task["bg"])
    cytology_photo_3_3_1 = ImageTk.PhotoImage(img1)
    canvas.create_image(0, 0, anchor=NW, image=cytology_photo_3_3_1)

    image_paths = [opt["img_path"] for (_, opt) in task["options"]]
    cytology_photos = [
        ImageTk.PhotoImage(PilImage.open(img_path))
        for img_path in image_paths
    ]

    valid_puzzles = []

    def check_position(name, x, y):
        diff = 5
        xx, yy = find_coordinates(task["options"], name)

        if (abs(xx - x) < diff and abs(yy - y) < diff):
            if (name not in valid_puzzles):
                valid_puzzles.append(name)
        else:
            if (name in valid_puzzles):
                valid_puzzles.remove(name)

    draggable_texts = [name for (name, _) in task["options"]]
    for i, text in enumerate(draggable_texts):
        lbl = DraggableWidget(
            frm_wrapper, cursor="hand2", bd=0, text=text,
            image=cytology_photos[i],
            on_release_callback=check_position
        )
        lbl.place(x=randint(20, 160), y=randint(70, 260))

    for (name, option_config) in task["options"]:
        Label(frm_tips, bg="white", fg="black",
              text=f"<-- {name}").place(x=0, y=option_config["hint_y"])

    def check_result():
        if (len(valid_puzzles) == len(task["options"])):
            increase_score()

    check_result_button = Button(
        frames["3_3"], text="Проверить результат", font=CONFIG["font_size"]["title"], cursor="hand2", command=check_result)
    check_result_button.grid(row=3, column=0, pady=50, sticky=EW)

    def show_tips():
        frm_tips.grid()
        btn_tip.grid_remove()
        frm_tips.after(5000, frm_tips.grid_remove)

    btn_tip = Button(frames["3_3"], text="Показать подсказку на 5 секунд", highlightbackground=frm_panel.cget(
        "bg"), cursor="hand2",  command=show_tips)
    btn_tip.grid()


if __name__ == "__main__":
    left_panel_ui()
    landing(frm_landing)
    window.mainloop()
