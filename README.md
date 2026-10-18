This README is made with AI

📊 Python Bubble Sort Visualiser
A modern, dark-themed desktop visualization of the bubble sort algorithm built with Python, CustomTkinter, and Tkinter Canvas. The app displays a shuffled set of bars and animates the sorting process step by step, highlighting the two bars being compared at each step. It's a great beginner-to-intermediate project for learning about algorithms, animations, canvas drawing, and GUI programming in Python.

📖 Python Bubble Sort Visualiser
The Python Bubble Sort Visualiser is a graphical application that demonstrates how bubble sort works in real time. When the app starts, a set of 30 bars of varying heights is shuffled randomly and drawn on a canvas.

Pressing Sort begins the animation. At each step, the two bars being compared are highlighted in a lighter blue. If they're out of order, they swap, and the animation continues. Once the entire list is sorted, the bars remain in ascending order and the status label displays "Sorted!".

Pressing Shuffle generates a new random arrangement and resets the sort state, allowing the user to watch the algorithm run again from scratch.

The interface uses CustomTkinter for the themeable buttons and labels, styled in a custom dark navy palette (#0d1b2a background), while the bars themselves are drawn on a standard Tkinter Canvas — a classic approach for smooth, low-level 2D drawing.

This project is ideal for anyone learning how sorting algorithms work visually, or for beginners exploring how to combine canvas graphics with a modern GUI.

✨ Features
30-bar visualization – Each bar's height represents its value (1–30).

Random shuffle on start – Bars are shuffled with random.shuffle() for a fresh arrangement.

Step-by-step bubble sort animation – The algorithm runs one comparison at a time using root.after().

Live comparison highlight – The two bars being compared are drawn in a lighter blue.

Automatic sorting detection – The animation stops once the list is fully sorted.

"Sorted!" status message – Confirms completion and disables the Sort button.

Shuffle button – Generates a new random arrangement and re-enables sorting.

Custom dark navy palette – Consistent styling across canvas, buttons, and labels.

Modern rounded buttons – CustomTkinter buttons with custom hover colors.

No blocking loops – Uses scheduled callbacks so the GUI stays responsive.

Single-window, self-contained app – No external files or assets required.

🛠️ What It Uses
Language & Library
Python 3

CustomTkinter – A modern, themeable Tkinter wrapper for buttons and labels.

Install with: pip install customtkinter

Tkinter – For the Canvas widget that draws the bars.

random – For shuffling the bars.

Key Variables
Variable	Purpose
bars	A list of values representing each bar's height, shuffled at startup.
i	The outer loop index for bubble sort (tracks how many passes have completed).
j	The inner loop index for bubble sort (tracks the current comparison position).
NUM_BARS	The number of bars to display (30).
BAR_WIDTH	The width of each bar in pixels (20).
CANVAS_HEIGHT / CANVAS_WIDTH	The dimensions of the drawing canvas.
Key Functions
Function	Purpose
draw_bars(highlight=())	Clears the canvas and redraws all bars, highlighting the indices in highlight.
sort()	Performs one comparison/swap step of bubble sort, then schedules itself again with root.after().
shuffle()	Randomly reshuffles the bars, resets the sort indices, and re-enables sorting.
CustomTkinter & Tkinter Widgets Used
ctk.CTk() – Main application window.

ctk.CTkFrame – Container for the button row.

ctk.CTkButton – The Sort and Shuffle buttons.

ctk.CTkLabel – Status label.

tk.Canvas – The drawing surface for the bars.

ctk.set_appearance_mode("dark") – Enables dark mode.

ctk.set_default_color_theme("blue") – Applies the blue theme.

canvas.create_rectangle() – Draws each bar.

canvas.delete("all") – Clears the canvas before redrawing.

root.after(50, sort) – Schedules the next animation frame.

root.mainloop() – Starts the event loop.

Python Concepts Demonstrated
Bubble sort algorithm – Classic O(n²) sorting with nested loops.

Animating with callbacks – Using root.after() to step through the algorithm without blocking the GUI.

Tuple swapping – bars[j], bars[j + 1] = bars[j + 1], bars[j].

Global variables – Sharing i and j across functions.

Default arguments – highlight=() for optional highlighting.

List methods – random.shuffle() for randomization.

enumerate() – Getting both index and value while drawing bars.

Conditional coloring – Choosing bar colors based on highlighted indices.

Widget state management – Enabling/disabling the Sort button.

Event-driven programming – Buttons trigger functions.

Hex colors – Custom palette styling.

Built-in Functions Used
range() – Generating the initial 1–30 bar list.

enumerate() – Iterating with indices.

len() – Checking sort boundaries.

random.shuffle() – Shuffling bar order.

list() – Creating the initial list.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
bubble_sort_visualiser.py
Then install the required library:

bash
pip install customtkinter
▶️ How to Run
Make sure you have Python 3 installed (python.org).

Install CustomTkinter:

bash
pip install customtkinter
Save the code as bubble_sort_visualiser.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python bubble_sort_visualiser.py
Press Sort to watch the bars sort themselves. Press Shuffle to try again with a new random arrangement.

🐍 Made with Python
This project is written in Python 3 and uses CustomTkinter for the buttons and labels plus Tkinter's Canvas for the animated bars. It's a clean, practical example of how classic algorithms can be animated with simple callback scheduling — no game engines or animation libraries required.

Whether you're a beginner learning how bubble sort works or someone exploring how to visualize algorithms, this project is a great starting point.

💡 Possible Future Improvements
Adjustable speed – Add a slider to control the animation delay.

Adjustable bar count – Let the user choose between 10, 30, or 100 bars.

Other sorting algorithms – Add options for selection sort, insertion sort, merge sort, or quicksort.

Comparison/swap counters – Display stats for how many comparisons and swaps occurred.

Sorting sound – Play a tone whose pitch depends on bar height (like "sorting sounds" videos).

Color gradient bars – Color bars based on their value for a more striking visual.

Pause/Resume button – Pause the animation mid-sort.

Reset button – Restore the original shuffled order.

Highlight sorted portions – Show the growing sorted section in a different color.

Responsive canvas – Resize the canvas with the window.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.
