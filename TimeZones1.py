from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
root=Tk()

root.geometry("1000x800")
root.title("Time Zones")

clockimg=ImageTk.PhotoImage(Image.open("clock.png"))
label1 = Label(root, text="India")
label1.place(relx=0.2, rely=0.1, anchor=CENTER)

label2 = Label(root)
label2["image"]=clockimg
label2.place(relx=0.2, rely=0.4, anchor=CENTER)

label3=Label(root)
label3.place(relx=0.2, rely=0.6,anchor=CENTER)

label4 = Label(root, text="Canada")
label4.place(relx=0.8, rely=0.1, anchor=CENTER)

label5 = Label(root)
label5["image"]=clockimg
label5.place(relx=0.8, rely=0.4, anchor=CENTER)

label6=Label(root)
label6.place(relx=0.8, rely=0.6,anchor=CENTER)

class india():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        label3["text"]="Time: "+current_time
        label3.after(200,self.times)

class canada():
    def times(self):
        home=pytz.timezone('US/Mountain')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        label6["text"]="Time: "+current_time
        label6.after(200,self.times)


oi=india()
ou=canada()

button2=Button(root,text="Time", command=ou.times)
button2.place(relx=0.8, rely=0.7,anchor=CENTER)

button1=Button(root,text="Time", command=oi.times)
button1.place(relx=0.2, rely=0.7,anchor=CENTER)

root.mainloop()