from pytube import YouTube
from tkinter import messagebox
import tkinter
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
    m = tkinter.Tk()
    print(m.tk.call("info", "patchlevel"))
    m.title('Youtube Video Downloader')
    
    screen_width = m.winfo_screenwidth()
    screen_height = m.winfo_screenheight()
    x = (screen_width/2) - (500/2)
    y = (screen_height/2) - (200/2)
    m.geometry(f'500x200+{int(x)}+{int(y)}')
    
    m.resizable(False, False)
    m.configure(
        bg='black'
	)
    
    label_1 = tkinter.Label(
        m,
        text='Enter the URL of the video you want to download: ',
        bg='black',
        fg='white',
        font='Arial 12',
        padx=10,
        pady=20
	)
    label_1.pack()
    
    input_field = tkinter.Entry(
        m,
        width=50,
        bg='black',
        fg='white',
        font='Arial 12',
        bd=0,
	)
    input_field.pack()
    
    download_button = tkinter.Button(
        m,
        text='Download',
        command=lambda: DownloadVideo(input_field.get()),
        bg='black',
        font='Arial 12',
        padx=10,
        pady=5
	)
    download_button.pack()
    
    m.mainloop()
    
render()

# result = DownloadVideo(str(input("Enter the URL of the video you want to download: \n>> ")))
# print(result + " has been successfully downloaded.")