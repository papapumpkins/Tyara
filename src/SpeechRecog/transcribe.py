import argparse
import io
from Speech_Interpreter import Text_Interpreter


def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    from google.cloud import speech
    speech_client = speech.Client()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
        audio_sample = speech_client.sample(
            content=content,
            source_uri=None,
            encoding=speech.Encoding.LINEAR16,
            sample_rate_hertz=16000)

    alternatives = audio_sample.recognize('en-US')
    for alternative in alternatives:
        Transc = format(alternative.transcript)
        print(Transc)
        command_Code = Interpret_Text(Transc)
        print(command_Code)


# ///////////////////////////////////////////////////////////////////////////

def Interpret_Text(command):
    code = -1
    command = command.lower()
    print(command)
    if (command.find("gmail") != -1):
        code = 1
    if (command.find("weather")):
        if ((command.find("now") != -1) | (command.find("outside")) != -1):
            code = 2
        if ((command.find("report")) != -1 | (command.find("forecast")) != -1):
            code = 3
    if (command.find("taxi") != -1) | (command.find("cab")) != -1 | (command.find("ride")) != -1:
        if (command.find("home to work")):
            code = 4
        elif (command.find("work to home") != -1):
            code = 5
        else:
            code = 0
    if (command.find("alarm") != -1):
        code = 6
    if (command.find("class") != -1 & command.find("today") != -1):
        code = 7
    if (command.find("date") != -1):
        code = 8
    if (command.find("time") != -1):
        code = 9
    if (command.find("lock") != -1 & command.find("speech") != -1):
        code = 10
    if (command.find("unlock") != -1 & command.find("speech") != -1):
        code = 11

    print(code)

    return code


# //////////////////////////////////////////////////////////////////////////

def transcribe_gcs(gcs_uri):
    """Transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    speech_client = speech.Client()

    audio_sample = speech_client.sample(
        content=None,
        source_uri=gcs_uri,
        encoding='FLAC',
        sample_rate_hertz=16000)

    alternatives = audio_sample.recognize('en-US')
    for alternative in alternatives:
        Transcript = format(alternative.transcript)
        print(Transcript)
        return Transcript
        # print('Transcript: {}'.format(alternative.transcript))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File or GCS path for audio file to be recognized')
    args = parser.parse_args()
    if args.path.startswith('gs://'):
        transcribe_gcs(args.path)
    else:
        transcribe_file(args.path)
