import pyttsx3

engine = pyttsx3.init()
want_to_exit = False


voices = engine.getProperty("voices")
for i, voice in enumerate(voices):
    print(f"voices[{i}]:")
    print(f"ID: {voice.id}")
    print(f"Name: {voice.name}")
    print(f"language: {voice.languages}")
    print(f"Gender: {voice.gender}")
    print()

while not want_to_exit: 
    while True:
        print("Enter 0 for French")
        print("Enter 1 for English")
        try:
            wanted_voice = int(input("Enter your choice: "))
        except ValueError:
            print("It needs to be either 0 or 1!!!!!!")
            continue    

        if wanted_voice in [0, 1]:
            break

    engine.setProperty("volume", 1)
    engine.setProperty("voice", voices[wanted_voice].id)

    text = input("Type what you want ot be said: ")

    engine.say(text)

    save_as_file = input("Do you want to save it as a file? [yes, no]: ").lower()
    if save_as_file == "yes":
        name = input("What's the name of the file: ")
        engine.save_to_file(text, f"{name}.mp3")
    
    engine.runAndWait()

    answer_to_exiting = input("Do you want to exit? [yes, no]: ").lower()
    if answer_to_exiting == "yes":
        want_to_exit = True
