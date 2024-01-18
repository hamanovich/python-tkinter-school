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


def clear_frame_content(frame):
    frame.grid_remove()
    for widget in frame.winfo_children():
        widget.destroy()


def choose_topic(slug, name):
    global btn_home
    for btn in menu_btns:
        btn.config(highlightbackground="lightgreen", fg="black")
    btn_index = [index for index, (slug_name, _, _) in enumerate(
        data.menu_buttons) if slug_name == slug]

    btn = menu_btns[btn_index[0]]
    btn.config(highlightbackground="green", fg="green")

    lbl_main.config(text=name)

    frm_landing.grid_remove()
    for frame_id in frame_ids:
        clear_frame_content(frames[frame_id])

    # TODO: Make landing screens for each section
    if slug == "botanika":
        task_1_1()
        # task_1_2()
        # task_1_3()

    if slug == "anatomy":
        # task_2_1()
        # task_2_2()
        task_2_3()

    if slug == "cytology":
        # task_3_1()
        # task_3_2()
        task_3_3()

    if btn_home is None:
        btn_home = Button(frm_menu_buttons,
                          text="🏠",
                          cursor="hand2",
                          highlightbackground=frm_panel.cget("bg"),
                          font=font.Font(size=20),
                          command=go_home)
        btn_home.grid(row=5, column=0, pady=5, sticky=EW)


def increase_score():
    global score
    score += 1
    lbl_score.config(text=f"{score}/{total_tasks}")

# ==========
# LEFT PANEL


def go_home():
    global btn_home
    frm_landing.grid()
    for frame_id in frame_ids:
        clear_frame_content(frames[frame_id])
    clear_frame_content(btn_home)
    lbl_main.config(text=TITLE)
    btn_home = None

    for btn in menu_btns:
        btn.config(highlightbackground="lightgreen", fg="black")


def left_panel_ui():
    global menu_btns
    global btn_home
    global frm_panel
    global frm_menu_buttons
    global lbl_score
    frm_panel = Frame(window, bg="lightgreen", relief=RAISED, bd=2)
    frm_panel.grid(row=0, column=0, sticky=NSEW)
    frm_panel.rowconfigure(2, weight=1)

    lbl_panel = Label(frm_panel, text="Выберите раздел:",
                      bg="lightgreen", fg="black")
    lbl_panel.grid(row=0, column=0, padx=5, pady=1)

    frm_menu_buttons = Frame(frm_panel, bg="lightgreen")
    frm_menu_buttons.grid(row=1, column=0, padx=10, sticky=NSEW)

    menu_btns = []

    for idx, (slug, name, _) in enumerate(data.menu_buttons):
        btn_menu = Button(frm_menu_buttons,
                          text=name,
                          cursor="hand2",
                          highlightbackground=frm_panel.cget("bg"),
                          font=font.Font(size=18),
                          command=lambda slug=slug, name=name: choose_topic(slug, name))
        btn_menu.grid(row=idx, column=0, pady=5, sticky=EW)
        menu_btns.append(btn_menu)

    btn_home = None

    frm_copyrights = Frame(frm_panel, bg=frm_panel.cget("bg"))
    frm_copyrights.grid(row=2, column=0, sticky=N)

    lbl_copyrights = Label(frm_copyrights, text="СШ №8, Биология,\n2023", bg=frm_panel.cget(
        "bg"), fg="black", font=font.Font(size=10))
    lbl_copyrights.grid(row=0, column=0)

    lbl_score = Label(frm_panel, text=f"{score}/{total_tasks}", font=font.Font(size=30),
                      bg="lightgreen", fg="black")
    lbl_score.grid(row=3, column=0, padx=5, pady=1)

    # TODO: Add Sunflower image
    # tk_image = PhotoImage(file=resource_path("images/sunflower.png"))
    # lbl_image = Label(frm_panel, image=tk_image, bg="lightgreen")
    # lbl_image.image = tk_image
    # lbl_image.grid(row=10, column=0)


# ============
# MAIN CONTENT
frm_main = Frame(bg="lightgreen")
frm_main.grid(row=0, column=1, sticky=NSEW)
frm_main.columnconfigure(0, weight=1)

lbl_main = Label(frm_main, text=TITLE, bg="lightgreen", fg="black",
                 font=font.Font(size=38), anchor="center")
lbl_main.grid(row=0, column=0, columnspan=3, pady=(20, 20), sticky=EW)

frm_content = Frame(frm_main, padx=5, pady=5, bg=frm_main.cget("bg"))
frm_content.grid(row=1, column=0)

frm_landing = Frame(frm_content, bg="lightgreen")
frm_landing.grid(row=0, column=0)

frames = {}
frame_ids = ["1_1", "1_2", "1_3", "2_1", "2_2", "2_3", "3_1", "3_2", "3_3"]
for frame_id in frame_ids:
    frame = Frame(frm_content, bg=frm_main.cget("bg"))
    frame.grid(row=0, column=0)
    frames[frame_id] = frame


total_tasks = sum(len(cat["tasks"]) for cat in data.data.values())
score = 0


# ============
# LANDING SCREEN
def landing(frame):
    lbl_landing = Label(frame,
                        anchor=W,
                        text=f"Выберите раздел",
                        font=font.Font(size=20),
                        bg="lightgreen",
                        fg="black",
                        pady=10)
    lbl_landing.grid(row=0, column=0, columnspan=4)

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


# =============
# TASKS CONTENT

# BOTANIKA
def task_1_1():
    frames["1_1"].grid()

    lbl_task = Label(frames["1_1"], anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=20),
                     text=data.data["botanika"]["tasks"][0]["name"])
    lbl_task.grid(row=0, column=0)

    frm_options = Frame(frames["1_1"], bg=frm_main.cget("bg"))
    frm_options.grid(row=1, column=0)

    for i, option in enumerate(data.data["botanika"]["tasks"][0]["options"]):
        lbl_option = Label(frm_options, anchor=W, wraplength=750,
                           bg=frm_main.cget("bg"),
                           fg="black",
                           font=font.Font(size=16),
                           text=f"{option[0]}. {option[1]}")
        lbl_option.grid(row=i, column=0)

    frm_task = Frame(frames["1_1"], bg=frm_main.cget("bg"))
    frm_task.grid(row=2, column=0, pady=20)

    row_entries = []

    for i in range(5):
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
                if (variant.get() != data.data["botanika"]["tasks"][0]["answer"][i]):
                    variant.config(bg="red", fg="white")
                else:
                    variant.config(bg="green", fg="white")

    check_result_button = Button(
        frames["1_1"], text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_task)
    check_result_button.grid(row=4, column=0, pady=10, sticky=EW)


def task_1_2():
    frames["1_2"].grid()

    lbl_task = Label(frames["1_2"], anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["botanika"]["tasks"][1]["name"])
    lbl_task.grid(row=0, column=0)

    frm_crossword_questions = Frame(
        frames["1_2"], bg=frm_main.cget("bg"))
    frm_crossword_questions.grid(row=1, column=0)

    for i, option in enumerate(data.data["botanika"]["tasks"][1]["options"]):
        lbl_crossword_question = Label(frm_crossword_questions, anchor=W, wraplength=750,
                                       bg=frm_main.cget("bg"),
                                       fg="black",
                                       width=75,
                                       text=f"{i+1}. {option["question"]}")
        lbl_crossword_question.grid(row=i, column=0)

    frm_crossword = Frame(frames["1_2"], bg=frm_main.cget("bg"))
    frm_crossword.grid(row=2, column=0, pady=20)

    crossword_answers = []
    crossword_keyword = []

    def check_crossword():
        valid = True
        for i, crossword_answer in enumerate(crossword_answers):
            result = ""
            for k, entry in enumerate(crossword_answer):
                result += entry.get()
                if (entry.get() != data.data["botanika"]["tasks"][1]["options"][i]["answer"][k]):
                    entry.config(bg="red", fg="white")
                    valid = False
                else:
                    entry.config(bg="green", fg="white")

        keyword = ""
        for char in crossword_keyword:
            keyword += char.get()

        if (keyword == data.data["botanika"]["tasks"][1]["answer"] and valid):
            messagebox.showinfo("Кроссворд разгадан",
                                "Поздравляю, вы разгадали кроссворд верно!")

    def reset_crossword():
        for crossword_answer in crossword_answers:
            for entry in crossword_answer:
                entry.config(bg="white", fg="black")
                entry.delete(0, END)

    # Draw grid
    for row, option in enumerate(data.data["botanika"]["tasks"][1]["options"]):
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
        frames["1_2"], text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_crossword)
    check_result_button.grid(row=20, column=0, pady=10, sticky=EW)

    reset_crossword_button = Button(
        frames["1_2"], text="Начать сначала", font=font.Font(size=20), cursor="hand2", command=reset_crossword)
    reset_crossword_button.grid(row=21, column=0, pady=10, sticky=EW)


def task_1_3():
    frames["1_3"].grid()

    lbl_task = Label(frames["1_3"], anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["botanika"]["tasks"][2]["name"])
    lbl_task.grid(row=0, column=0)


# ======
# ANATOMY


def task_2_1():
    global entry_answer
    frames["2_1"].grid()

    lbl_task = Label(frames["2_1"], anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     text=data.data["anatomy"]["tasks"][0]["name"])
    lbl_task.grid(row=0, column=0)

    entry_answer = Entry(frames["2_1"], bg="white",
                         fg="black", font=font.Font(size=20))
    entry_answer.grid(row=1, column=0, pady=10, sticky=EW)

    def task_2_1_btn_click(index):
        current_text = entry_answer.get()
        updated_text = f"{current_text} {index}"
        entry_answer.config(bg="white", fg="black")
        entry_answer.delete(0, END)
        entry_answer.insert(0, updated_text)

    for (idx, option) in data.data["anatomy"]["tasks"][0]["options"]:
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

        if formatted_result == data.data["botanika"]["tasks"][0]["answer"]:
            entry_answer.config(bg="green", fg="white")
        else:
            entry_answer.config(bg="red", fg="white")

    check_result_button = Button(
        frames["2_1"], text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_result)
    check_result_button.grid(row=10, column=0, pady=10, sticky=EW)


def task_2_2():
    frames["2_2"].grid()
    lbl_task = Label(frames["2_2"],
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["anatomy"]["tasks"][1]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

    tk_image = PhotoImage(file=resource_path("images/eye_350.png"))
    lbl_image = Label(frames["2_2"], image=tk_image)
    lbl_image.image = tk_image
    lbl_image.grid(row=1, column=0)

    def check_result():
        pass

    def check_position(name, x, y):
        diff = 25
        match_option = [option for (
            n, option) in data.data["anatomy"]["tasks"][1]["options"] if n == name][0]
        match_btn = [
            btn for btn in draggable_labels if btn.cget("text") == name][0]

        if (abs(match_option["x"] - x)) < diff and abs(match_option["y"] - y) < diff:
            match_btn.config(highlightbackground="green", fg="green")
        else:
            match_btn.config(highlightbackground="red", fg="red")

    draggable_labels = []
    for idx, (name, _) in enumerate(data.data["anatomy"]["tasks"][1]["options"]):
        draggable_label = DraggableWidget(
            frames["2_2"], cursor="hand2", relief=RAISED, bd=1, bg="#666", fg="white", text=name, on_release_callback=check_position)
        draggable_label.place(x=5, y=50 + idx * 25)
        draggable_labels.append(draggable_label)

    check_result_button = Button(
        frames["2_2"], text="Проверить результат", font=font.Font(size=20), command=check_result)
    check_result_button.grid(row=2, column=0, pady=10, sticky=EW)

    link_label = Label(
        frames["2_2"], text="Узнать больше на Youtube.com", bg="#333", fg="lightgreen", cursor="hand2")
    link_label.grid(row=3, column=0, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open(data.data["anatomy"]["tasks"][1]["meta"]["youtube"]))


def task_2_3():
    frames["2_3"].grid()

    options = data.data["anatomy"]["tasks"][2]["options"]

    lbl_task = Label(frames["2_3"],
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["anatomy"]["tasks"][2]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

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
        value = get_value(name, options)
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

        if (len(valid_elements) == len(options)):
            increase_score()

    draggable_labels = []
    for (name, _) in options:
        draggable_label = DraggableWidget(
            container, cursor="hand2", relief=SOLID, font=font.Font(size=20), width=2, bd=1, bg="white", fg="black", text=name, on_release_callback=check_position)
        draggable_label.place(x=randint(10, 400), y=randint(275, 400))
        draggable_labels.append(draggable_label)

    check_result_button = Button(
        frames["2_3"], text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_result)
    check_result_button.grid(row=3, column=0, pady=(50, 0), sticky=EW)

    link_label = Label(
        frames["2_3"], text="Узнать больше на Youtube.com", bg="#333", fg="lightgreen", cursor="hand2")
    link_label.grid(row=4, column=0, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open(data.data["anatomy"]["tasks"][2]["meta"]["youtube"]))


# ======
# CYTOLOGY


def task_3_1():
    global cytology_photo_3_1_0
    global cytology_photos

    options = data.data["cytology"]["tasks"][0]["options"]

    frames["3_1"].grid()
    lbl_intro = Label(frames["3_1"],
                      anchor=W,
                      wraplength=500,
                      bg=frm_main.cget("bg"),
                      fg="black",
                      pady=5,
                      font=font.Font(size=16),
                      text=data.data["cytology"]["tasks"][0]["name"])
    lbl_intro.grid(row=0, column=0)

    frm_wrapper = Frame(frames["3_1"],
                        bg="white", height=750, width=464, bd=0)
    frm_wrapper.grid(row=1, column=0)
    frm_wrapper.grid_propagate(0)

    canvas = Canvas(frm_wrapper, width=464, height=750,
                    bg="white", highlightthickness=0)
    canvas.grid(row=0, column=0)

    image_paths = [opt["img_path"] for (_, opt) in options]
    cytology_photos = [
        ImageTk.PhotoImage(PilImage.open(img_path))
        for img_path in image_paths
    ]

    draggable_texts = [name for (name, _) in options]

    img0 = PilImage.open("images/cytology/клетка.png")
    cytology_photo_3_1_0 = ImageTk.PhotoImage(img0)
    canvas.create_image(0, 0, anchor=NW, image=cytology_photo_3_1_0)

    valid_options = []

    def check_position(name, x, y):
        value = get_value(name, options)

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
            bg="lightgreen", relief=SOLID,
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

        if (len(valid_options) == len(options)):
            increase_score()

    check_button = Button(frames["3_1"], text="Проверить результат", font=font.Font(
        size=20), cursor="hand2", command=check_result)
    check_button.grid(row=2, column=0, pady=20, sticky=EW)


def task_3_2():
    frames["3_2"].grid()
    lbl_task = Label(frames["3_2"],
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["cytology"]["tasks"][1]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15), columnspan=4)

    options = data.data["cytology"]["tasks"][1]["options"]

    def check_result():
        correct_answers = 0
        for _, correct, var, label in options:
            if var.get() == correct:
                label.config(bg="green", fg="white")
                correct_answers += 1
            else:
                label.config(bg="red", fg="white")
        if correct_answers == len(options):
            increase_score()

    choice_values = list(set(value for _, value in options))

    for i, (name, correct_answer) in enumerate(options):
        var = StringVar(value="")
        label = Label(frames["3_2"], text=name, font=font.Font(size=16), bg=frm_main.cget("bg"),
                      fg="black")
        label.grid(row=i+1, column=0)

        for j, choice in enumerate(choice_values):
            rad_button = Radiobutton(frames["3_2"], text=choice, variable=var, value=choice, bg=frm_main.cget("bg"),
                                     fg="black")
            rad_button.grid(row=i+1, column=j+1)

        # TODO: fix, otherwise next time it's broken
        options[i] = (
            name, correct_answer, var, label)

    check_button = Button(frames["3_2"], text="Проверить результат", font=font.Font(
        size=20), cursor="hand2", command=check_result)
    check_button.grid(row=i+2, column=0, pady=50, sticky=EW,
                      columnspan=4)


def task_3_3():
    global cytology_photo_3_3_1
    global cytology_photos

    options = data.data["cytology"]["tasks"][2]["options"]

    frames["3_3"].grid()
    lbl_task = Label(frames["3_3"],
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["cytology"]["tasks"][2]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

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

    img1 = PilImage.open("images/cytology/cytology_3_3_00.jpg")
    cytology_photo_3_3_1 = ImageTk.PhotoImage(img1)
    canvas.create_image(0, 0, anchor=NW, image=cytology_photo_3_3_1)

    image_paths = [opt["img_path"] for (_, opt) in options]
    cytology_photos = [
        ImageTk.PhotoImage(PilImage.open(img_path))
        for img_path in image_paths
    ]

    valid_puzzles = []

    def check_position(name, x, y):
        diff = 5
        xx, yy = find_coordinates(options, name)

        if (abs(xx - x) < diff and abs(yy - y) < diff):
            if (name not in valid_puzzles):
                valid_puzzles.append(name)
        else:
            if (name in valid_puzzles):
                valid_puzzles.remove(name)

    draggable_texts = [name for (name, _) in options]
    for i, text in enumerate(draggable_texts):
        lbl = DraggableWidget(
            frm_wrapper, cursor="hand2", bd=0, text=text,
            image=cytology_photos[i],
            on_release_callback=check_position
        )
        lbl.place(x=randint(20, 160), y=randint(70, 260))

    for (name, option_config) in options:
        Label(frm_tips, bg="white", fg="black",
              text=f"<-- {name}").place(x=0, y=option_config["hint_y"])

    def check_result():
        if (len(valid_puzzles) == len(data.data["cytology"]["tasks"][2]["options"])):
            increase_score()

    check_result_button = Button(
        frames["3_3"], text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_result)
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
