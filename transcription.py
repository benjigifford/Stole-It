import os
from google.cloud import speech
import wave

# Print the environment variable (for debugging purposes)
print("GOOGLE_APPLICATION_CREDENTIALS:", os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

def get_sample_rate(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        sample_rate = wav_file.getframerate()
    return sample_rate

def transcribe_audio(file_path):
    client = speech.SpeechClient()
    
    with open(file_path, 'rb') as audio_file:
        audio_content = audio_file.read()
    
    sample_rate = get_sample_rate(file_path)
    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code='en-US'
    )
    
    response = client.recognize(config=config, audio=audio)
    
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    
    return response

if __name__ == "__main__":
    audio_file_path = 'conversation.wav'
    print(f"Transcribing audio file: {audio_file_path}")
    
    try:
        response = transcribe_audio(audio_file_path)
        print("Transcription completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
