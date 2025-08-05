# Jarvis Voice Assistant 🤖

A Python-based voice assistant inspired by Iron Man's JARVIS that can perform various automation tasks through voice commands.

## Features ✨

- **Voice Recognition**: Listens to voice commands in English
- **Text-to-Speech**: Responds with computer-generated voice
- **WhatsApp Automation**: Send messages via voice commands
- **Google Search**: Search and get Wikipedia summaries
- **YouTube Integration**: Search and play videos on YouTube
- **How-to Queries**: Get step-by-step instructions using WikiHow

## Prerequisites 📋

Before running this program, make sure you have Python installed on your system and the following packages:

```bash
pip install pyttsx3
pip install speechrecognition
pip install pywhatkit
pip install pywikihow
pip install wikipedia
pip install pyaudio
```

## Installation 🔧

1. Clone this repository:
```bash
git clone https://github.com/Talha-Aslam/Jarvis_Program.git
cd Jarvis_Program
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main program:
```bash
python main.py
```

## Usage 🎯

Once the program is running, you can use the following voice commands:

### WhatsApp Messaging
- Say: **"send message"** or **"whatsapp message"**
- Follow the prompts to provide phone number and message

### Google Search
- Say: **"search on google [your query]"**
- For how-to queries: **"how to [your question]"**

### YouTube Features
- Search: **"search on youtube [your query]"**
- Play video: **"play video [video name]"**

## File Structure 📁

```
Jarvis_Program/
├── main.py           # Main program with voice recognition and task execution
├── Automation.py     # WhatsApp automation functionality
├── Feautures.py      # Google search and YouTube features
└── README.md         # This file
```

## How It Works 🔧

### Voice Recognition
- Uses Google's speech recognition API
- Converts speech to text with English (India) language model
- Processes commands with 2-second pause threshold

### Text-to-Speech
- Uses pyttsx3 with SAPI5 voice driver
- Customizable voice selection and speech rate
- Currently set to voice index 5 at 130 WPM

### Core Components

1. **main.py**: 
   - Initializes voice engine
   - Handles voice recognition
   - Processes and routes commands

2. **Automation.py**:
   - WhatsApp web automation using pywhatkit
   - Sends instant messages to specified numbers

3. **Feautures.py**:
   - Google search with Wikipedia integration
   - YouTube search and video playback
   - WikiHow integration for instructional content

## Supported Commands 🗣️

| Command | Function |
|---------|----------|
| "message" / "whatsapp message" | Send WhatsApp message |
| "search on google [query]" | Search Google and get summary |
| "how to [question]" | Get step-by-step instructions |
| "search on youtube [query]" | Search YouTube |
| "play video [name]" | Play specific YouTube video |

## Configuration ⚙️

### Voice Settings
You can modify voice settings in `main.py`:
- Change voice: Modify `voices[5].id` to different index
- Adjust speed: Change `rate` value (default: 130)

### WhatsApp Setup
- Ensure WhatsApp Web is accessible
- First-time users may need to scan QR code

## Troubleshooting 🔧

### Common Issues:
1. **Microphone not working**: Check system permissions
2. **Voice not recognized**: Ensure clear pronunciation and minimal background noise
3. **WhatsApp not sending**: Verify internet connection and WhatsApp Web access
4. **Import errors**: Ensure all required packages are installed

### Dependencies Issues:
If you encounter issues with pyaudio:
```bash
# On Windows
pip install pipwin
pipwin install pyaudio

# On Linux
sudo apt-get install portaudio19-dev python3-pyaudio
```

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License 📄

This project is open source and available under the MIT License.

## Future Enhancements 🚀

- [ ] Add more voice commands
- [ ] Implement weather updates
- [ ] Add calendar integration
- [ ] Support for multiple languages
- [ ] GUI interface
- [ ] Smart home device control

## Author 👨‍💻

**Talha Aslam**
- GitHub: [@Talha-Aslam](https://github.com/Talha-Aslam)

---

**Note**: This is an educational project. Ensure you have proper permissions before automating messaging services.
