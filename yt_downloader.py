from pytube import YouTube
import PySimpleGUI as gui 

def download(url, type):
    yt = YouTube(url)
    yt.streams.get_by_itag(type).download()
if __name__ == "__main__":
    gui.theme('DarkAmber')
    link = gui.InputText(key= "_URL_", size=(70, 50))
    choices = ['video', 'audio']
    layout = [
        [gui.Text("Welcome, type in the link for the YouTube video, then click download", font = 'Courier 11')],
        [link, gui.DropDown(choices, default_value='Video/Audio', size=(12, 50), key="_TYPE_")],
        [gui.Button("Download")]
        ]
    win = gui.Window("YT Downloader", layout, (75, 50), element_justification='c')
    while True:
        event, values = win.read()
        if event == gui.WIN_CLOSED:
            break
        if event == "Download":
            if values["_TYPE_"] == 'video':
                download(values["_URL_"], 18)
            elif values["_TYPE_"] == 'audio':
                download(values["_URL_"], 140)
    win.close()

