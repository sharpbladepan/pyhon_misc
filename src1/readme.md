### speech_synthesis_basic_demo.py
使用MS Azure提供的语音识别服务，将一段文本转换成语音并保存wav格式的本地文件。

### speech_synthesis_ssml_demo.py
使用ssml格式定义的文本，ssml可以指定语速，语调，风格等，能够提供更多的控制。
同样转化为本地wav文件，并且播放出来。

### convert_texts_to_multi_speeches.py
读取word文档（格式样例如sample.docx，段落分割固定为Pxx），将其中的每一段文本都转成语音，并保存为一个独立的wav文件，
