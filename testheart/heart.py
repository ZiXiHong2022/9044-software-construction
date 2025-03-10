#!/usr/bin/env python3
import tkinter as tk

def draw_heart(canvas):
    canvas.create_arc(50, 50, 150, 150, start=0, extent=180, fill='red', outline='red')
    canvas.create_arc(150, 50, 250, 150, start=0, extent=180, fill='red', outline='red')
    canvas.create_polygon(50, 100, 150, 250, 250, 100, fill='red', outline='red')

root = tk.Tk()
root.title("Heart with Tkinter")

canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.pack()

draw_heart(canvas)

root.mainloop()