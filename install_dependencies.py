from os import system

try:
    system("python -m pip install pystray wmi SpeechRecognition gTTS playsound==1.2.2 pynput Pillow "
           "keyboard AVMSpeechMath psutil")
except Exception:
    system("python3 -m pip install pystray wmi SpeechRecognition gTTS playsound==1.2.2 pynput Pillow "
           "keyboard AVMSpeechMath psutil")
finally:
    system("pip install pystray wmi SpeechRecognition gTTS playsound==1.2.2 pynput Pillow keyboard AVMSpeechMath "
           "psutil")
