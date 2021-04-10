from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

def openLocation():                                                                                          #FUN FOR FILE LOCATION
    global Folder_Name
    Folder_Name = filedialog.askdirectory()

    if(len(Folder_Name) > 1):
        locationError.config(text = Folder_Name , fg = "green")
    else:
        locationError.config(text = "Please Choose Folder!!", fg = "green")

def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url) > 1):
        ytdError.config(text = "")
        yt = YouTube(url)                                                                                   #creating an obj of youtube and paste url

        if(choice == choices[0]):
            select = yt.streams.filter(progressive = True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive = True, file_extension="mp4").last()

        elif(choice == choices[2]):  
            select = yt.streams.filter(only_audio=True).first()  

        else:
            ytdError.config(text = "Paste link again!!", fg = "red")

    select.download(Folder_Name)                                                                           #download fun
    ytdError.config(text = "Download completed!!")


    
root = Tk()                         #creating obj of tkinter
root.title("YT Downloader")
root.geometry("350x400")            #giving height nd width
root.columnconfigure(0,weight = 1)  #content in center


ytdLabel = Label(root,text = "Enter the URL of the Video", font = ("jost",15))
ytdLabel.grid()

ytdEntryVar = StringVar()                                                                                 #creating a text box
ytdEntry = Entry(root, width = 50, textvariable = ytdEntryVar)
ytdEntry.grid()

ytdError = Label(root, text ="Msg area", fg = "deepskyblue", font = ("MS Sans Serif",10))                 #showing error msg
ytdError.grid()

saveLable = Label(root, text = "Save the Video File", font = ("MS Sans Serif",13))

saveEntry = Button(root, width = 10 , bg = "green", fg = "white", text = "Choose Path" , command = openLocation)           #Creating Choose_file button
saveEntry.grid()

locationError = Label(root, text = "Msg area", fg = "deepskyblue", font = ("MS Sans Serif",10))           #Creating path error msg
locationError.grid()

ytQuality = Label(root, text = "Select Quality", font = ("MS Sans Serif",13))
ytQuality.grid()

choices = ["720p", "144p", "Only Audio"]
ytdchoices = ttk.Combobox(root, values = choices)                                                           #ttk is object of tkinter
ytdchoices.grid()

downloadbtn = Button(root, width = 10 , bg = "green", fg = "white", text = "Download" , command = DownloadVideo)           #Creating Choose_file button
downloadbtn.grid()

developerLabel = Label(root, text = "Developed with ❤ by Himanshu", font = ("MS Sans Serif",15))
developerLabel.grid()

root.mainloop()


