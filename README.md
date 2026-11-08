## Bubble Sort Visualiser
A desktop bubble sort visualiser built with CustomTkinter and a Tkinter Canvas. It draws a shuffled list of values as bars and animates the bubble sort process one comparison at a time.

## Features
Bar Chart Display — Draws 30 bars on a tk.Canvas, with each bar's height representing its value.

Random Shuffle — Randomly reorders the values at startup and whenever Shuffle is pressed.

Step-by-Step Sort — Compares and swaps adjacent bars one pair at a time, updating the display after each step.

Highlighting — Shows the two bars currently being compared in a lighter blue.

Animated Delay — Uses root.after(50, sort) so the sorting is visible rather than instant.

Sort Complete — Disables the Sort button and shows "Sorted!" when the list is in order.

Custom Theme — Dark navy background with blue accents applied to both the Canvas and CustomTkinter widgets.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `customtkinter` | Buttons and labels |
| `tkinter.Canvas` | Draws the bars |
| `random.shuffle()` | Randomises the bar order |
| `root.after()` | Schedules the next sort step |
| `global` | Tracks the `i` and `j` loop indices |
| `create_rectangle()` | Renders each bar |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install CustomTkinter by running pip install customtkinter.

Save the code as bubble_sort.py.

Open a terminal in the folder containing the file.

Run python bubble_sort.py.

Press Sort to watch the animation, then Shuffle to try again with a new order.

## Improvements
Add a speed slider — the 50ms delay is hardcoded; a slider that changes the value passed to root.after() would let the user slow the animation down or speed it up.

Reset the indices on Shuffle — shuffle() resets i and j, but if the Sort button is pressed while a sort is mid-way through, the pending root.after call still fires and continues the old sort; cancelling the scheduled call with root.after_cancel() on shuffle would prevent overlapping sorts.

