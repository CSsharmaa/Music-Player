from tkinter import *
from tkinter import filedialog
import pygame

window = Tk()

window.title("MP3 PLAYER")
window.geometry("500x500")

# initialize pygame
pygame.mixer.init()


def add_song():
    song = filedialog.askopenfilename(initialdir='Music/', title="choose a song", filetypes=(("mp3 Files", "*.mp3"),))
    # remove directory address
    song = song.replace("C:/Users/CSsharma/Documents/Ind Python/works/Music/", " ")
    song = song.replace(".mp3", " ")
    playlist_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='Music/', title="choose a song", filetypes=(("mp3 Files", "*.mp3"),))

    # loop through songs
    for song in songs:
        # remove directory address


        # add to playlist
        playlist_box.insert(END, song)


def delete_song():
    playlist_box.delete(ANCHOR)


def delete_all_songs():
    playlist_box.delete(0, END)


def play():
    song = playlist_box.get(ACTIVE)

    my_label.config(text=song)
    # load song with pygame mixer
    pygame.mixer.music.load(song)
    # play song with pygame mixer
    pygame.mixer.music.play(loops=0)


# create playlist box
playlist_box = Listbox(window, bg="black", fg="green", width=60, selectbackground="green", selectforeground="red")
playlist_box.pack(pady=20)

# Control Button images
back_btn_img = PhotoImage(file='Music Player Images/back.png')
fwd_btn_img = PhotoImage(file='Music Player Images/forward.png')
play_btn_img = PhotoImage(file='Music Player Images/play.png')
pause_btn_img = PhotoImage(file='Music Player Images/pause.png')
stop_btn_img = PhotoImage(file='Music Player Images/stop.png')

# create button frames
control_frame = Frame(window)
control_frame.pack(pady=20)

# create play/pause/stop/etc. buttons
back_btn = Button(control_frame, image=back_btn_img, borderwidth=0)
fwd_btn = Button(control_frame, image=fwd_btn_img, borderwidth=0)
play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0)
stop_btn = Button(control_frame, image=stop_btn_img, borderwidth=0)

back_btn.grid(row=0, column=0, padx=10)
fwd_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

# Creating main Menu
my_menu = Menu(window)
window.config(menu=my_menu)

# Create add song menu dropdowm
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Songs", menu=add_song_menu)
# add one song
add_song_menu.add_command(label="Add one song to playlist", command=add_song)
# add many songs
add_song_menu.add_command(label="Add many songs to playlist", command=add_many_songs)

# delete song
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Remove songs", menu=remove_song_menu)

remove_song_menu.add_command(label="delete song from playlist", command=delete_song)
remove_song_menu.add_command(label="delete all songs from playlist", command=delete_all_songs)

# Temporary label
my_label = Label(window, text="")
my_label.pack(pady=20)

window.mainloop()
