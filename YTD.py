
import tkinter as tk
from tkinter import *
from pytube import YouTube





def download():
	url = text_box.get(1.0, "end-1c")
	lbl.config(text = "Provided Input: "+url)
	print(url)
	#url = 'https://www.youtube.com/watch?v=h--P8HzYZ74&ab_channel=ZEDDVEVO'
	my_video = YouTube(url)
	my_video = my_video.streams.get_highest_resolution()
	my_video.download()
	lbl.config(text = "Sucess!")
			



window = tk.Tk()
window.geometry("500x500")
window.title("Youtube video downloader")



text_box = tk.Text(width=25,
    height=1,)
text_box.pack(padx=50, pady=30)

button = tk.Button(
    text="Download!",
    width=22,
    height=1,
    bg="blue",
    fg="yellow",
command=lambda: download(),
)
button.pack(padx=50) 

lbl = tk.Label(window, text = "")
lbl.pack(padx=50, pady=10)


window.mainloop()