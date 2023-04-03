import os
import azure.cognitiveservices.speech as speechsdk
# For play the generated .wav file
import wave
import pyaudio

def Play_Wav(file_name):
    # Open the WAV file
    wav_file = wave.open(file_name, "rb")

    # Get the sample rate and channels
    sample_rate = wav_file.getframerate()
    channels = wav_file.getnchannels()

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open a stream and play the audio
    stream = audio.open(format=audio.get_format_from_width(wav_file.getsampwidth()),
                    channels=channels,
                    rate=sample_rate,
                    output=True)
    data = wav_file.readframes(1024)
    while data:
        stream.write(data)
        data = wav_file.readframes(1024)

    # Cleanup
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wav_file.close()

def Speech_Synthesis_to_Wave(file_name, ssml_str):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

    audio_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
    speech_config.speech_synthesis_voice_name ="en-US-JennyNeural"

    # Create a TTS synthesizer and synthesize the speech
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_synthesizer.speak_ssml_async(ssml_str).get()
    
    # Write the synthesized speech to an output file
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file(file_name) 


# Set the SSML to be converted to speech
text = "This is a test text! Let me have a try!"
ssml_before = """<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
 				 <voice name="en-US-JennyNeural">
                 <mstts:express-as style="cheerful" styledegree="2">
				 <prosody rate="1.0">"""
ssml_after = """</prosody>
                </mstts:express-as>
				</voice>
				</speak>"""

ssml = ssml_before + text + ssml_after

file_name_tmp = "test01.wav"

Speech_Synthesis_to_Wave(file_name_tmp, ssml)
Play_Wav(file_name_tmp)




