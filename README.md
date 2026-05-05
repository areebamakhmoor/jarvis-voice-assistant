# 🎙️ Jarvis Voice Assistant

This is a simple Python-based voice assistant that can perform basic tasks like opening websites and playing songs using voice commands.

The project was built to understand how speech recognition and text-to-speech systems work in real applications.



## 🚀 Features

- Listens for a wake word ("Jarvis") to activate
- Converts voice input into text using speech recognition
- Opens websites like Google, YouTube, LinkedIn, etc.
- Plays specific songs through browser links
- Gives voice responses using text-to-speech



## 🛠️ Tech Used

- Python
- SpeechRecognition
- pyttsx3
- Webbrowser (built-in module)



## ⚙️ How It Works

- The program continuously listens through the microphone
- When it detects the word **"Jarvis"**, it becomes active
- It then listens for the next command
- The command is converted into text
- Based on predefined conditions, it performs actions like opening websites or playing songs
- The assistant responds back using voice output

## ▶️ How to Run

## 1. Install dependencies
```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

## 2. Run the program
```bash
python jarvis.py
```



## Example Commands

### Open Google
### Open YouTube
### Open LinkedIn
### Play perfect
### Play doraemon

## ⚠️ Limitations
Works only with predefined commands
Uses Google Speech API, so internet is required
Voice recognition may not be accurate in noisy environments

## 🔮 Future Improvements
Add support for more dynamic commands
Improve accuracy of voice recognition
Integrate APIs for real-time information (weather, news, etc.)
Add a simple user interface

Author
Areeba Makhmoor

