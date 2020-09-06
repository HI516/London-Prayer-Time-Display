# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from tkinter import *
from datetime import datetime
import time
import random, requests
import arabic_reshaper
from bidi.algorithm import get_display
from math import *
import http.client

root = Tk()
root.title("Prayer Times")
root.geometry("1920x1080")

titlelabel = Label(root, text="Prayer Times (London Unified Timetable)")
titlelabel.config(font=("Calibri 26 underline"))
titlelabel.place(relx=0.5, y=25, anchor=CENTER)


def get_times():
    """ Gets times from the mosque website as a list and formats each item as a datetime object"""
    global times
    global times_list
    base_url = "http://www.crawleymosque.com/"
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, features="html.parser")

    times_list = []
    for salah_time in soup.find_all(class_="prayer-start"):
        times_list.append(salah_time.contents[0].strip())

    print(times_list)
    times = []
    for i in times_list:
        datetime_object = datetime.strptime(i, "%I:%M %p")
        just_time = datetime.time(datetime_object)
        times.append(just_time)

    print(times)

    # spam = Label(root, text="checking for spam")
    # spam.place(x=460, y=110)


get_times()


def refresh():
    """refreshes the UI once the current time reaches the Salah time"""
    now = datetime.now()
    time_now = datetime.time(now)
    curr_timelabel = Label(root, text="Current Time: " + str(time_now)[:8])
    curr_timelabel.config(font=("Calibri 16"))
    curr_timelabel.place(relx=0.5, rely=0.065, anchor=CENTER)

    if time_now > times[0] and time_now < times[1]:
        curr_salahlabel = Label(root, text="Current Salah: Fajr")
        curr_salahlabel.config(font=("Calibri, 18"))
        curr_salahlabel.place(relx=0.1, rely=0.29, anchor=CENTER)

        next_salahlabel = Label(root, text="Sunrise: " + times[1])
        next_salahlabel.config(font=("Calibri, 18"))
        next_salahlabel.place(relx=0.3, rely=0.29, anchor=CENTER)

    elif time_now > times[1] and time_now < times[2]:
        curr_salahlabel = Label(root, text="Sunrise - No Salah")
        curr_salahlabel.config(font=("Calibri, 18"))
        curr_salahlabel.place(relx=0.1, rely=0.29, anchor=CENTER)

        next_salahlabel = Label(
            root, text="Next Salah: Zuhr " + "(" + str(times[2]) + ")"
        )
        next_salahlabel.config(font=("Calibri, 18"))
        next_salahlabel.place(relx=0.3, rely=0.29, anchor=CENTER)

    elif time_now > times[2] and time_now < times[3]:
        curr_salahlabel = Label(root, text="Current Salah: Zuhr")
        curr_salahlabel.config(font=("Calibri, 18"))
        curr_salahlabel.place(relx=0.1, rely=0.29, anchor=CENTER)

        next_salahlabel = Label(
            root, text="Next Salah: Asr " + "(" + str(times[3]) + ")"
        )
        next_salahlabel.config(font=("Calibri, 18"))
        next_salahlabel.place(relx=0.3, rely=0.29, anchor=CENTER)

    elif time_now > times[3] and time_now < times[4]:
        curr_salahlabel = Label(root, text="Current Salah: Asr")
        curr_salahlabel.config(font=("Calibri, 18"))
        curr_salahlabel.place(relx=0.1, rely=0.29, anchor=CENTER)

        next_salahlabel = Label(
            root, text="Next Salah: Maghrib " + "(" + str(times[4]) + ")"
        )
        next_salahlabel.config(font=("Calibri, 18"))
        next_salahlabel.place(relx=0.3, rely=0.29, anchor=CENTER)

    elif time_now > times[4] and time_now < times[5]:
        curr_salahlabel = Label(root, text="Current Salah: Maghrib")
        curr_salahlabel.config(font=("Calibri, 18"))
        curr_salahlabel.place(relx=0.1, rely=0.29, anchor=CENTER)

        next_salahlabel = Label(
            root, text="Next Salah: Isha " + "(" + str(times[5]) + ")"
        )
        next_salahlabel.config(font=("Calibri, 18"))
        next_salahlabel.place(relx=0.3, rely=0.29, anchor=CENTER)

    elif time_now > times[5]:
        curr_salahlabel = Label(root, text="Current Salah: Isha")
        curr_salahlabel.config(font=("Calibri, 18"))
        curr_salahlabel.place(relx=0.1, rely=0.29, anchor=CENTER)

        next_salahlabel = Label(
            root, text="Next Salah: Fajr " + "(" + str(times[0]) + "~)"
        )
        next_salahlabel.config(font=("Calibri, 18"))
        next_salahlabel.place(relx=0.3, rely=0.29, anchor=CENTER)

    root.after(1000, refresh)
    root.after(1000, curr_salahlabel.pack_forget)
    root.after(1000, next_salahlabel.pack_forget)
    root.after(1000, curr_timelabel.pack_forget)


def all_salah():
    fajrlabel = Label(root, text="Fajr: " + times_list[0])
    fajrlabel.config(font=("Calibri, 18"))
    fajrlabel.place(relx=0.5, rely=0.29, anchor=CENTER)

    sunriselabel = Label(root, text="Sunrise: " + times_list[1])
    sunriselabel.config(font=("Calibri, 18"))
    sunriselabel.place(relx=0.5, rely=0.33, anchor=CENTER)

    zuhrlabel = Label(root, text="Zuhr: " + times_list[2])
    zuhrlabel.config(font=("Calibri, 18"))
    zuhrlabel.place(relx=0.5, rely=0.37, anchor=CENTER)

    asrlabel = Label(root, text="Asr: " + times_list[3])
    asrlabel.config(font=("Calibri, 18"))
    asrlabel.place(relx=0.5, rely=0.41, anchor=CENTER)

    maghriblabel = Label(root, text="Maghrib: " + times_list[4])
    maghriblabel.config(font=("Calibri, 18"))
    maghriblabel.place(relx=0.5, rely=0.45, anchor=CENTER)

    ishalabel = Label(root, text="Isha: " + times_list[5])
    ishalabel.config(font=("Calibri, 18"))
    ishalabel.place(relx=0.5, rely=0.49, anchor=CENTER)


all_salah()


def masjidinfo():
    masjidinfolabel = Label(root, text="Masjid information")
    masjidinfolabel.config(font=("Calibri 18 underline"))
    masjidinfolabel.place(relx=0.87, rely=0.062, anchor=CENTER)


masjidinfo()


def Clock0(w, nx, ny):  # clock draw function
    now = datetime.now()
    time_now = datetime.time(now)
    x0 = nx / 2
    lx = 9 * nx / 20  # center and half-width of clock face
    y0 = ny / 2
    ly = 9 * ny / 20
    r0 = 0.9 * min(lx, ly)  # distance of hour labels from center
    r1 = 0.6 * min(lx, ly)  # length of hour hand
    r2 = 0.8 * min(lx, ly)  # length of minute hand

    w.create_oval(x0 - lx, y0 - ly, x0 + lx, y0 + ly, width=2)  # clock face
    for i in range(1, 13):  # label the clock face
        phi = pi / 6 * i  # angular position of label
        x = x0 + r0 * sin(phi)  # Cartesian position of label
        y = y0 - r0 * cos(phi)
        w.create_text(x, y, text=str(i))  # hour label

        # t = localtime()                                             # current time
        # print(t)
    if time_now > times[0] and time_now < times[1]:
        datetime_object = datetime.strptime(str(times_list[0]), "%I:%M %p")
    elif time_now > times[1] and time_now < times[2]:
        datetime_object = datetime.strptime(str(times_list[1]), "%I:%M %p")
    elif time_now > times[2] and time_now < times[3]:
        datetime_object = datetime.strptime(str(times_list[2]), "%I:%M %p")
    elif time_now > times[3] and time_now < times[4]:
        datetime_object = datetime.strptime(str(times_list[3]), "%I:%M %p")
    elif time_now > times[4] and time_now < times[5]:
        datetime_object = datetime.strptime(str(times_list[4]), "%I:%M %p")
    elif time_now > times[5]:
        datetime_object = datetime.strptime(str(times_list[5]), "%I:%M %p")
    t = str(datetime.time(datetime_object))
    t_s = int(t[6] + t[7])  # seconds
    t_m = int(t[3] + t[4]) + t_s / 60  # minutes
    t_h = int(t[0] + t[1]) % 12 + t_m / 60  # hours [0,12]

    phi = pi / 6 * t_h  # hour hand angle
    x = x0 + r1 * sin(phi)  # position of arrowhead
    y = y0 - r1 * cos(phi)  # draw hour hand
    w.create_line(x0, y0, x, y, arrow=LAST, fill="red", width=3)

    phi = pi / 30 * t_m  # minute hand angle
    x = x0 + r2 * sin(phi)  # position of arrowhead
    y = y0 - r2 * cos(phi)  # draw minute hand
    w.create_line(x0, y0, x, y, arrow=LAST, fill="blue", width=2)

    phi = pi / 30 * t_s  # second hand angle
    x = x0 + r2 * sin(phi)  # position of arrowhead
    y = y0 - r2 * cos(phi)
    w.create_line(x0, y0, x, y, arrow=LAST)  # draw second hand


def Clock(w, nx, ny):  # clock callback function
    w.delete(ALL)  # delete canvas
    Clock0(w, nx, ny)  # draw clock
    # print("updating clock...")
    w.after(10, Clock, w, nx, ny)  # call callback after 10 ms


# main


nx = 200
ny = 200  # canvas size
w = Canvas(root, width=nx, height=ny)  # create canvas w
w.place(relx=0.1, rely=0.4, anchor=CENTER)  # make canvas visible

Clock(w, nx, ny)  # call clock function


def bring_verse(verse):
    ayahlabel = Label(root, text="Ayah of the Day")
    ayahlabel.config(font=("Calibri 15 underline"))
    ayahlabel.place(relx=0.5, rely=0.6, anchor=CENTER)
    url = (
        "http://api.alquran.cloud/ayah/"
        + str(verse)
        + "/editions/quran-uthmani,en.asad"
    )
    json_data = requests.get(url).json()
    verse_a = json_data["data"][0]["text"]
    verse_en = json_data["data"][1]["text"]
    sura = (
        json_data["data"][0]["surah"]["englishName"]
        + "("
        + str(json_data["data"][0]["surah"]["number"])
        + "):"
        + str(json_data["data"][0]["numberInSurah"])
    )
    return [verse_a, verse_en, sura]


def ayah():
    aya = random.randint(1, 6237)
    link = bring_verse(aya)
    arabic = link[0]
    reshaped_text = arabic_reshaper.reshape(arabic)
    bidi_text = get_display(reshaped_text)
    newlabel = Label(root, text=bidi_text)
    newlabel.place(relx=0.5, rely=0.63, anchor=CENTER)
    englishlabel = Label(root, text=link[1], wraplength=700)
    englishlabel.place(relx=0.5, rely=0.67, anchor=CENTER)
    reflabel = Label(root, text=link[2])
    reflabel.place(relx=0.5, rely=0.7, anchor=CENTER)


ayah()


def hadith():
    hadithlabel = Label(root, text="Hadith of the Day")
    hadithlabel.config(font=("Calibri 15 underline"))
    hadithlabel.place(relx=0.5, rely=0.77, anchor=CENTER)
    # conn = http.client.HTTPSConnection("api.sunnah.com")

    # payload = "{}"

    # headers = { 'x-api-key': "SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk" }

    # conn.request("GET", "/v1/hadiths/random", payload, headers)

    # res = conn.getresponse()
    # print(res.read())


hadith()

root.after(1000, refresh)
root.mainloop()
