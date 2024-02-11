from tkinter import Tk

CONFIG = {
    "window": {
        "width": 1000,
        "height": 925
    },
    "bg": {
        "main": "lightgreen",
        "ok": "green",
        "error": "red"
    },
    "font_size": {
        "heading": 30,
        "title": 16,
        "text": 14,
        "text_small": 12,
    }
}

FRAME_IDS = ["intro", "botanika", "anatomy", "cytology", "task_1_1", "task_1_2", "task_1_3",
             "task_2_1", "task_2_2", "task_2_3", "task_3_1", "task_3_2", "task_3_3", "result"]
TASKS_ALL = ["intro", "task_1_1", "task_1_2", "task_1_3", "task_2_1",
             "task_2_2", "task_2_3", "task_3_1", "task_3_2", "task_3_3", "landing_result"]
TASKS_BOTANIKA = ["intro", "task_1_1",
                  "task_1_2", "task_1_3", "landing_result"]
TASKS_ANATOMY = ["intro", "task_2_1", "task_2_2", "task_2_3", "landing_result"]
TASKS_CYTOLOGY = ["intro", "task_3_1", "task_3_2", "task_3_3", "landing_result"]


def set_global_options(title):
    window = Tk()
    window.geometry(f"{CONFIG["window"]["width"]}x{
                    CONFIG["window"]["height"]}+{(window.winfo_screenwidth() - CONFIG["window"]["width"]) // 2}+{(window.winfo_screenheight() - CONFIG["window"]["height"]) // 2}")
    window.resizable(0, 0)
    window.title(title)
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

    return window
