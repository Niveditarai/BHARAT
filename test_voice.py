import speech_recognition as sr


def get_voice_input():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("🎤 Speak something...")

            # noise adjust
            r.adjust_for_ambient_noise(source, duration=1)

            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said:", text)
            return text

        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return input("👉 Type your question instead: ")

        except sr.RequestError:
            print("❌ API error")
            return input("👉 Type your question instead: ")

    except Exception as e:
        print("⚠️ Mic not working, switching to typing mode...")
        return input("👉 Enter your question: ")


# test run
if __name__ == "__main__":
    result = get_voice_input()
    print("Final Output:", result)