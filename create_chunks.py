import whisper
import json
import os
import time

print("model loading.....")
model = whisper.load_model("small")
print("model loaded......")

audios = os.listdir("audios")

for audio in audios:
    number = audio.split("_")[0]
    title = audio.split("_")[1]
    print(number, title)
    print("transcribing..... Stay connected !!")
    start = time.time()
    result = model.transcribe(audio = f"audios/4_Token Count using Lexical Analysis _ Questions on Lexical Analysis _ Imp Questions.mp4.mp3",
                            language="hi",
                            task="translate",
                            word_timestamps=False,
                            fp16= False )
    end = time.time()
    
    chunks = []
    for segment in result["segments"]:
        chunks.append({"number": number, "title": title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})

    chunks_with_metadata = {"chunks": chunks, "text": result["text"]}

    with open(f"jsons/{audio}.json", "w") as f:
        json.dump(chunks_with_metadata , f) 