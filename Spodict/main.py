from tkinter import *
from PIL import ImageTk,Image  
from backend import *

window = Tk()
window.title('SpoDict')
window.config(bg='#06006c')
window.geometry("700x700")
window.iconbitmap('logo.ico')
speak = Speaking()
mic = ImageTk.PhotoImage(Image.open("mic.jpeg"))  

meaning_box=Label( window,text='type in box the then hit "Get meaning" button',fg="white",
	bg="#06006c",
	font=('Consolas',15))

def get_meaning_of_word():
	if search_box.get().strip():
		word=Dictionary(query=search_box.get())
		if word:
			meaning_box.config(text=word['Noun'][0])
			for state in word:
				print(word[state])
				speak.speak("the meaning  is" + str(word[state]))
		else:
			word="No Meaning found Try again" 
			meaning_box.config(text=word)
			speak.speak(word)


Label( window,image=mic,
	bg="#06006c",
	font=('Calibri',15)).pack()

Label( window,text='SpoDict',fg="white",
	bg="#06006c",
	font=('Arial Bold',40)).pack()
Label( window,text='MINIPROJECT',fg="white",
	bg="#06006c",
	font=('Calibri',15)).pack()

Label( window,text='Dear user which word do you want to find meaning \n',fg="white",
	bg="#06006c",
	font=('Consolas',15)).pack()

search_box =Entry(window,
		font=('Georgia',30),
		fg="black",bg="#00feca",
		highlightthickness=3,
		highlightbackground = "red",
		highlightcolor= "red")
submit_button=Button(window,text='Get meaning',
			font=('Century',25),
			activebackground="#ce8ac0",
			bg='#998ace',
			command= get_meaning_of_word
			)
meaning_box=Label( window,text='type in box the then hit "Get meaning" button',fg="white",
	width=100,
	bg="#06006c",
	font=('Consolas',15))

search_box.pack(ipadx = 30, ipady = 15,pady=10)
submit_button.pack()
meaning_box.pack()

window.mainloop()
