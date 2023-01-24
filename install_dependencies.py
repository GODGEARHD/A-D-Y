from os import system

try:
    system("python -m pip install pystray PyAudio pygame wmi SpeechRecognition gTTS playsound==1.2.2 pynput "
           "Pillow keyboard psutil")
except Exception:
    system("python3 -m pip install pystray PyAudio pygame wmi SpeechRecognition gTTS playsound==1.2.2 pynput "
           "Pillow keyboard psutil")
finally:
    system("pip install pystray PyAudio pygame wmi SpeechRecognition gTTS playsound==1.2.2 pynput Pillow "
           "keyboard psutil")
