import speech_recognition as sr

r = sr.Recognizer()


def the_func() :
    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
        print ('Done!')
        the_func()
        return

audio = r.listen(source)
text = r.recognize_google(audio)
print(text)

the_func()
