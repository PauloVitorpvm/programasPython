import webbrowser
mfrom Tkinter import *

root = Tk( )

root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abri o Google', command=google()).pack(pady=20)
root.mainloop()