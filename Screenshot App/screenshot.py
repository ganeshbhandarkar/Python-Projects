import time
import pyautogui as ss
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name = "C:/Users/KIIT/Coding/Python-Projects/Screenshot App/screenshots//{}.png".format(name)
    #time.sleep(3)
    img = ss.screenshot(name)
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take Screenshot",
    command=screenshot
)
button.pack(side = tk.LEFT)

close = tk.Button(
    frame,
    text = "Quit",
    command=quit
)
close.pack(side = tk.RIGHT)

root.mainloop()