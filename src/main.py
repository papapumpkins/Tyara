from SpeechRecog import SpeechAuth

SP = SpeechAuth

audio_file="report.mp3"

SP.transcribe_file(audio_file)

