# to import tkinter Type "pip install tkinter" in Terminal
from tkinter import * # * means Import all.
from tkinter import ttk
import time # using this module we can access current time.
import webbrowser # used to play alarm sound on Youtube
from tkinter import messagebox # this creates a dialogue message box to set alarm.

root = Tk()
root.title("Alarm clock")
# this function is used  to give access to the submit button
def SubmitButton():
    AlarmTime= entry1.get()
    Message1()

    CurrentTime = time.strftime("%H:%M")
    print("the alarm time is: {}".format(AlarmTime))

    # this will ensure that the current time has not reached to the alarm time.
    while AlarmTime != CurrentTime:

        CurrentTime = time.strftime("%H:%M") # this tells the current time
        time.sleep(1)
 # this tells the code that the current time = the set time by the user.
    if AlarmTime == CurrentTime:
        print("now Alarm Musing Playing")
        # using this function we can access the YouTube to play alarm Sound.
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=GWXLPu8Ky9k')
def Message1():
    AlarmTimeLable= entry1.get()
    label2.config(text="the Alarm time is Counting...")
    #label2.config(text= "the Alarm will ring at {}".format(AlarmTimeLable))
    messagebox.showinfo(title = 'Alarm clock', message = 'Alarm will Ring at {}'.format(AlarmTimeLable))
frame1 = ttk.Frame(root)
frame1.pack()
frame1.config(height = 100, width = 100)

label1= ttk.Label(frame1,text = "Enter the Alarm time :")
label1.pack()


entry1 = ttk.Entry(frame1, width = 30)                  # all this is to create and style our message box in tkinter.
entry1.pack()
entry1.insert(3,"example - 13:15")

labelAlarmMessage= ttk.Label(frame1, text="Alarm Message:")
labelAlarmMessage.pack()

entry2= ttk.Entry(frame1, width=30)
entry2.pack()

button1= ttk.Button(frame1, text= "submit", command=SubmitButton)
button1.pack()

label2= ttk.Label(frame1)
label2.pack()


root.mainloop()

# coded by Vaibhav Krishna
# use it and make your own Alarm clock.
# not for commercial use