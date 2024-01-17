import data
import webbrowser
import sys
import os

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
    clear_frame_content(frm_task_1_1)
    clear_frame_content(frm_task_1_2)
    clear_frame_content(frm_task_1_3)
    clear_frame_content(frm_task_2_1)
    clear_frame_content(frm_task_2_2)
    clear_frame_content(frm_task_2_3)
    clear_frame_content(frm_task_3_1)
    clear_frame_content(frm_task_3_2)
    clear_frame_content(frm_task_3_3)

    if slug == "botanika":
        task_1_1()
        # task_1_2()
        # task_1_3()

    if slug == "anatomy":
        task_2_1()
        # task_2_2()
        # task_2_3()

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
    lbl_score.config(text=f"{score}/9")

# ==========
# LEFT PANEL


def go_home():
    global btn_home
    frm_landing.grid()
    clear_frame_content(frm_task_1_1)
    clear_frame_content(frm_task_1_2)
    clear_frame_content(frm_task_1_3)
    clear_frame_content(frm_task_2_1)
    clear_frame_content(frm_task_2_2)
    clear_frame_content(frm_task_2_3)
    clear_frame_content(frm_task_3_1)
    clear_frame_content(frm_task_3_2)
    clear_frame_content(frm_task_3_3)
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

    # TODO: replace 9 to amount of tasks
    lbl_score = Label(frm_panel, text=f"{score}/9", font=font.Font(size=30),
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

frm_task_1_1 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_1_1.grid(row=0, column=0)

frm_task_1_2 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_1_2.grid(row=0, column=0)

frm_task_1_3 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_1_3.grid(row=0, column=0)

frm_task_2_1 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_2_1.grid(row=0, column=0)

frm_task_2_2 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_2_2.grid(row=0, column=0)

frm_task_2_3 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_2_3.grid(row=0, column=0)

frm_task_3_1 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_3_1.grid(row=0, column=0)

frm_task_3_2 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_3_2.grid(row=0, column=0)

frm_task_3_3 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_3_3.grid(row=0, column=0)


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
    frm_task_1_1.grid()

    lbl_task = Label(frm_task_1_1, anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=20),
                     text=data.data["botanika"]["tasks"][0]["name"])
    lbl_task.grid(row=0, column=0)

    frm_options = Frame(frm_task_1_1, bg=frm_main.cget("bg"))
    frm_options.grid(row=1, column=0)

    for i, option in enumerate(data.data["botanika"]["tasks"][0]["options"]):
        lbl_option = Label(frm_options, anchor=W, wraplength=750,
                           bg=frm_main.cget("bg"),
                           fg="black",
                           font=font.Font(size=16),
                           text=f"{option[0]}. {option[1]}")
        lbl_option.grid(row=i, column=0)

    frm_task = Frame(frm_task_1_1, bg=frm_main.cget("bg"))
    frm_task.grid(row=2, column=0, pady=20)

    row_entries = []

    for i in range(5):
        var = StringVar()
        var.trace_add("write", lambda *args, var=var: check_only_digit(var))
        entry = Entry(frm_task, bg="white", fg="black", font=font.Font(size=48), width=2, highlightthickness=1,
                      highlightbackground="white", bd=2, justify="center", relief="solid", textvariable=var)
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
        frm_task_1_1, text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_task)
    check_result_button.grid(row=4, column=0, pady=10, sticky=EW)


def task_1_2():
    frm_task_1_2.grid()

    lbl_task = Label(frm_task_1_2, anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["botanika"]["tasks"][1]["name"])
    lbl_task.grid(row=0, column=0)

    frm_crossword_questions = Frame(frm_task_1_2, bg=frm_main.cget("bg"))
    frm_crossword_questions.grid(row=1, column=0)

    for i, option in enumerate(data.data["botanika"]["tasks"][1]["options"]):
        lbl_crossword_question = Label(frm_crossword_questions, anchor=W, wraplength=750,
                                       bg=frm_main.cget("bg"),
                                       fg="black",
                                       width=75,
                                       text=f"{i+1}. {option["question"]}")
        lbl_crossword_question.grid(row=i, column=0)

    frm_crossword = Frame(frm_task_1_2, bg=frm_main.cget("bg"))
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
                      fg="black", bd=1, highlightthickness=1, relief="solid")
        label.grid(row=row+2, column=option["padLeft"])

        row_entries = []

        for i in range(option["padLeft"]+1, option["padLeft"]+1 + len(option["answer"])):
            var = StringVar()
            var.trace_add("write", lambda *args,
                          var=var: check_only_letter(var))
            entry = Entry(frm_crossword, bg="yellow" if i == 8 else "white", fg="black",
                          width=2, highlightthickness=1, highlightbackground="white", bd=1, justify="center", relief="solid", textvariable=var)
            entry.grid(row=row+2, column=i)
            row_entries.append(entry)
            if (i == 7):
                crossword_keyword.append(entry)

        crossword_answers.append(row_entries)

    check_result_button = Button(
        frm_task_1_2, text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_crossword)
    check_result_button.grid(row=20, column=0, pady=10, sticky=EW)

    reset_crossword_button = Button(
        frm_task_1_2, text="Начать сначала", font=font.Font(size=20), cursor="hand2", command=reset_crossword)
    reset_crossword_button.grid(row=21, column=0, pady=10, sticky=EW)


def task_1_3():
    frm_task_1_3.grid()

    lbl_task = Label(frm_task_1_3, anchor=W, wraplength=600,
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
    frm_task_2_1.grid()

    lbl_task = Label(frm_task_2_1, anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     text=data.data["anatomy"]["tasks"][0]["name"])
    lbl_task.grid(row=0, column=0)

    entry_answer = Entry(frm_task_2_1, bg="white",
                         fg="black", font=font.Font(size=20))
    entry_answer.grid(row=1, column=0, pady=10, sticky=EW)

    def task_2_1_btn_click(index):
        current_text = entry_answer.get()
        updated_text = f"{current_text} {index}"
        entry_answer.config(bg="white", fg="black")
        entry_answer.delete(0, END)
        entry_answer.insert(0, updated_text)

    for (idx, option) in data.data["anatomy"]["tasks"][0]["options"]:
        row_frame = Frame(frm_task_2_1, bg="white")
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
        frm_task_2_1, text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_result)
    check_result_button.grid(row=10, column=0, pady=10, sticky=EW)


def task_2_2():
    frm_task_2_2.grid()
    lbl_task = Label(frm_task_2_2,
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["anatomy"]["tasks"][1]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

    tk_image = PhotoImage(file=resource_path("images/eye_350.png"))
    lbl_image = Label(frm_task_2_2, image=tk_image)
    lbl_image.image = tk_image
    lbl_image.grid(row=1, column=0)

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
            frm_task_2_2, cursor="hand2", relief=RAISED, bd=1, bg="#666", fg="white", text=name, on_release_callback=check_position)
        draggable_label.place(x=5, y=50 + idx * 25)
        draggable_labels.append(draggable_label)

    # check_result_button = Button(
    #     frm_task_2_2, text="Проверить результат", font=font.Font(size=20), command=check_result)
    # check_result_button.grid(row=2, column=0, pady=10, sticky=EW)

    link_label = Label(
        frm_task_2_2, text="Узнать больше на Youtube.com", bg="#333", fg="lightgreen", cursor="hand2")
    link_label.grid(row=3, column=0, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open(data.data["anatomy"]["tasks"][1]["meta"]["youtube"]))


def task_2_3():
    frm_task_2_3.grid()
    lbl_task = Label(frm_task_2_3,
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["anatomy"]["tasks"][2]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

    link_label = Label(
        frm_task_2_3, text="Узнать больше на Youtube.com", bg="#333", fg="lightgreen", cursor="hand2")
    link_label.grid(row=3, column=0, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open(data.data["anatomy"]["tasks"][2]["meta"]["youtube"]))


# ======
# CYTOLOGY


def task_3_1():
    global cytology_photo_3_1_1, cytology_photo_3_1_2
    frm_task_3_1.grid()
    lbl_intro = Label(frm_task_3_1,
                      anchor=W,
                      wraplength=500,
                      bg=frm_main.cget("bg"),
                      fg="black",
                      pady=5,
                      font=font.Font(size=16),
                      text=data.data["cytology"]["tasks"][0]["name"])
    lbl_intro.grid(row=0, column=0)

    canvas = Canvas(frm_task_3_1, width=650, height=650,
                    bg="white", highlightthickness=1)
    canvas.grid(row=1, column=0)

    img1 = PilImage.open("images/cytology/клетка.png")
    cytology_photo_3_1_1 = ImageTk.PhotoImage(img1)

    img2 = PilImage.open("images/cytology/ядро.png")
    cytology_photo_3_1_2 = ImageTk.PhotoImage(img2)

    canvas.create_image(0, 0, anchor=NW, image=cytology_photo_3_1_1)
    canvas.create_image(0, 0, anchor=NW, image=cytology_photo_3_1_2)


def task_3_2():
    frm_task_3_2.grid()
    lbl_task = Label(frm_task_3_2,
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["cytology"]["tasks"][1]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))


def task_3_3():
    global cytology_photo_3_3_1, cytology_photo_3_3_2, cytology_photo_3_3_3, cytology_photo_3_3_4, cytology_photo_3_3_5, cytology_photo_3_3_6, cytology_photo_3_3_7

    frm_task_3_3.grid()
    lbl_task = Label(frm_task_3_3,
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["cytology"]["tasks"][2]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

    frm_wrapper = Frame(frm_task_3_3, bg="white", height=508,
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
    img2 = PilImage.open("images/cytology/cytology_3_3_01.jpg")
    cytology_photo_3_3_2 = ImageTk.PhotoImage(img2)
    img3 = PilImage.open("images/cytology/cytology_3_3_02.jpg")
    cytology_photo_3_3_3 = ImageTk.PhotoImage(img3)
    img4 = PilImage.open("images/cytology/cytology_3_3_03.jpg")
    cytology_photo_3_3_4 = ImageTk.PhotoImage(img4)
    img5 = PilImage.open("images/cytology/cytology_3_3_04.jpg")
    cytology_photo_3_3_5 = ImageTk.PhotoImage(img5)
    img6 = PilImage.open("images/cytology/cytology_3_3_05.jpg")
    cytology_photo_3_3_6 = ImageTk.PhotoImage(img6)
    img7 = PilImage.open("images/cytology/cytology_3_3_06.jpg")
    cytology_photo_3_3_7 = ImageTk.PhotoImage(img7)

    canvas.create_image(0, 0, anchor=NW, image=cytology_photo_3_3_1)

    valid_puzzles = []

    def check_position(name, x, y):
        diff = 5
        xx, yy = find_coordinates(
            data.data["cytology"]["tasks"][2]["options"], name)

        if (abs(xx - x) < diff and abs(yy - y) < diff):
            if (name not in valid_puzzles):
                valid_puzzles.append(name)
        else:
            if (name in valid_puzzles):
                valid_puzzles.remove(name)

    DraggableWidget(
        frm_wrapper, cursor="hand2", bd=0, text="дерма", image=cytology_photo_3_3_2, on_release_callback=check_position).place(x=155, y=85)
    Label(frm_tips, bg="white", fg="black", text="<-- дерма").place(x=0, y=450)

    DraggableWidget(
        frm_wrapper, cursor="hand2", bd=0, text="базальный", image=cytology_photo_3_3_3, on_release_callback=check_position).place(x=40, y=195)
    Label(frm_tips, bg="white", fg="black", text="<-- базальный").place(x=0, y=375)

    DraggableWidget(
        frm_wrapper, cursor="hand2", bd=0, text="шиповатый", image=cytology_photo_3_3_4, on_release_callback=check_position).place(x=75, y=115)
    Label(frm_tips, bg="white", fg="black", text="<-- шиповатый").place(x=0, y=300)

    DraggableWidget(
        frm_wrapper, cursor="hand2", bd=0, text="зернистый", image=cytology_photo_3_3_5, on_release_callback=check_position).place(x=140, y=205)
    Label(frm_tips, bg="white", fg="black", text="<-- зернистый").place(x=0, y=210)

    DraggableWidget(
        frm_wrapper, cursor="hand2", bd=0, text="блестящий", image=cytology_photo_3_3_6, on_release_callback=check_position).place(x=30, y=70)
    Label(frm_tips, bg="white", fg="black", text="<-- блестящий").place(x=0, y=120)

    DraggableWidget(
        frm_wrapper, cursor="hand2", bd=0, text="роговой", image=cytology_photo_3_3_7, on_release_callback=check_position).place(x=25, y=255)
    Label(frm_tips, bg="white", fg="black", text="<-- роговой").place(x=0, y=35)

    def check_result():
        if (len(valid_puzzles) == len(data.data["cytology"]["tasks"][2]["options"])):
            increase_score()

    check_result_button = Button(
        frm_task_3_3, text="Проверить результат", font=font.Font(size=20), cursor="hand2", command=check_result)
    check_result_button.grid(row=3, column=0, pady=50, sticky=EW)

    def show_tips():
        frm_tips.grid()
        btn_tip.grid_remove()
        frm_tips.after(5000, frm_tips.grid_remove)

    btn_tip = Button(frm_task_3_3, text="Показать подсказку на 5 секунд", highlightbackground=frm_panel.cget(
        "bg"), cursor="hand2",  command=show_tips)
    btn_tip.grid()


if __name__ == "__main__":
    left_panel_ui()
    landing(frm_landing)
    window.mainloop()
