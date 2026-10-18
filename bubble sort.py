import tkinter as tk
import random

NUM_BARS = 30
BAR_WIDTH = 20
CANVAS_HEIGHT = 400
CANVAS_WIDTH = NUM_BARS * BAR_WIDTH

bars = list(range(1, NUM_BARS + 1))
random.shuffle(bars)

i = 0
j = 0


def draw_bars(highlight=()):
    canvas.delete("all")
    for k, value in enumerate(bars):
        x1 = k * BAR_WIDTH
        y1 = CANVAS_HEIGHT - value * 10
        x2 = x1 + BAR_WIDTH
        y2 = CANVAS_HEIGHT
        colour = "#3b8ed0" if k in highlight else "#1f6aa5"
        canvas.create_rectangle(x1, y1, x2, y2, fill=colour, outline="#0d1b2a")


def sort():
    global i, j

    if j >= len(bars) - i - 1:
        i += 1
        j = 0
        if i >= len(bars) - 1:
            draw_bars()
            status_label.config(text="Sorted!")
            sort_btn.config(state="disabled")
            return

    if bars[j] > bars[j + 1]:
        bars[j], bars[j + 1] = bars[j + 1], bars[j]

    draw_bars(highlight=(j, j + 1))
    j += 1
    root.after(50, sort)


def shuffle():
    global i, j
    random.shuffle(bars)
    i = 0
    j = 0
    draw_bars()
    status_label.config(text="Ready to sort")
    sort_btn.config(state="normal")


root = tk.Tk()
root.title("Bubble Sort")
root.configure(bg="#0d1b2a")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                   bg="#0d1b2a", highlightthickness=0)
canvas.pack(pady=10)

button_row = tk.Frame(root, bg="#0d1b2a")
button_row.pack(pady=10)

sort_btn = tk.Button(button_row, text="Sort", width=15,
                     bg="#1f6aa5", fg="white", activebackground="#3b8ed0",
                     relief="flat", command=sort)
sort_btn.pack(side="left", padx=5)

shuffle_btn = tk.Button(button_row, text="Shuffle", width=15,
                        bg="#1f6aa5", fg="white", activebackground="#3b8ed0",
                        relief="flat", command=shuffle)
shuffle_btn.pack(side="left", padx=5)

status_label = tk.Label(root, text="Ready to sort",
                        font=("Arial", 14), bg="#0d1b2a", fg="#8ecae6")
status_label.pack(pady=5)

draw_bars()
root.mainloop()