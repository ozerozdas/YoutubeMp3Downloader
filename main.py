from pytube import YouTube
from tkinter import messagebox
import customtkinter
import os

def DownloadVideo(url, destination = './output'):
	yt = YouTube(url)
	video = yt.streams.filter(only_audio=True).first()
	out_file = video.download(output_path=destination)

	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'
	os.rename(out_file, new_file) 
 
	file = new_file.split('/')[-1]
 
	messagebox.showinfo('Success', f'{file} has been successfully downloaded.')
	os.system(f'open {destination}')
	return file

def render():
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.title("Youtube Mp3 Downloader")

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width/2) - (400/2)
    y = (screen_height/2) - (240/2)
    app.geometry(f'400x240+{int(x)}+{int(y)}')

    entry = customtkinter.CTkEntry(app, placeholder_text="Enter the URL of the video you want to download", width=360)
    entry.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

    def button_function():
        if entry.get() == "":
            messagebox.showerror("Error", "Please enter a valid URL.")
            return
        
        DownloadVideo(entry.get())
        entry.delete(0, customtkinter.END)

    button = customtkinter.CTkButton(master=app, text="Download", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    app.mainloop()
    
render()