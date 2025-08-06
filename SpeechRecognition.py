import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Microphone is ready.")
    recognizer.adjust_for_ambient_noise(source)
    print("🔊 Listening... (say something within 5 seconds)")

    try:
        audio = recognizer.listen(source, timeout=5)
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)
        print("✅ You said:", text)

    except sr.WaitTimeoutError:
        print("⏱️ Timeout: No speech detected.")
    except sr.UnknownValueError:
        print("🤷 Could not understand speech.")
    except sr.RequestError as e:
        print(f"❌ Request error: {e}")

print("🛑 Script finished.")


