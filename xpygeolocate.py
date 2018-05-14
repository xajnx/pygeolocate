#!/usr/bin/env python3

import requests
from tkinter import *

base_url='https://maps.googleapis.com/maps/api/geocode/json?'

def write(statmsg):
	stext.config(state=NORMAL)
	stext.insert("end", statmsg + "\n")
	stext.see("end")
	stext.config(state=DISABLED)
	
def geo2add(geo):
    try:
        my_coord = {'latlng': geo, 'sensor':'true'}
        response = requests.get(base_url, params = my_coord)
        results = response.json()['results']
        x_add = results[0]['formatted_address']
    except (IndexError):
        write("\nerror. unable to locate geotag: " + str(geo) + "\ncheck your arguments and try again")
    else:
        write("\nApproximate address: " + str(x_add))

def add2geo(add):
    try:
        get_tag = {'address': add, 'language':'en'}
        response = requests.get(base_url, params = get_tag)
        results = response.json()['results']
        addy= results[0]['geometry']['location']
    except (IndexError):
        write("\nerror. unable to locate address: " + str(add) + "\ncheck your arguments and try again")
    else:
        write("\nApproximate geotag: " + str(addy['lat']) + str(addy['lng']))

def findit():
	upick = ebox.get()
	selection = pick.get()
	write("Querying Google Maps for address: \n" + upick)
	if selection == 1:
		add2geo(str(upick))
	else:
		geo2add(str(upick))
		
'''GUI Elements'''		
		
main = Tk()
main.title=("xPygeolocate")


titlelbl = Label(main, text="xPyGeolocate")
titlelbl.pack(fill=X, padx=20, pady=10)

'''radiobutton options''' 
pick = IntVar()
pick.set(1)

chooselbl = Label(main, text="Choose an option:", justify=LEFT, padx=20)
chooselbl.pack(anchor=W)
atogbtn = Radiobutton(main, text="Address to Geotag", padx=20, pady=5, variable=pick, value=1)
atogbtn.pack(anchor=W)
gtoabtn = Radiobutton(main, text="Geotag to Address", padx=20, pady=5, variable=pick, value=2)
gtoabtn.pack(anchor=W)

'''text-box'''
elable = Label(main, text="Enter Geotag or Address to look-up")
elable.pack()
ebox = Entry(main, bd=3, width=30)
ebox.pack(fill=X, padx=20, pady=10)

'''buttons'''
gbtn = Button(main, text="Search", command=findit)
gbtn.pack(padx=3, pady=2)
qbtn = Button(main, justify=RIGHT, text="Quit", command=quit)
qbtn.pack(side=BOTTOM,padx=3, pady=2)

'''output box'''
stext = Text(main, width=55, height=15)
stext.pack(side=BOTTOM, padx=5, pady=5)

main.mainloop()
