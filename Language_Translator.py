from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import pyttsx3
import speech_recognition as sr
root=Tk()
root.geometry("500x500")
root.configure(bg="skyblue")
root.title("Language Translator")
text_to_speech=pyttsx3.init()

Title=Label(root, text="Language Translator", font=('Algerian', 22, 'italic'), bg="skyblue")
Title.place(relx=0.5, rely=0.1, anchor=CENTER)

languages=list(LANGUAGES.values())
ISO6391CODES={ 'afrikaans' :'af', 'albanian' :'sq', 'amharic' :'am', 'arabic' :'ar', 'armenian' :'hy', 'azerbaijani' :'az', 'basque' :'eu', 'belarusian' :'be', 'bengali' :'bn', 'bosnian' :'bs', 'bulgarian' :'bg', 'catalan' :'ca', 'cebuano' :'ceb', 'chichewa' :'ny', 'chinese (simplified)' :'zh-cn', 'chinese (traditional)' :'zh-tw', 'corsican' :'co', 'croatian' :'hr', 'czech' :'cs', 'danish' :'da', 'dutch' :'nl', 'english' :'en', 'esperanto' :'eo', 'estonian' :'et', 'filipino' :'tl', 'finnish' :'fi', 'french' :'fr', 'frisian' :'fy', 'galician' :'gl', 'georgian' :'ka', 'german' :'de', 'greek' :'el', 'gujarati' :'gu', 'haitian creole' :'ht', 'hausa' :'ha', 'hawaiian' :'haw', 'hebrew' :'iw', 'hebrew' :'he', 'hindi' :'hi', 'hmong' :'hmn', 'hungarian' :'hu', 'icelandic' :'is', 'igbo' :'ig', 'indonesian' :'id', 'irish' :'ga', 'italian' :'it', 'japanese' :'ja', 'javanese' :'jw', 'kannada' :'kn', 'kazakh' :'kk', 'khmer' :'km', 'korean' :'ko', 'kurdish (kurmanji)' :'ku', 'kyrgyz' :'ky', 'lao' :'lo', 'latin' :'la', 'latvian' :'lv', 'lithuanian' :'lt', 'luxembourgish' :'lb', 'macedonian' :'mk', 'malagasy' :'mg', 'malay' :'ms', 'malayalam' :'ml', 'maltese' :'mt', 'maori' :'mi', 'marathi' :'mr', 'mongolian' :'mn', 'myanmar (burmese)' :'my', 'nepali' :'ne', 'norwegian' :'no', 'odia' :'or', 'pashto' :'ps', 'persian' :'fa', 'polish' :'pl', 'portuguese' :'pt', 'punjabi' :'pa', 'romanian' :'ro', 'russian' :'ru', 'samoan' :'sm', 'scots gaelic' :'gd', 'serbian' :'sr', 'sesotho' :'st', 'shona' :'sn', 'sindhi' :'sd', 'sinhala' :'si', 'slovak' :'sk', 'slovenian' :'sl', 'somali' :'so', 'spanish' :'es', 'sundanese' :'su', 'swahili' :'sw', 'swedish' :'sv', 'tajik' :'tg', 'tamil' :'ta', 'telugu' :'te', 'thai' :'th', 'turkish' :'tr', 'ukrainian' :'uk', 'urdu' :'ur', 'uyghur' :'ug', 'uzbek' :'uz', 'vietnamese' :'vi', 'welsh' :'cy', 'xhosa' :'xh', 'yiddish' :'yi', 'yoruba' :'yo', 'zulu' :'zu'}
Label1=Label(root, text="Select the destination language", bg="skyblue")
Label1.place(relx=0.5, rely=0.2, anchor=CENTER)
Dropdown1=ttk.Combobox(root, state='readonly', values=languages)
Dropdown1.set("From : ")
Dropdown1.place(relx=0.25, rely=0.3, anchor=CENTER)
Dropdown2=ttk.Combobox(root, state='readonly', values=languages)
Dropdown2.set("To : ")
Dropdown2.place(relx=0.75, rely=0.3, anchor=CENTER)
Text_area=Text(root, width=50, height=7)
Text_area.place(relx=0.5, rely=0.45, anchor=CENTER)
output=Label(root, width=60, height=7)
output.place(relx=0.5, rely=0.75, anchor=CENTER)

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def Translate():
    translator=Translator()
    src=ISO6391CODES.get(str(Dropdown1.get()))
    dest=ISO6391CODES.get(str(Dropdown2.get()))
    translation = translator.translate(text=Text_area.get(1.0, END), src=src, dest=dest)
    output['text']=translation.text
    speak(translation.text)

btn=Button(root, text="Translate", command=Translate)
btn.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
