# Stole-It
A remake/ripoff of Strolid's Portal vCON system, that I'm designing in Python to run on my Raspberry Pi. 

Designed to capture, transcribe, store, and analyze customer conversations, this project runs on a Raspberry Pi and leverages Python, Google Cloud Speech-to-Text, and Flask for its operations.

## Project Structure

stole-it/

│

├── app.py

├── audio_capture.py

├── transcription.py

├── database.py

└── templates/

└── search_results.html


## Components

- **audio_capture.py**: Handles audio recording using a USB microphone.
- **transcription.py**: Transcribes recorded audio to text using Google Cloud Speech-to-Text.
- **database.py**: Manages the SQLite database for storing and searching transcripts.
- **templates/search_results.html**: Contains the HTML template for displaying search results.
- **app.py**: Contains the Flask web application.

## Requirements

- Python 3.x
- Raspberry Pi with Raspbian OS
- USB microphone
- Google Cloud account with Speech-to-Text enabled
- Python packages: pyaudio, google-cloud-speech, flask, sqlite3

## Setup

### 1. Set Up Google Cloud Speech-to-Text

Ensure you have set up your Google Cloud account and obtained the necessary credentials. Set the environment variable for the Google Cloud credentials:

```sh
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

### 2. Install Necessary Python Packages

```
pip install pyaudio google-cloud-speech flask
```

### 3. Running the Application

Recording audio: 
- `python audio-capture.py`
- Say something

Transcribe audio:
- `python transcription.py`

Store Transcript:
- `python database.py`

Run Flask web app:
- `python app.py`

Access Web Interface:

- Open a web browser and go to 'http://127.0.0.1:5000'

## Example Usage
- Record a conversation and save it as conversation.wav.
- Transcribe the recorded conversation using Google Cloud Speech-to-Text.
- Store the transcript in the SQLite database.
- Use the web interface to search and analyze the stored transcripts.

## Contributing
- Feel free to fork this repository and make your own modifications. Pull requests are welcome.




