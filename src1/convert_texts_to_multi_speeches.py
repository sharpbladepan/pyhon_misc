import docx
import os
import azure.cognitiveservices.speech as speechsdk


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



# create a new document object from the docx file
doc = docx.Document('sample.docx')

ssml_before = """<speak xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xmlns:emo="http://www.w3.org/2009/10/emotionml" version="1.0" xml:lang="en-US">
                 <voice name="en-US-ChristopherNeural">
                 <prosody rate="1.0">"""
ssml_after = """</prosody>
                </voice>
                </speak>"""
                
# get all the text from the document
paras = doc.paragraphs
text = ""
for i in range(len(paras)):
    if (paras[i].text == ""):        
        continue
    if ( paras[i].text[0]== 'P' and paras[i].text[1:].isnumeric()):
        # convert to speeach for this section
        if ( text != "" ):
            print(text)
            ssml = ssml_before + text + ssml_after
            Speech_Synthesis_to_Wave(file_name, ssml)
            text = ""            
        if ( paras[i+1].text[0]== 'P' and paras[i+1].text[1:].isnumeric() ):            
            continue        
        # a new wav file
        file_name = paras[i].text + ".wav"        
        print(">>>" + file_name)
        continue        
    # add text to current section    
    text += paras[i].text
    
#convert last section
print(text)
ssml = ssml_before + text + ssml_after
Speech_Synthesis_to_Wave(file_name, ssml)
    
        
        


# print(page_delimiter_lines)



    
    
        