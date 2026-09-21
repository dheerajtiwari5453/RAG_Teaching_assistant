import whisper
import time

print("Loading model...")
model = whisper.load_model("small")
print("Model loaded.")
print("Starting transcription...")
start = time.time()

result = model.transcribe(audio = "audio/9_How to Check a Grammar is LL(1) or Not _ Short Trick.mp4.mp3",
                          fp16=False,
                          language="hi",
                          task="translate")

end = time.time()
print(f"Transcription finished in {end - start:.2f} seconds")
print("Writing output to file...")
print(result["text"])

text = result["text"].replace(". ", ".\n")
with open("lecture_12.txt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        f.write(segment["text"].strip() + "\n")

print("Done.")