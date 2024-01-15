from tkinter import *
from PIL import Image as PilImage, ImageTk

window = Tk()
window_width = 1000
window_height = 1000
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
window.resizable(0, 0)
window.title("Sandbox")
window.rowconfigure(0, minsize=1000, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

frm_task_3_1 = Frame(window, bg="lightgreen")
frm_task_3_1.grid(row=0, column=0)
frm_task_3_1.grid()

def display_images():
    # Add the images to the canvas
    canvas.create_image(0, 0, anchor="nw", image=photo1)
    canvas.create_image(0, 0, anchor="nw", image=photo2)
    # Now the canvas with the images will be displayed.
    canvas.pack()

canvas = Canvas(frm_task_3_1, width=500, height=500)

img1 = PilImage.open("images/cytology/клетка.png")
photo1 = ImageTk.PhotoImage(img1)

img2 = PilImage.open("images/cytology/ядро.png")
photo2 = ImageTk.PhotoImage(img2)

button = Button(frm_task_3_1, text="Display Images", command=display_images)
button.pack()


# =====
if __name__ == "__main__":
    window.mainloop()