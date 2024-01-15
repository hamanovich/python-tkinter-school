import data
import webbrowser
import sys
import os

from tkinter import *
from tkinter import font, messagebox
from PIL import Image as PilImage, ImageTk

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


def choose_topic(topic):
    global btn_home
    for btn in menu_btns:
        btn.config(highlightbackground="lightgreen", fg="black")
    btn_index = [index for index, (label, _) in enumerate(
        data.menu_buttons) if label == topic]

    btn = menu_btns[btn_index[0]]
    btn.config(highlightbackground="green", fg="green")

    lbl_main.config(text=topic)

    frm_landing.grid_remove()
    clear_frame_content(frm_task_2_1)
    clear_frame_content(frm_task_2_2)
    clear_frame_content(frm_task_3_1)

    if topic == "Ботаника":
        # task_2_1()
        task_1_2()

    if topic == "Анатомия":
        # task_2_1()
        # task_2_2()
        task_2_3()

    if topic == "Цитология":
        task_3_1()

    if btn_home is None:
        btn_home = Button(frm_menu_buttons,
                          text="🏠",
                          cursor="hand2",
                          highlightbackground=frm_panel.cget("bg"),
                          font=font.Font(size=20),
                          command=go_home)
        btn_home.grid(row=5, column=0, pady=5, sticky=EW)


def task_2_1_btn_click(index):
    current_text = entry_answer.get()
    updated_text = f"{current_text} {index}"
    entry_answer.config(bg="white", fg="black")
    entry_answer.delete(0, END)
    entry_answer.insert(0, updated_text)


def check_result():
    result = entry_answer.get()
    formatted_result = ''.join(result.split())

    if formatted_result == data.data["Ботаника"]["tasks"][0]["answer"]:
        entry_answer.config(bg="green", fg="white")
    else:
        entry_answer.config(bg="red", fg="white")


score = 0

# ==========
# LEFT PANEL


def go_home():
    global btn_home
    frm_landing.grid()
    clear_frame_content(frm_task_2_1)
    clear_frame_content(frm_task_2_2)
    clear_frame_content(frm_task_2_3)
    clear_frame_content(frm_task_3_1)
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
    frm_panel = Frame(window, bg="lightgreen", relief=RAISED, bd=2)
    frm_panel.grid(row=0, column=0, sticky=NSEW)
    frm_panel.rowconfigure(2, weight=1)

    lbl_panel = Label(frm_panel, text="Выберите раздел:",
                      bg="lightgreen", fg="black")
    lbl_panel.grid(row=0, column=0, padx=5, pady=1)

    frm_menu_buttons = Frame(frm_panel, bg="lightgreen")
    frm_menu_buttons.grid(row=1, column=0, padx=10, sticky=NSEW)
    menu_btns = []
    for idx, (menu_name_item, _) in enumerate(data.menu_buttons):
        btn_menu = Button(frm_menu_buttons,
                          text=menu_name_item,
                          cursor="hand2",
                          highlightbackground=frm_panel.cget("bg"),
                          font=font.Font(size=18),
                          command=lambda topic=menu_name_item: choose_topic(topic))
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
lbl_main.grid(row=0, column=0, columnspan=3, pady=(0, 15), sticky=EW)

frm_content = Frame(frm_main, padx=5, pady=5, bg=frm_main.cget("bg"))
frm_content.grid(row=1, column=0)

frm_landing = Frame(frm_content, bg="lightgreen")
frm_landing.grid(row=0, column=0)

frm_task_1_1 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_1_1.grid(row=0, column=0)

frm_task_1_2 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_1_2.grid(row=0, column=0)

frm_task_2_1 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_2_1.grid(row=0, column=0)

frm_task_2_2 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_2_2.grid(row=0, column=0)

frm_task_2_3 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_2_3.grid(row=0, column=0)

frm_task_3_1 = Frame(frm_content, bg=frm_main.cget("bg"))
frm_task_3_1.grid(row=0, column=0)


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

    for idx, (frm_name, frm_img) in enumerate(data.menu_buttons):
        frm = Frame(frame, borderwidth=2, relief=GROOVE, cursor="hand2")
        frm.grid(row=1, column=idx, padx=10, pady=10)
        image = PhotoImage(file=resource_path(frm_img))
        lbl_image = Label(frm, image=image)
        lbl_image.image = image
        lbl_image.grid(row=0, column=0)
        lbl_image.bind("<Button-1>", lambda _,
                       topic=frm_name: choose_topic(topic))
        lbl_text = Label(frm, text=frm_name)
        lbl_text.grid(row=1, column=0)
        lbl_text.bind("<Button-1>", lambda _,
                      topic=frm_name: choose_topic(topic))


# =============
# TASKS CONTENT

# БОТАНИКА
def task_1_2():
    frm_task_1_2.grid()

    lbl_task = Label(frm_task_1_2, anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["Ботаника"]["tasks"][1]["name"])
    lbl_task.grid(row=0, column=0)

    frm_crossword_questions = Frame(frm_task_1_2, bg=frm_main.cget("bg"))
    frm_crossword_questions.grid(row=1, column=0)

    for i, option in enumerate(data.data["Ботаника"]["tasks"][1]["options"]):
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
                if (entry.get() != data.data["Ботаника"]["tasks"][1]["options"][i]["answer"][k]):
                    entry.config(bg="red", fg="white")
                    valid = False
                else:
                    entry.config(bg="green", fg="white")

        keyword = ""
        for char in crossword_keyword:
            keyword += char.get()

        if (keyword == data.data["Ботаника"]["tasks"][1]["answer"] and valid):
            messagebox.showinfo("Кроссворд разгадан",
                                "Поздравляю, вы разгадали кроссворд верно!")

    def reset_crossword():
        for crossword_answer in crossword_answers:
            for entry in crossword_answer:
                entry.config(bg="white", fg="black")
                entry.delete(0, END)

    # Draw grid
    for row, option in enumerate(data.data["Ботаника"]["tasks"][1]["options"]):
        for i in range(0, option["padLeft"]):
            label = Label(frm_crossword, width=2, bg=frm_panel.cget("bg"))
            label.grid(row=row+3, column=i)

        label = Label(frm_crossword, width=2, text=row+1, bg="white",
                      fg="black", bd=1, highlightthickness=1, relief="solid")
        label.grid(row=row+2, column=option["padLeft"])

        row_entries = []

        for i in range(option["padLeft"]+1, option["padLeft"]+1 + len(option["answer"])):
            entry = Entry(frm_crossword, bg="yellow" if i == 8 else "white", fg="black",
                          width=2, highlightthickness=1, highlightbackground="white", bd=1, justify="center", relief="solid")
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


# ======
# АНАТОМИЯ
def task_2_1():
    global entry_answer
    frm_task_2_1.grid()

    lbl_task = Label(frm_task_2_1, anchor=W, wraplength=600,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     text=data.data["Анатомия"]["tasks"][0]["name"])
    lbl_task.grid(row=0, column=0)

    entry_answer = Entry(frm_task_2_1, bg="white",
                         fg="black", font=font.Font(size=20))
    entry_answer.grid(row=1, column=0, pady=10, sticky=EW)

    for (idx, option) in data.data["Анатомия"]["tasks"][0]["options"]:
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
                     text=data.data["Анатомия"]["tasks"][1]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

    tk_image = PhotoImage(file=resource_path("images/eye_350.png"))
    lbl_image = Label(frm_task_2_2, image=tk_image)
    lbl_image.image = tk_image
    lbl_image.grid(row=1, column=0)

    def check_position(name, x, y):
        diff = 25
        match_option = [option for (
            n, option) in data.data["Анатомия"]["tasks"][1]["options"] if n == name][0]
        match_btn = [
            btn for btn in draggable_labels if btn.cget("text") == name][0]

        if (abs(match_option["x"] - x)) < diff and abs(match_option["y"] - y) < diff:
            match_btn.config(highlightbackground="green", fg="green")
        else:
            match_btn.config(highlightbackground="red", fg="red")

    draggable_labels = []
    for idx, (name, _) in enumerate(data.data["Анатомия"]["tasks"][1]["options"]):
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
        "<Button-1>", lambda _: webbrowser.open(data.data["Анатомия"]["tasks"][1]["meta"]["youtube"]))


def task_2_3():
    frm_task_2_3.grid()
    lbl_task = Label(frm_task_2_3,
                     anchor=W,
                     wraplength=500,
                     bg=frm_main.cget("bg"),
                     fg="black",
                     pady=5,
                     font=font.Font(size=16),
                     text=data.data["Анатомия"]["tasks"][2]["name"])
    lbl_task.grid(row=0, column=0, pady=(0, 15))

    link_label = Label(
        frm_task_2_3, text="Узнать больше на Youtube.com", bg="#333", fg="lightgreen", cursor="hand2")
    link_label.grid(row=3, column=0, pady=10)
    link_label.bind(
        "<Button-1>", lambda _: webbrowser.open(data.data["Анатомия"]["tasks"][2]["meta"]["youtube"]))

# ======
# ЦИТОЛОГИЯ


def task_3_1():
    global photo1, photo2
    frm_task_3_1.grid()
    lbl_intro = Label(frm_task_3_1,
                      anchor=W,
                      wraplength=500,
                      bg=frm_main.cget("bg"),
                      fg="black",
                      pady=30,
                      text=data.data["Цитология"]["intro"])
    lbl_intro.grid(row=0, column=0)

    canvas = Canvas(frm_task_3_1, width=650, height=650,
                    bg="lightgreen", highlightthickness=1)
    canvas.grid(row=1, column=0)

    img1 = PilImage.open("images/botanika/botanika_3_3x650.png")
    photo1 = ImageTk.PhotoImage(img1)

    img2 = PilImage.open("images/cytology/ядро.png")
    photo2 = ImageTk.PhotoImage(img2)

    canvas.create_image(0, 0, anchor=NW, image=photo1)
    canvas.create_image(0, 0, anchor=NW, image=photo2)


# =====
if __name__ == "__main__":
    left_panel_ui()
    landing(frm_landing)
    window.mainloop()
