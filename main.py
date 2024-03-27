import requests

import assemblyai as aai



aai.settings.api_key = "905cdffbffe14990b6b1259fe2d66dba"

audio_url = "output.wav"

transcriber = aai.Transcriber()

transcript = transcriber.transcribe(audio_url)

print(transcript.text)