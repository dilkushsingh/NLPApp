from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API
class NLPApp:
    def __init__(self):

        self.dbo = Database()
        self.apio = API()
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('400x500')
        self.root.configure(bg='#695aa6')

        self.login_gui()

        self.root.mainloop()
    def login_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#695aa6', fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email', bg='#695aa6', fg='white')
        label1.pack(pady=(10,5))
        label1.configure(font=('verdana', 13))
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5,10))

        label2 = Label(self.root, text='Enter Password', bg='#695aa6', fg='white')
        label2.pack(pady=(10,5))
        label2.configure(font=('verdana', 13))
        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5,10))

        login_btn = Button(self.root, text='Login', width=20, height=1, command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a Member?', bg='#695aa6', fg='white')
        label3.pack(pady=(10,5))

        redirect_btn = Button(self.root, text='Register Now', command=self.register_gui)
        redirect_btn.pack()

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPApp', bg='#695aa6', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name', bg='#695aa6', fg='white')
        label0.pack(pady=(10, 5))
        label0.configure(font=('verdana', 13))
        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10))

        label1 = Label(self.root, text='Enter Email', bg='#695aa6', fg='white')
        label1.pack(pady=(10, 5))
        label1.configure(font=('verdana', 13))
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10))

        label2 = Label(self.root, text='Enter Password', bg='#695aa6', fg='white')
        label2.pack(pady=(10, 5))
        label2.configure(font=('verdana', 13))
        self.password_input = Entry(self.root, width=30, show='*')
        self.password_input.pack(pady=(5, 10))

        register_btn = Button(self.root, text='Register', width=15, height=1, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a Member?', bg='#695aa6', fg='white')
        label3.pack(pady=(10, 5))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_user(name, email, password)
        if response:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
            self.login_gui()
        else:
            messagebox.showinfo('Error', 'Email Already exist. Login now')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search_user(email, password)
        if response:
            messagebox.showinfo('Success', 'Login successfull')
            self.home_gui()
        else:
            messagebox.showinfo('Error', 'Incorrect Email/Password')
    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#695aa6', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=25, height=3, command=self.perform_ner)
        ner_btn.pack(pady=(10, 10))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=25, height=3, command=self.perform_sentiment)
        sentiment_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=25, height=3, command=self.perform_emotion)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack()

    def perform_ner(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#695aa6', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#695aa6', fg='white')
        heading2.pack(pady=(20, 30))
        heading2.configure(font=('verdana', 15))

        label1 = Label(self.root, text='Enter the text:', bg='#695aa6', fg='white')
        label1.pack(pady=(5,10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5,10), ipady=4)

        ner_btn = Button(self.root, text='Perform NER', bg='#695aa6', fg='white', command=self.do_ner)
        ner_btn.pack(pady=(5, 5))

        self.ner_result = Label(self.root, text='', bg='#695aa6', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 11))

        back_btn = Button(self.root, text='Go Back', command=self.home_gui)
        back_btn.pack(pady=(5,5))

    def perform_sentiment(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#695aa6', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#695aa6', fg='white')
        heading2.pack(pady=(20, 30))
        heading2.configure(font=('verdana', 15))

        label1 = Label(self.root, text='Enter the text:', bg='#695aa6', fg='white')
        label1.pack(pady=(5,10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5,10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(5,5))

        self.sentiment_result = Label(self.root, text='', bg='#695aa6', fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana', 11))

        back_btn = Button(self.root, text='Go Back', command=self.home_gui)
        back_btn.pack(pady=(5,5))


    def perform_emotion(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#695aa6', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Detection', bg='#695aa6', fg='white')
        heading2.pack(pady=(20, 30))
        heading2.configure(font=('verdana', 15))

        label1 = Label(self.root, text='Enter the text:', bg='#695aa6', fg='white')
        label1.pack(pady=(5, 10))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        emotion_btn = Button(self.root, text='Analyze Sentiment', command=self.do_emotion)
        emotion_btn.pack(pady=(5, 5))

        self.emotion_result = Label(self.root, text='', bg='#695aa6', fg='white')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 11))

        back_btn = Button(self.root, text='Go Back', command=self.home_gui)
        back_btn.pack(pady=(5, 5))


    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        txt = ''
        for i in range(len(result[0])):
            txt += f'{result[0][i]['label']} : {round(result[0][i]['score'] * 100, 2)}%\n'
        self.sentiment_result['text'] = txt

    def do_ner(self):
        text = self.ner_input.get()
        result = self.apio.ner(text)
        txt = ""
        for i in range(len(result)):
            txt += f"'entity_group':'{result[i]['entity_group']}', 'word':'{result[i]['word']}', 'score':{round(result[i]['score']*100,2)}%\n"
        self.ner_result['text'] = txt

    def do_emotion(self):
        text = self.emotion_input.get()
        result = self.apio.emotion(text)
        txt = ''
        for emotion in result[0]:
            txt += f"'emotion':'{emotion['label']}', 'score':{round(emotion['score']*100,2)}%\n"
        self.emotion_result['text'] = txt

nlp = NLPApp()