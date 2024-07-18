from tkinter import *
import tkinter as ttk
import openai
import random
from gtts import gTTS
import os
import playsound

# Initialize the OpenAI API client
openai.api_key = 'sk-proj-dWQmYfr3ah11H8Gn9PH8T3BlbkFJPT1xJdnPb2pxqUYvLFrI'

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x600+250+30')
        self.root.title('Welcome to Sindh Museum Hyderabad')
        self.root.bind('<Return>', self.ent_func)
        
        #===========title================
        lbl_title = Label(self.root, bg='White', text='Welcome to Sindh Museum Hyderabad', font=('Calibri', 25, 'bold'))
        lbl_title.place(x=50, y=20)

        #========Main Frame with Text=========
        main_frame = Frame(self.root, relief=RAISED, bg='white')
        main_frame.place(x=0, y=60, width=700, height=400)

        # ===========Text area with scrollbar===
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, font=('Calibiri', 14), relief=RAISED, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        #====Search label
        lbl_search = Label(self.root, text='هتي ڳولا ڪريو', font=('Calibri', 18, 'bold'))
        lbl_search.place(x=20, y=480)

        #=====entry
        self.ent = StringVar()
        self.entry = ttk.Entry(self.root, textvariable=self.ent, bd=2, font=('Calibri', 16, 'bold'))
        self.entry.place(x=200, y=480, width=400, height=30)

        # =====btn send
        self.btn_send = ttk.Button(self.root, command=self.send, width=20, text='جمع ڪريو', font=('Calibiri', 14,), bg='gray', fg='Black')
        self.btn_send.place(x=200, y=520, width=200, height=30)
        
        # =====btn clear
        self.btn_clr = ttk.Button(self.root, command=self.clear, width=20, text='صاف ڪريو', font=('Calibiri', 14,), bg='gray', fg='Black')
        self.btn_clr.place(x=410, y=520, width=200, height=30)

        # ====label message
        self.msg = StringVar()
        self.lbl_msg = Label(self.root, textvariable=self.msg)
        self.lbl_msg.place(x=100, y=580)

    # ======================================functions=============

    def ent_func(self, event):
        self.btn_send.invoke()
        self.ent.set("")

    def clear(self):
        self.text.delete('1.0', END)
        self.ent.set("")

    def speak(self, text, lang='sd'):
        tts = gTTS(text=text, lang=lang)
        tts.save("response.mp3")
        playsound.playsound("response.mp3")
        os.remove("response.mp3")
    
    def get_gpt3_response(self, prompt, model="gpt-3.5-turbo"):
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()

    def send(self):
        user_input = "\t\t\t" + "توهان: " + self.entry.get()
        self.text.insert(END, "\n" + user_input)

        if self.entry.get() == "About area":
            self.msg.set("مهرباني ڪري ڪجھ ٽائيپ ڪريو")
            self.lbl_msg.config(text=self.msg.get(), fg='black')
        else:
            self.msg.set("")
            self.lbl_msg.config(text=self.msg.get(), fg='black')

    input_list = ['hello']
    output_list = ['ہیلو اور ہنٹریئن میوزیم میں خوش آمدید۔ میں ایک AI لینگویج ماڈل ہوں اور آج آپ کا ورچوئل کیوریٹر ہوں گا۔ میرا نام اوپن AI ہے۔ میں آج آپ کی کیسے مدد کرسکتا ہوں؟']
    for mess in input_list:
            if self.entry.get().lower() == mess:
                put_into_text = random.choice(output_list)
                self.text.insert(END, '\n\n' + "Bot :" + put_into_text)
                self.speak(put_into_text)

    Area_museum = "سنڌ ميوزيم سنڌ جي تاريخ ۽ ثقافت جي نمائش لاءِ آهي، جتي مختلف وقتن جي قديم نوادرات، هٿرادو شيون ۽ ثقافتي شين جي نمائش ڪئي ويندي آهي"
    if self.entry.get().lower() in ["i would like to learn about the wars in the area", "about area"]:
           self.text.insert(END, '\n\n' + "Bot :" + Area_museum)
           self.speak(Area_museum)
           questions_answers = {
            "سنڌ ميوزيم بابت ٻڌايو": "سنڌ ميوزيم سنڌ جي تاريخ ۽ ثقافت جي نمائش لاءِ آهي، جتي مختلف وقتن جي قديم نوادرات، هٿرادو شيون ۽ ثقافتي شين جي نمائش ڪئي ويندي آهي.",
            "سنڌ ميوزيم ڪٿي واقع آهي؟": "سنڌ ميوزيم پاڪستان جي صوبي سنڌ جي شهر حيدرآباد ۾ واقع آهي.",
            "سنڌ ميوزيم جي داخلا فيس ڇا آهي؟": "سنڌ ميوزيم جي داخلا فيس بالغن لاءِ 50 روپيا ۽ ٻارن لاءِ 20 روپيا آهي."
        }

user_query = self.entry.get().strip()
response = questions_answers.get(user_query, self.get_gpt3_response(user_query))
self.text.insert(END, '\n\n' + "بوٽ: " + response)

if __name__ == "__main__":
    root = Tk()
    chatbot = Chatbot(root)
    root.mainloop()