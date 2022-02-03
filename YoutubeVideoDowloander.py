from tkinter import *
from tkinter import ttk
import tkinter as tk


from pytube import YouTube
root = Tk() #our window


root.geometry("300x50+600+250") #window size
root.config(background='black') #window background color
root.title("Youtube Video Dowloander") #our window's name


path = r'C:\Users\Ekiz\PycharmProjects\QuarCode\venv' #video path
url = Entry(root) #it's an input from user
url.pack() #closed Entry method


def dowloand(): #dowloand Method for button

    value = url.get()
    # we're changing the our input
    # Because tkinter lib. does'nt understand with Entry method

    if value != '': #if link is not empty
        video = YouTube(value) #we're finding ur video from value(user input)
        print("Video indiriliyor...\n")
        videoa = video.streams.get_highest_resolution() #this method for dowloading with hight resolution.
        #you should use this ---> videoa = video.streams.get_lowe_resolution() this is for low Quality
        videoa.download(path) #and finally, we are dowloened

    elif value == '': #if value's empty
        print("değer giriniz..")


button = Button(root) #we're creating a button
button.config(text="Dowloand", bg="black", fg="white", command=dowloand) #button settings
button.pack() #close the button


root.mainloop() 
