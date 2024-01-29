import tkinter as tk
import pygame

app = tk.Tk()
app.geometry("350x250")
app.title("Dev Duniya Music Player")


def play_music():
    pygame.mixer.music.load("Crock Pot - Diamond Ortiz.mp3")
    pygame.mixer.music.play()
def pause_music():
    pygame.mixer.music.pause()
def stop_music():
    pygame.mixer.music.stop()
def resume_music():
    pygame.mixer.music.unpause()
def exit_program():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    app.destroy()

def set_volume(val):
    volume = float(val)
    pygame.mixer.music.set_volume(volume)




volume_scale = tk.Scale(app, from_=0, to=1, resolution=0.1, orient="horizontal", label="Volume Control")
volume_scale.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
volume_scale.config(command=set_volume)



play_button = tk.Button(app, text="Play", command=play_music)
pause_button = tk.Button(app, text="Pause", command=pause_music)
stop_button = tk.Button(app, text="Stop", command=stop_music)
resume_button = tk.Button(app, text="Resume", command=resume_music)
exit_button = tk.Button(app, text="Exit", command=exit_program)

play_button.grid(row=0, column=0, padx=10, pady=10)
pause_button.grid(row=0, column=1, padx=10, pady=10)
stop_button.grid(row=0, column=2, padx=10, pady=10)
resume_button.grid(row=0, column=4, padx=10, pady=10)
exit_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

pygame.mixer.init()
app.mainloop()