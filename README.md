Bubble Sort Visualiser
A GUI Python app built with CustomTkinter and Tkinter Canvas that animates a bubble sort on a shuffled bar chart.

Concepts Used
Tkinter Canvas — create_rectangle draws each bar, redrawn every step via draw_bars().

root.after() — schedules the next comparison every 50ms, turning a fast sort into a visible animation.

Global Index Tracking — i and j track the bubble sort's pass and comparison position across calls.

Features
Animated Sorting — bars swap in real time, with the two being compared highlighted in a lighter blue.

Shuffle & Reset — reshuffles the bars and resets the sort indices so you can replay.

Completion State — the status label updates to "Sorted!" and disables the sort button when finished.

Improvements
Use after_cancel on Shuffle — shuffling mid-sort leaves the old after callback running, causing two sort loops to race; cancel any pending job first.

Merge the Advance Logic — the index-advance check runs before the swap, so the last comparison of each pass is skipped; reorder so the swap happens, then advance.

Highlight Sorted Portion — only the active pair is coloured; shading the already-sorted tail would make progress clearer.
