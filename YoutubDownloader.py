from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("تحميل الفيديوهات من يوتيوب")
root.geometry("350x400") 
root.columnconfigure(0,weight=1)

ytdLabel = Label(root,text="أدخل رابط الفيديو",font=("jost",15))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

ytdError = Label(root,text="",fg="green",font=("jost",10))
ytdError.grid()

saveLabel = Label(root,text="إختر مكان حفظ الفيديو",font=("jost",15,"bold"))
saveLabel.grid()

saveEntry = Button(root,width=10,bg="Green",fg="white",text="إختر المسار",command=openLocation)
saveEntry.grid()

locationError = Label(root,text="",fg="red",font=("jost",10))
locationError.grid()

ytdQuality = Label(root,text="إختر الجودة ",font=("jost",15))
ytdQuality.grid()

choices = ["720p","144p","الصوت فقط"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

downloadbtn = Button(root,text="تحميل",width=10,bg="Green",fg="white",command=DownloadVideo)
downloadbtn.grid()

developerlabel = Label(root,text="تم التطوير من طرف: عدنان زيادي ",font=("jost",15))
developerlabel.grid()
root.mainloop()
