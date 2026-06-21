import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import os
import pyttsx3

def speak(text):
    print(f"Jarvis: {text}")

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    engine.say(text)
    engine.runAndWait()

    engine.stop()


def record_audio(duration=3, fs=44100):

    print("Listening...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    write(temp_file.name, fs, recording)

    return temp_file.name


def take_command():

    recognizer = sr.Recognizer()

    try:

        audio_file = record_audio()

        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

        os.remove(audio_file)

        print("Recognizing...")

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print("You said:", command)

        return command.lower()

    except Exception as e:
        print("Error:", e)
        return ""


def process_command(command):

    if "hello" in command or "hi" in command:
        speak("Hello sir! How are you?")

    elif "what is your name" in command:
        speak("My name is Jarvis.")

    elif "how are you" in command:
        speak("I am doing well sir. Thank you for asking.")

    elif "what time is it" in command:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif "what is the date" in command:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")

    elif "what day is it" in command:
        from datetime import datetime
        current_day = datetime.now().strftime("%A")
        speak(f"Today is {current_day}")

    elif "open notepad" in command:
        import subprocess
        subprocess.Popen("notepad.exe")
        speak("Notepad opened.")

    elif "show battery status" in command:
        import psutil
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent

        if battery.power_plugged:
            speak(f"Battery is at {percent} percent and charging.")
        else:
            speak(f"Battery is at {percent} percent.")

    elif "open command prompt" in command:
        import subprocess
        subprocess.Popen("cmd.exe")
        speak("Command Prompt opened.")

    elif "open powershell" in command:
        import subprocess
        subprocess.Popen("powershell.exe")
        speak("PowerShell opened.")

    elif "control brightness" in command:
        try:
            import screen_brightness_control as sbc
        except ImportError:
            speak("Screen brightness control library is not installed.")
            return

        brightness_level = command.replace("control brightness", "").strip()

        if "increase" in brightness_level:
            current_brightness = sbc.get_brightness()
            new_brightness = min(current_brightness[0] + 10, 100)
            sbc.set_brightness(new_brightness)
            speak(f"Brightness increased to {new_brightness} percent.")
        elif "decrease" in brightness_level:
            current_brightness = sbc.get_brightness()
            new_brightness = max(current_brightness[0] - 10, 0)
            sbc.set_brightness(new_brightness)
            speak(f"Brightness decreased to {new_brightness} percent.")
        else:
            speak("Please specify whether to increase or decrease the brightness.")

    elif "cpu usage" in command:
        import psutil
        cpu_percent = psutil.cpu_percent(interval=1)
        speak(f"Current CPU usage is {cpu_percent} percent.")

    elif "system information" in command:
        import platform
        system_info = platform.uname()
        speak(f"System: {system_info.system}, Node Name: {system_info.node}, Release: {system_info.release}, Version: {system_info.version}, Machine: {system_info.machine}, Processor: {system_info.processor}")

    elif "ram usage" in command:
        import psutil
        ram = psutil.virtual_memory()
        speak(f"Total RAM: {ram.total / (1024 ** 3):.2f} GB, Used RAM: {ram.used / (1024 ** 3):.2f} GB, Available RAM: {ram.available / (1024 ** 3):.2f} GB, RAM Usage: {ram.percent}%")

    elif "disk usage" in command:
        import psutil
        disk = psutil.disk_usage('/')
        speak(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB, Used Disk Space: {disk.used / (1024 ** 3):.2f} GB, Free Disk Space: {disk.free / (1024 ** 3):.2f} GB, Disk Usage: {disk.percent}%")

    elif "memory usage" in command:
        import psutil
        memory = psutil.virtual_memory()
        speak(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB, Used Memory: {memory.used / (1024 ** 3):.2f} GB, Available Memory: {memory.available / (1024 ** 3):.2f} GB, Memory Usage: {memory.percent}%")

    elif "open google" in command:
        import webbrowser
        webbrowser.open("https://www.google.com")

    elif "search google for" in command:
        import webbrowser
        search_query = command.replace("search google for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif "open youtube" in command:
        import webbrowser
        webbrowser.open("https://www.youtube.com")

    elif "search youtube for" in command:
        import webbrowser
        search_query = command.replace("search youtube for", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

    elif "open downloads folder" in command:
       
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(downloads_path)
        speak("Downloads folder opened.")

    elif "open github" in command:
        import webbrowser
        webbrowser.open("https://www.github.com")

    elif "open stack overflow" in command:
        import webbrowser
        webbrowser.open("https://stackoverflow.com")

    elif "open gmail" in command:
        import webbrowser
        webbrowser.open("https://mail.google.com")

    elif "open yahoo mail" in command:
        import webbrowser
        webbrowser.open("https://mail.yahoo.com")

    elif "open chrome" in command:
        
        os.system("start chrome")
        speak("Google Chrome opened.")

    elif "open brave" in command:
        import subprocess
        subprocess.Popen("brave.exe")
        speak("Brave browser opened.")

    elif "open firefox" in command:
        
        os.system("start firefox")
        speak("Mozilla Firefox opened.")

    elif "open facebook" in command:
        import webbrowser
        webbrowser.open("https://www.facebook.com")

    elif "open twitter" in command:
        import webbrowser
        webbrowser.open("https://www.twitter.com")

    elif "open linkedin" in command:
        import webbrowser
        webbrowser.open("https://www.linkedin.com")

    elif "open instagram" in command:
        import webbrowser
        webbrowser.open("https://www.instagram.com")

    elif "open reddit" in command:
        import webbrowser
        webbrowser.open("https://www.reddit.com")

    elif "open whatsapp" in command:
        import webbrowser
        webbrowser.open("https://web.whatsapp.com")

    elif "open telegram" in command:
        import webbrowser
        webbrowser.open("https://web.telegram.org")

    elif "open discord" in command:
        import webbrowser
        webbrowser.open("https://discord.com")

    elif "open coursera" in command:
        import webbrowser
        webbrowser.open("https://www.coursera.org")

    elif "open calculator" in command:
        import subprocess
        subprocess.Popen("calc.exe")
        speak("Calculator opened.")

    elif "open chat gpt" in command:
        import webbrowser
        webbrowser.open("https://chat.openai.com")
        speak("ChatGPT opened.")

    elif "open spotify" in command:
        import webbrowser
        
        webbrowser.open("https://open.spotify.com")
        speak("Spotify opened.")

    elif "open netflix" in command:
        import webbrowser
        webbrowser.open("https://www.netflix.com")
        speak("Netflix opened.")

    elif "open calendar" in command:
         import pyautogui

         pyautogui.click(x=1800, y=1050)  # bottom-right clock area

         speak("Opening calendar.")

    elif "open vs code" in command:
        import subprocess
        subprocess.Popen( r"C:\Users\SWASTIK\AppData\Local\Programs\Microsoft VS Code\Code.exe")
        speak("Visual Studio Code opened.")

    elif "open file explorer" in command:
        import subprocess
        subprocess.Popen("explorer.exe")
        speak("File Explorer opened.")

    elif "open control panel" in command:
        import subprocess
        subprocess.Popen("control.exe")
        speak("Control Panel opened.")

    elif "open task manager" in command:
        import subprocess
        subprocess.Popen("taskmgr.exe")
        speak("Task Manager opened.")

    elif "open device manager" in command:
        os.system("start devmgmt.msc")
        speak("Opening Device Manager.")


    elif "open recycle bin" in command:
        import subprocess
        subprocess.Popen("explorer.exe shell:RecycleBinFolder")
        speak("Recycle Bin opened.")

    elif "empty recycle bin" in command:
        import winshell
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Recycle Bin emptied.")

    elif "open settings" in command:
        
        os.system("start ms-settings:")
        speak("Settings opened.")

    elif "open camera" in command:
        
        os.system("start microsoft.windows.camera:")
        speak("Camera opened.")

    elif "open paint" in command:
        import subprocess
        subprocess.Popen("mspaint.exe")
        speak("Paint opened.")

    elif "open snipping tool" in command:
        import subprocess
        subprocess.Popen("snippingtool.exe")
        speak("Snipping Tool opened.")

    elif "open magnifier" in command:
        
        os.system("start magnify:")

        speak("Magnifier opened.")

    elif "open voice recorder" in command:
        import subprocess
        subprocess.Popen("soundrecorder.exe")
        speak("Voice Recorder opened.")

    elif "create note" in command:
        speak("What should I write in the note?")

        note_content = take_command()

        with open("note.txt", "w") as file:
         file.write(note_content)

        os.startfile("note.txt")
        speak("Note created successfully.")

    elif "read note" in command:
        
        note_file = "note.txt"
        if os.path.exists(note_file):
            with open(note_file, "r") as f:
                note_content = f.read()
            speak(f"The content of the note is: {note_content}")
        else:
            speak("No note found. Please create a note first.")

    elif "take screenshot" in command:
        import pyautogui
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot taken and saved as screenshot.png")

    elif "show screenshot" in command:
        
        if os.path.exists("screenshot.png"):
            os.startfile("screenshot.png")
            speak("Displaying the screenshot.")
        else:
            speak("No screenshot found. Please take a screenshot first.")

    elif "control volume" in command:
        import pyautogui
        volume_level = command.replace("control volume", "").strip()

        if "up" in volume_level:
            pyautogui.press("volumeup")
            speak("Volume increased.")
        elif "down" in volume_level:
            pyautogui.press("volumedown")
            speak("Volume decreased.")
        elif "mute" in volume_level:
            pyautogui.press("volumemute")
            speak("Volume muted.")
        else:
            speak("Please specify whether to increase, decrease, or mute the volume.")

    elif "what is the weather" in command:
        import requests

        api_key = "a72ea72d5d53afe0791ce80bed10b869"
        city = "Bhubaneswar"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data["cod"] == 200:
                weather_desc = data["weather"][0]["description"]
                temp = data["main"]["temp"]
                speak(f"The weather in {city} is currently {weather_desc} with a temperature of {temp} degrees Celsius.")
            else:
                speak("Sorry, I couldn't retrieve the weather information.")

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I couldn't retrieve the weather information.")


    elif "what is the news" in command:
        import requests

        api_key = " xx"
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            if data["status"] == "ok":
                articles = data["articles"][:5]
                speak("Here are the top news headlines:")
                for i, article in enumerate(articles, 1):
                    speak(f"{i}. {article['title']}")
            else:
                speak("Sorry, I couldn't retrieve the news information.")

        except Exception as e:
            print("Error:", e)
            speak("Sorry, I couldn't retrieve the news information.")

    elif "internet speed" in command:
        import speedtest

        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download() / (1024 * 1024)
            upload_speed = st.upload() / (1024 * 1024)
            speak(f"Your internet speed is {download_speed:.2f} Mbps for download and {upload_speed:.2f} Mbps for upload.")
        except Exception as e:
            print("Error:", e)
            speak("Sorry, I couldn't retrieve the internet speed information.")


    elif "good evening" in command:
            speak("Good evening sir! How was your day?")


    elif "good afternoon" in command:
            speak("Good afternoon sir! How is your day going?")

    elif "good morning" in command:
            speak("Good morning sir! How are you today?")
        
    elif "good night" in command:
            speak("Good night sir! Sleep well.")
        
    elif "thank you" in command:
            speak("You're welcome sir!")

    elif "lock my pc" in command:
        import ctypes
        ctypes.windll.user32.LockWorkStation()
        speak("Your PC has been locked.")

    elif "restart my pc" in command:
        
        os.system("shutdown /r /t 0")
        speak("Your PC is restarting.")

    elif "shut down my pc" in command:
        
        os.system("shutdown /s /t 0")
        speak("Your PC is shutting down.")

    elif "bye" in command or "exit" in command:
        speak("Goodbye!")
        return False

    else:
        speak("Sorry, I don't understand that command.")

    return True


speak("Initiating all protocols. All systems online. Hello sir, I am Jarvis, your virtual assistant.")

while True:

    command = take_command()

    if not command:
        continue

    if not process_command(command):
        break