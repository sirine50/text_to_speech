import tkinter as tk
import pyttsx3

window = tk.Tk()
window.title("text to speech")
window.geometry("800x800")
window.configure(bg="#9EB1E7")  # background color

default_font = ("Arial", 12)  # consistent font

languages = {"French": 0, "English": 1}

def speak():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    selected_language = selected_option.get()
    save = save_enable.get()
    voice_volume = volume.get()
    voice_rate = rate.get()
    engine.setProperty("voice", voices[languages[selected_language]].id)
    engine.setProperty("volume", voice_volume)
    engine.setProperty("rate", voice_rate)
    user_input = entry.get()
    if save:
        file_name = entry2.get()
        engine.save_to_file(user_input, f"{file_name}.mp3")
    engine.say(user_input)
    engine.runAndWait()

def show_input_box():
    save = save_enable.get()
    if save:
        label_filename.pack(pady=(10, 0))
        entry2.pack(pady=5)
    else:
        label_filename.pack_forget()
        entry2.pack_forget()  


# Label + Input for main text
label_text = tk.Label(window, text="Enter text to speak:", font=default_font, bg="#9EB1E7")
label_text.pack(pady=(20, 5))

entry = tk.Entry(window, width=70, font=default_font)
entry.pack(pady=10)

# Language dropdown
selected_option = tk.StringVar()
selected_option.set("French")

options = ["French", "English"]
dropdown = tk.OptionMenu(window, selected_option, *options)
dropdown.config(font=default_font)
dropdown.pack()

# Save checkbox
save_enable = tk.BooleanVar()
save_enable.set(False)

cb = tk.Checkbutton(window, text="Save as file", variable=save_enable, command=show_input_box, font=default_font, bg="#9EB1E7")
cb.pack(pady=10)

# Filename input (hidden initially)
label_filename = tk.Label(window, text="Filename:", font=default_font, bg="#9EB1E7")
entry2 = tk.Entry(window, width=50, font=default_font)

# Sliders frame
slider_frame = tk.Frame(window, bg="#9EB1E7")
slider_frame.pack(pady=10)

volume = tk.DoubleVar()
volume.set(1.0)

volume_scale = tk.Scale(slider_frame, from_=0.0, to=1.0, resolution=0.1,
                        orient="horizontal", label="Volume", variable=volume,
                        length=200, font=default_font, bg="#9EB1E7")
volume_scale.pack(side="left", padx=20)

rate = tk.DoubleVar()
rate.set(200)

rate_scale = tk.Scale(slider_frame, from_=100, to=300, resolution=10,
                      orient="horizontal", label="Speed", variable=rate,
                      length=200, font=default_font, bg="#9EB1E7")
rate_scale.pack(side="left", padx=20)

# Speak button
speak_botton = tk.Button(window, text="Speak", command=speak, font=default_font,
                         bg="#ED9596", fg="white", padx=10, pady=5)
speak_botton.pack(pady=20)

window.mainloop()
