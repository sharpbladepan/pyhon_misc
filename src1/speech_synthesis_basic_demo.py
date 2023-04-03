# basic usage of MS azure cognitive service.
# In put some text, synthesize to speech and save to wave file
# In comments, also show how to output the speech to local speaker.
# required package: azure-cognitiveservices-speech

import os
import azure.cognitiveservices.speech as speechsdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

# audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
audio_config = speechsdk.audio.AudioOutputConfig(filename="file.wav")

# Set either the `SpeechSynthesisVoiceName` or `SpeechSynthesisLanguage`.
# speech_config.speech_synthesis_language = "en-US" 
speech_config.speech_synthesis_voice_name ="en-US-JennyNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# Construct the text we want to synthesis.

text = "This is a test text! Let me have a try!"
result = speech_synthesizer.speak_text_async(text).get()
stream = speechsdk.AudioDataStream(result)
stream.save_to_wav_file("file.wav") 

# This will output the speech directly to local speaker
# speech_synthesizer.speak_text_async(text).get()

