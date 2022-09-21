# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:13:16 2022

@author: pulle
"""

from tkinter import *

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="lavender")

name = Label(root, font=("courier",25,"bold"), bg="lavender", text="Planet Encyclopedia")
label_planet = Label(root, text="Planet: ", bg="lavender")
label_planet_name = Label(root, font=("courier",18,"bold"), bg="lavender")
label_planet_image = Label(root, bg="gold2", highlightthickness=5, borderwidth=2, relief=SOLID)
label_planet_gravity_radius = Label(root, font=("castellar"), bg="lavender")
label_planet_info = Label(root, font=("courier",10,"bold"), bg="lavender", wraplength=500)

def PlanetInfo():
    print("hi")
    
btn = Button(root, text="Show Planet Info" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

name.place(relx=0.5, rely=0.05, anchor=CENTER)
label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()