import whisper

model = whisper.load_model("tiny.en")
result = model.transcribe(r"C:\Users\lucyc\Desktop\aaa.wav")
print(result)
input()

