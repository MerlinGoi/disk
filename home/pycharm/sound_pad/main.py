import sys
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import ast
import os
import subprocess
from mutagen import File as AudioFile  # pip install mutagen
from pydub import AudioSegment      # pip install pydub
import sounddevice as sd
import numpy as np


root = tk.Tk()
root.title("Audio List Manager")
root.geometry("900x500")

# ------------------------ Setup ----------------------
frame1 = tk.Frame(root, bg="lightblue", bd=2, relief="solid")
frame2 = tk.Frame(root, bg="lightgreen", bd=2, relief="solid")

frame1.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))
frame2.pack(fill=tk.X, padx=10, pady=(5, 10))

listbox = tk.Listbox(frame1, height=15, width=70, font=("Consolas", 11))
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(5, 0), pady=5)

scrollbar = tk.Scrollbar(frame1, orient="vertical", command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 5), pady=5)

listbox.config(yscrollcommand=scrollbar.set)

# ------------------------ Load Data -------------------------
data = []
if os.path.exists("ur_song_here.txt"):
    with open("ur_song_here.txt", "r", encoding="utf-8") as file:
        content = file.read().strip()
        if content:
            data = ast.literal_eval(content)

# Selected microphone device index
selected_mic_index = None

# ------------------------ Populate Listbox -------------------------
def refresh_listbox():
    listbox.delete(0, tk.END)
    for i, entry in enumerate(data, start=1):
        name = entry[0][0]
        duration = entry[1][0]
        listbox.insert(tk.END, f"{i}. {name} — {duration}")

refresh_listbox()

# ------------------------ Helper: Get Duration -------------------------
def get_audio_length(filepath):
    try:
        audio = AudioFile(filepath)
        if not audio or not audio.info:
            return "0:00"
        total_seconds = int(audio.info.length)
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes}:{seconds:02d}"
    except Exception:
        return "0:00"

# ------------------------ Add Function -------------------------
def add_fun():
    filepath = filedialog.askopenfilename(
        title="Select an audio file",
        filetypes=[
            ("Audio Files", "*.mp3 *.wav *.flac *.ogg *.m4a"),
            ("All Files", "*.*")
        ]
    )
    if not filepath:
        return

    name = os.path.splitext(os.path.basename(filepath))[0]
    duration = get_audio_length(filepath)
    entry = [[name], [duration], [filepath]]
    data.append(entry)
    refresh_listbox()

    with open("ur_song_here.txt", "w", encoding="utf-8") as f:
        f.write(str(data))

# ------------------------ Open Function -------------------------
def open_selected_file(event=None):
    selection = listbox.curselection()
    if not selection:
        print("No item selected.")
        return

    index = selection[0]
    path = data[index][2][0]

    if os.path.exists(path):
        if os.name == "nt":
            os.startfile(path)
        elif os.name == "posix":
            subprocess.call(("open" if sys.platform == "darwin" else "xdg-open", path))
        print(f"Opened: {path}")
    else:
        print(f"File not found: {path}")

# ------------------------ Remove Function -------------------------
def remove_selected_file():
    selection = listbox.curselection()
    if not selection:
        print("No item selected to remove.")
        return

    index = selection[0]
    removed = data.pop(index)
    refresh_listbox()

    with open("ur_song_here.txt", "w", encoding="utf-8") as f:
        f.write(str(data))

    print(f"Removed: {removed[0][0]}")

# ------------------------ Configure Microphone -------------------------
def configure_mic():
    global selected_mic_index
    devices = sd.query_devices()
    input_devices = [(i, d['name']) for i, d in enumerate(devices) if d['max_input_channels'] > 0]
    if not input_devices:
        messagebox.showerror("Error", "No input devices found")
        return

    device_strs = [f"{i}: {name}" for i, name in input_devices]
    selection = simpledialog.askstring("Select Microphone",
                                       "Available input devices:\n" + "\n".join(device_strs) +
                                       "\n\nEnter device index:")
    if selection is None:
        return
    try:
        selection_index = int(selection)
        if selection_index in [i for i, _ in input_devices]:
            selected_mic_index = selection_index
            messagebox.showinfo("Microphone Selected", f"Selected mic: {devices[selected_mic_index]['name']}")
        else:
            messagebox.showerror("Error", "Invalid index")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# ------------------------ Play Selected Audio to Mic -------------------------
def play_selected_to_mic():
    if selected_mic_index is None:
        messagebox.showwarning("Warning", "Please configure a microphone first")
        return

    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Warning", "No audio selected")
        return

    index = selection[0]
    path = data[index][2][0]

    try:
        # Use pydub for all formats
        audio = AudioSegment.from_file(path)
        audio = audio.set_channels(1).set_frame_rate(44100)
        samples = np.array(audio.get_array_of_samples()).astype(np.float32) / (2**15)
        sd.play(samples, samplerate=44100, device=selected_mic_index)
        sd.wait()
        messagebox.showinfo("Done", f"Played {data[index][0][0]} to selected mic")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ------------------------ Frame 2 (Buttons) -------------------------
btn_add = tk.Button(frame2, text='Add Audio', font=('Arial', 16), bg="lightgrey", command=add_fun)
btn_add.pack(side=tk.RIGHT, padx=20, pady=10)

btn_remove = tk.Button(frame2, text='Remove', font=('Arial', 16), bg="lightgrey", command=remove_selected_file)
btn_remove.pack(side=tk.RIGHT, padx=20, pady=10)

btn_open = tk.Button(frame2, text='Open File', font=('Arial', 16), bg="lightgrey", command=open_selected_file)
btn_open.pack(side=tk.RIGHT, padx=20, pady=10)

btn_mic = tk.Button(frame2, text='Configure Mic', font=('Arial', 16), bg="lightgrey", command=configure_mic)
btn_mic.pack(side=tk.LEFT, padx=20, pady=10)

btn_play_mic = tk.Button(frame2, text='Play to Mic', font=('Arial', 16), bg="lightgrey", command=play_selected_to_mic)
btn_play_mic.pack(side=tk.LEFT, padx=20, pady=10)

ver_label = tk.Label(frame2, text="v0.0.4", font=("Arial", 8), bg="lightgreen")
ver_label.pack(side=tk.LEFT, padx=10, pady=10)

listbox.bind("<Double-Button-1>", open_selected_file)

root.mainloop()
