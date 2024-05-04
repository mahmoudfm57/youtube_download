from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import threading

root = Tk()
root.title("youtube download")
root.geometry('600x320')
root.resizable(False, False)

#my Functoin
def browse():
    directory = filedialog.askdirectory(title='Save Video')
    folderLink.delete(0, "end")
    folderLink.insert(0, directory)
def down_yt():
    staus.config(text="Status: Downloading...")
    link=ytLink.get()
    folder=folderLink.get()
    YouTube(link,on_complete_callback=finsh).streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download(folder)

def finsh(stream=None,chunk=None,filename=None,remaining=None):
    staus.config(text="Status: Complete")
#youtube loge,
ytlogo=PhotoImage(file="download.png").subsample(2)
logo=Label(root,image=ytlogo)
logo.place(relx=0.5, rely=0.25, anchor="center")
#youtube Link

ytlabel= Label(root,text="Youtube link")
ytlabel.place(x=20,y=150)

ytLink= Entry(root,width=60)
ytLink.place(x=140,y=150)

#download folder

folderLabel=Label(root,text="Download Folder")
folderLabel.place(x=25,y=183)

folderLink=Entry(root,width=50)
folderLink.place(x=140,y=183)

#Browae Button

browse = Button(root,text="Browse",command=browse)
browse.place(x=455,y=180)


#download Button

Download = Button(root,text="Download",command=threading.Thread(target=down_yt).start)
Download.place(x=280,y=220)

#Status
staus= Label(root,text="Status Readt",font="Calibre 10 italic",fg="blue",bg="white",anchor="w")
staus.place(rely=1, anchor="sw",relwidth=1)

root.mainloop()