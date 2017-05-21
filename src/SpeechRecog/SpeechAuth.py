import io
from google.cloud import speech


def transcribe_file(speech_file):
    """Transcribe the given audio file."""

    speech_client = speech.Client()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
        audio_sample = speech_client.sample(
            content=content,
            source_uri=None,
            encoding='LINEAR16',
            sample_rate=16000)

    alternatives = audio_sample.sync_recognize('en-US')
    for alternative in alternatives:
        print('Transcript: {}'.format(alternative.transcript))