#!/usr/bin/env python3
#Created by Tegar Dev
#AsukaDev all right reversed
#Give me credit if you modify
import requests, bs4
from tkinter import *
from tkinter import messagebox


def nextdate(name):
    try:
        req = requests.get("https://www.episodate.com/tv-show/" + name)
        soup = bs4.BeautifulSoup(req.text, 'html.parser')
        date = soup.find('div', {'class': 'countdown'})
        next_episode = str(date)[34:63]
        next_episode = next_episode.replace('"', "")
        next_episode = next_episode.replace("status", "")
        next_episode = next_episode.replace("/div><", "")
        next_episode = next_episode.replace("class=><a href=/sear",
                                            "Show not Found")
        if (next_episode == None):
            check = soup.find('div', {
                'class': 'countdown'
            }).find('div', {"class": "status"})
            check_status = check.getText()
            return check_status
        else:
            return next_episode
    except:
        return "Tidak Ada!!"


def function():
    value = nextdate(entry.get().lower())
    mylabel = Label(frame, text=entry.get() + " " + value)
    mylabel.pack()
    messagebox.showinfo("Tanggal tayang berikutnya : " + entry.get(), value)


value = ""
root = Tk()
root.title("Episode Selanjutnya")
frame = LabelFrame(root,
                   text="Anime Tracker\nBy AsukaDev Official\nCoded : Tegar Dev\nCari tanggal episode anime berikutnya :",
                   padx=5,
                   pady=5)
frame.pack(padx=10, pady=10)
entry = Entry(frame, width=25)
entry.pack()
button = Button(frame, text="cari", command=function).pack()
root.mainloop()