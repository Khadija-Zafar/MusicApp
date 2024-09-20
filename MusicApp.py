import pygame
from tkinter import *
from tkinter import filedialog
import os

pygame.mixer.init()
def play_music():
    file = filedialog.askopenfilename(initialdir="/", title="Select a Music File",
                                      filetypes=(("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")))
    if file:
        song_name.set(os.path.basename(file))  # Show the file name on the player
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(loops=0)
def pause_music():
    pygame.mixer.music.pause()
def resume_music():
    pygame.mixer.music.unpause()
def stop_music():
    pygame.mixer.music.stop()
#Code for GUI
window = Tk()
window.title("Music Player")

song_name = StringVar()
song_label = Label(window, textvariable=song_name, font=("Helvetica", 16), pady=20)
song_label.pack()

play_button = Button(window, text="Play", command=play_music, font=("Helvetica", 12), width=10)
play_button.pack(pady=10)

pause_button = Button(window, text="Pause", command=pause_music, font=("Helvetica", 12), width=10)
pause_button.pack(pady=10)

resume_button = Button(window, text="Resume", command=resume_music, font=("Helvetica", 12), width=10)
resume_button.pack(pady=10)

stop_button = Button(window, text="Stop", command=stop_music, font=("Helvetica", 12), width=10)
stop_button.pack(pady=10)

window.mainloop()