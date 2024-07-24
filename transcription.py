from google.cloud import speech
import io

def transcribe_audio(file_name):
    client = speech.SpeechClient()

    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ""
    for result in response.results:
        transcript += result.alternatives[0].transcript

    return transcript

if __name__ == '__main__':
    print(transcribe_audio('conversation.wav'))
