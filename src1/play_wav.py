import wave
import pyaudio
# required package: pyaudio


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