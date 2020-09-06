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

root = Tk()
root.title("Prayer Times")
root.geometry("1920x1080")

titlelabel = Label(root, text="Prayer Times (Crawley)")
titlelabel.config(font=("Calibri 26 underline"))
titlelabel.place(relx=0.2, y=25, anchor=CENTER)



def get_times():
	''' Gets times from the mosque website as a list and formats each item as a datetime object'''
	global times
	global times_list
	base_url = 'http://www.crawleymosque.com/'
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

	#spam = Label(root, text="checking for spam")
	#spam.place(x=460, y=110)

get_times()

def refresh():
	'''refreshes the UI once the current time reaches the Salah time'''
	now = datetime.now()
	time_now = datetime.time(now)
	curr_timelabel = Label(root, text="Current Time: " + str(time_now))
	curr_timelabel.place(relx=0.2, y=75, anchor=CENTER)

	if time_now > times[0] and time_now < times[1]:
		salah = "fajr"
		curr_salahlabel = Label(root, text="Current Salah: Fajr")
		curr_salahlabel.config(font=("Calibri, 18"))
		curr_salahlabel.place(relx=0.1, y=220, anchor=CENTER)

		next_salahlabel = Label(root, text="Sunrise: " + times[1])
		next_salahlabel.config(font=("Calibri, 18"))
		next_salahlabel.place(relx=0.3, y=220, anchor=CENTER)


	elif time_now > times[1] and time_now < times[2]:
		salah = "sunrise"
		curr_salahlabel = Label(root, text="Sunrise - No Salah")
		curr_salahlabel.config(font=("Calibri, 18"))
		curr_salahlabel.place(relx=0.1, y=220, anchor=CENTER)

		next_salahlabel = Label(root, text="Next Salah: Zuhr " + "(" + str(times[2]) + ")")
		next_salahlabel.config(font=("Calibri, 18"))
		next_salahlabel.place(relx=0.3, y=220, anchor=CENTER)


	elif time_now > times[2] and time_now < times[3]:
		salah = "zuhr"
		curr_salahlabel = Label(root, text="Current Salah: Zuhr")
		curr_salahlabel.config(font=("Calibri, 18"))
		curr_salahlabel.place(relx=0.1, y=220, anchor=CENTER)

		next_salahlabel = Label(root, text="Next Salah: Asr " + "(" + str(times[3]) + ")")
		next_salahlabel.config(font=("Calibri, 18"))
		next_salahlabel.place(relx=0.3, y=220, anchor=CENTER)


	elif time_now > times[3] and time_now < times[4]:
		salah = "asr"
		curr_salahlabel = Label(root, text="Current Salah: Asr")
		curr_salahlabel.config(font=("Calibri, 18"))
		curr_salahlabel.place(relx=0.1, y=220, anchor=CENTER)

		next_salahlabel = Label(root, text="Next Salah: Maghrib " + "(" + str(times[4]) + ")")
		next_salahlabel.config(font=("Calibri, 18"))
		next_salahlabel.place(relx=0.3, y=220, anchor=CENTER)


	elif time_now > times[4] and time_now < times[5]:
		salah = "maghrib"
		curr_salahlabel = Label(root, text="Current Salah: Maghrib")
		curr_salahlabel.config(font=("Calibri, 18"))
		curr_salahlabel.place(relx=0.1, y=220, anchor=CENTER)

		next_salahlabel = Label(root, text="Next Salah: Isha " + "(" + str(times[5]) + ")")
		next_salahlabel.config(font=("Calibri, 18"))
		next_salahlabel.place(relx=0.3, y=220, anchor=CENTER)


	elif time_now > times[5]:
		salah = "isha"
		curr_salahlabel = Label(root, text="Current Salah: Isha")
		curr_salahlabel.config(font=("Calibri, 18"))
		curr_salahlabel.place(relx=0.1, y=220, anchor=CENTER)
		
		next_salahlabel = Label(root, text="Next Salah: Fajr " + "(" + str(times[0]) + "~)")
		next_salahlabel.config(font=("Calibri, 18"))
		next_salahlabel.place(relx=0.3, y=220, anchor=CENTER)


	root.after(1000, refresh)
	root.after(1000, curr_salahlabel.pack_forget)
	root.after(1000, next_salahlabel.pack_forget)
	root.after(1000, curr_timelabel.pack_forget)



def Clock0(w, nx, ny):                                  # clock draw function
	now = datetime.now()
	time_now = datetime.time(now)
	x0 = nx/2; lx = 9*nx/20              # center and half-width of clock face
	y0 = ny/2; ly = 9*ny/20
	r0 = 0.9 * min(lx,ly)                # distance of hour labels from center
	r1 = 0.6 * min(lx,ly)                                # length of hour hand
	r2 = 0.8 * min(lx,ly)                              # length of minute hand

	w.create_oval(x0-lx, y0-ly, x0+lx, y0+ly, width=2)            # clock face
	for i in range(1,13):                               # label the clock face
		phi = pi/6 * i                              # angular position of label
		x = x0 + r0 * sin(phi)                    # Cartesian position of label
		y = y0 - r0 * cos(phi)
		w.create_text(x, y, text=str(i))                           # hour label

   #t = localtime()                                             # current time
   #print(t)
	if time_now > times[0] and time_now < times[1]:
		datetime_object = datetime.strptime(str(times_list[0]), '%I:%M %p')
	elif time_now > times[1] and time_now < times[2]:
		datetime_object = datetime.strptime(str(times_list[1]), '%I:%M %p')
	elif time_now > times[2] and time_now < times[3]:
		datetime_object = datetime.strptime(str(times_list[2]), '%I:%M %p')
	elif time_now > times[3] and time_now < times[4]:
		datetime_object = datetime.strptime(str(times_list[3]), '%I:%M %p')
	elif time_now > times[4] and time_now < times[5]:
		datetime_object = datetime.strptime(str(times_list[4]), '%I:%M %p')
	elif time_now > times[5]:
		datetime_object = datetime.strptime(str(times_list[5]), '%I:%M %p')
	t = str(datetime.time(datetime_object))
	t_s = int(t[6] + t[7])                                                       # seconds
	t_m = int(t[3] + t[4]) + t_s/60                                              # minutes
	t_h = int(t[0] + t[1]) % 12 + t_m/60                                    # hours [0,12]

	phi = pi/6 * t_h                                         # hour hand angle
	x = x0 + r1 * sin(phi)                             # position of arrowhead
	y = y0 - r1 * cos(phi)                                    # draw hour hand
	w.create_line(x0, y0, x, y, arrow=LAST, fill="red", width=3)

	phi = pi/30 * t_m                                      # minute hand angle
	x = x0 + r2 * sin(phi)                             # position of arrowhead
	y = y0 - r2 * cos(phi)                                  # draw minute hand
	w.create_line(x0, y0, x, y, arrow=LAST, fill="blue", width=2)

	phi = pi/30 * t_s                                      # second hand angle
	x = x0 + r2 * sin(phi)                             # position of arrowhead
	y = y0 - r2 * cos(phi)
	w.create_line(x0, y0 , x, y, arrow=LAST)                # draw second hand

	root.after(60000, Clock0)

def Clock(w, nx, ny):                               # clock callback function
	w.delete(ALL)                                              # delete canvas
	Clock0(w, nx, ny)                                             # draw clock
	w.after(10, Clock, w, nx, ny)                  # call callback after 10 ms

	root.after(60000, Clock)

# main


nx = 200; ny = 200                                              # canvas size
w = Canvas(root, width=nx, height=ny)         # create canvas w
w.place(relx=0.6, rely=0.7)                                                # make canvas visible

Clock(w, nx, ny)                                        # call clock function


def bring_verse(verse):
	ayahlabel = Label(root, text="Ayah of the Day")
	ayahlabel.config(font=("Calibri 15 underline"))
	ayahlabel.place(relx=0.2, rely=0.5, anchor=CENTER)
	url = 'http://api.alquran.cloud/ayah/'+str(verse)+'/editions/quran-uthmani,en.pickthall'
	json_data = requests.get(url).json()
	verse_a = json_data['data'][0]['text']
	verse_en = json_data['data'][1]['text']
	sura = json_data['data'][0]['surah']['englishName']+\
			'('+str(json_data['data'][0]['surah']['number'])+'):'+\
			str(json_data['data'][0]['numberInSurah'])
	return [verse_a,verse_en,sura]

def ayah():
	aya = random.randint(1,6237)
	link = bring_verse(aya)
	arabic = link[0]
	reshaped_text = arabic_reshaper.reshape(arabic)
	bidi_text = get_display(reshaped_text)
	newlabel = Label(root, text=bidi_text)
	newlabel.place(relx=0.2, rely=0.53, anchor=CENTER)
	englishlabel = Label(root, text=link[1], wraplength=700)
	englishlabel.place(relx=0.2, rely=0.57, anchor=CENTER)
	reflabel = Label(root, text=link[2])
	reflabel.place(relx=0.2, rely=0.60, anchor=CENTER)
	
ayah()

def hadith():
	hadithlabel = Label(root, text="Hadith of the Day")
	hadithlabel.config(font=("Calibri 15 underline"))
	hadithlabel.place(relx=0.2, rely=0.67, anchor=CENTER)

hadith()

def weathercrawley():
	weathercrawleylabel = Label(root, text="Weather (Crawley)")
	weathercrawleylabel.config(font=("Calibri 26 underline"))
	weathercrawleylabel.place(relx=0.57, y=25, anchor=CENTER)
	urlbbcc = 'https://www.bbc.co.uk/weather/2652053'
	rc = requests.get(urlbbcc)
	soupc = BeautifulSoup(rc.text, features="html.parser")

	weatherclist = []
	for headline in soupc.find_all(class_="wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque"):
	    weatherclist.append(headline.contents[0].strip())
	todayc = weatherclist[0]
	todayclabel = Label(root, text=todayc)
	todayclabel.config(font=("Calibri, 14"))
	todayclabel.place(relx=0.57, y=90, anchor=CENTER)

	temps = []
	for temp in soupc.find_all(class_="wr-value--temperature--c"):
		temps.append(str(temp))
	temps_new = [temps[0], temps[1]]
	print(temps_new)
	temps_final = []
	for i in temps_new:
		for x in i:
			if x.isnumeric():
				temps_final.append(x)
	if len(temps_final) == 3:
		final = [temps_final[0] + temps_final[1], temps_final[2]]
	elif len(temps_final) == 4:
		final = [temps_final[0] + temps_final[1], temps_final[2] + temps_final[3]]
	else:
		final = [temps_final[0], temps_final[1]]
	print(final)
	highlabel = Label(root, text="Highest temp = " + final[0])
	highlabel.config(font=("Calibri 12"))
	highlabel.place(relx=0.57, y=125, anchor=CENTER)
	lowlabel = Label(root, text="Lowest temp = " + final[1])
	lowlabel.config(font=("Calibri 12"))
	lowlabel.place(relx=0.57, y=155, anchor=CENTER)

weathercrawley()

def weatherlondon():
	weatherlondonlabel = Label(root, text="Weather (London)")
	weatherlondonlabel.config(font=("Calibri 26 underline"))
	weatherlondonlabel.place(relx=0.8, y=25, anchor=CENTER)
	urlbbcl = 'https://www.bbc.co.uk/weather/2643743'
	rl = requests.get(urlbbcl)
	soupl = BeautifulSoup(rl.text, features="html.parser")

	weatherllist = []
	for headline in soupl.find_all(class_="wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque"):
	    weatherllist.append(headline.contents[0].strip())
	todayl = weatherllist[0]
	todayllabel = Label(root, text=todayl)
	todayllabel.config(font=("Calibri, 14"))
	todayllabel.place(relx=0.8, y=90, anchor=CENTER)

	temps = []
	for temp in soupl.find_all(class_="wr-value--temperature--c"):
		temps.append(str(temp))

	temps_new = [temps[0], temps[1]]

	temps_final = []
	for i in temps_new:
		for x in i:
			if x.isdigit():
				temps_final.append(x)

	if len(temps_final) == 3:
		final = [temps_final[0] + temps_final[1], temps_final[2]]
	elif len(temps_final) == 4:
		final = [temps_final[0] + temps_final[1], temps_final[2] + temps_final[3]]
	else:
		final = [temps_final[0], temps_final[1]]

	highlabel = Label(root, text="Highest temp = " + final[0])
	highlabel.config(font=("Calibri 12"))
	highlabel.place(relx=0.8, y=125, anchor=CENTER)
	lowlabel = Label(root, text="Lowest temp = " + final[1])
	lowlabel.config(font=("Calibri 12"))
	lowlabel.place(relx=0.8, y=155, anchor=CENTER)

weatherlondon()

def tasks():
	tasks = requests.get(
    "https://api.todoist.com/rest/v1/tasks",
	params={
        "filter": "Today"
    },
    headers={
        "Authorization": "Bearer 1426994c24642fa2552d2436e628e6e909ad03d1"
    }).json()

	print(tasks)
	tasks_formatted = []

	for i in tasks:
		tasks_formatted.append(i["content"])
	print(tasks_formatted)

tasks()

root.after(1000, refresh)
root.after(60000, Clock0)
root.after(60000, Clock)
root.mainloop()