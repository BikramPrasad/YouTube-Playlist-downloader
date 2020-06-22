import urllib.request
import os
from tkinter import *
import youtube_dl
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *
from tkinter import ttk
import sys
import time

# the window size
root = Tk()
root.geometry('830x360')
root.title('Youtube Video PlayList Downloader 1.0')
root['bg'] = '#502C6C'
root.resizable(width=False, height=False)
photo = PhotoImage(file="icn.png")
root.iconphoto(False, photo)

# center Image
file = PhotoImage(file="Imgytd.png")
headImg = Label(root, image=file, bg="#502C6C")
headImg.place(x=330, y=20)

# Note
Label_3 = Label(root, text="Note:This tool cannot download Copyright content !", bg="#502C6C", fg="white",
                width=40, font=("bold", 9))
Label_3.place(x=540, y=340)


# footer
Label_2 = Label(root, text="Made By:-Bikram", bg="#502C6C", fg="white",
                width=40, font=("bold", 11)).place(x=170, y=330)


# to empty the placeholder when clicked


def userText(event):
    pastelink.delete(0, END)
    usercheck = True


mylink = StringVar()

# for taking the input
pastelink = Entry(root, width=50, textvariable=mylink, font=("verdana", 14))
pastelink.grid(row=0, column=1, padx=10, pady=10, ipady=3)
pastelink.place(x=100, y=155)
pastelink.insert(0, "Paste the Youtube link here...")
pastelink.bind("<Button>", userText)


# Checking Internet Connection
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False


if connect() is False:
    showerror("No InterNet", "Connect With the Internet!")


# for progress bar
mpb = ttk.Progressbar(root, orient="horizontal",
                      length=300, value=0, mode="determinate")
mpb.pack()
mpb["maximum"] = 100
mpb.grid(row=0, column=0, padx=100, pady=275)


def userText(event):
    pastelink.delete(0, END)
    usercheck = True


# for checking the URL
url = str(mylink.get())


def Startdownload():
    try:
        url = str(mylink.get())
        path_to_save_playlist = askdirectory()

        def my_hook(d):
            i = 0
            if d['status'] == 'finished':
                print("Done downloading")
            if d['status'] == 'downloading':
                p = d['_percent_str']
                p = p.replace('%', '')
                x = 'Percentage Downloaded:' + \
                    d['_percent_str'] + "  "+'||' + "  " + \
                    'Time Remaining:'+d['_eta_str']
                y = str(d['filename'])
                # assigning it to the title status
                mpb["value"] = float(p)
                # print(d['_percent_str'])
                vart.set(y)
                var.set(str(x))
        ydl_opts = {
            'outtmpl': path_to_save_playlist + '/%(autonumber)0003d-%(title)s.%(ext)s',
            'progress_hooks': [my_hook],
            'format': '22/18',
        }
        if path_to_save_playlist is None:
            return
        if not pastelink.get():
            showwarning("URL Missing", "Please enter the URL first!")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            showinfo("Downloaded Finished", "Downloaded Successfully")
            mylink.set("")
            var.set("")
            vart.set("")
            mpb.destroy()
            prog.set("")
            try:
                if connect() is False:
                    time.sleep(10)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)


def StartDownloadThread():
    thread = Thread(target=Startdownload)
    thread.start()


# for placing the status
var = StringVar()
vart = StringVar()
prog = StringVar()
prog.set("Status:")

vTitle = Label(root, textvariable=vart, bg="#502C6C", fg="white",
               font=("Helvetica", 9)).place(x=100, y=230)
vStatus = Label(root, textvariable=var, bg="#502C6C", fg="white",
                font=("Helvetica", 10)).place(x=100, y=245)


vprog = Label(root, textvariable=prog, bg="#502C6C", fg="white",
              font=("Helvetica", 16)).place(x=35, y=273)
# download Button
btn = Button(root, text="Download Playlist", width=21, bg='#EF4500',
             fg="black", font=("verdana", 11), command=StartDownloadThread).place(x=250, y=190)


root.mainloop()
