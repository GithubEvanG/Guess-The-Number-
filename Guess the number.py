from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random
window = ThemedTk(theme='breeze')
window.title("guess the number")
window.geometry('350x350')

def start():
    global Number
    if Difficulty.get()=="Easy":
        Number=random.randint(1,50)
    elif Difficulty.get()=="Medium":
        Number=random.randint(1,250)
    else:
        Number = random.randint(1,500)
    button8.place_forget()
def Game(event):
    global txt1
    if txt1.get() !="":
        Guess=int(txt1.get())
        txt1.delete(0, END)
        global Number
        if Number<Guess:
            lbl100.configure(image=downarrow)


        elif Number>Guess:
            lbl100.configure(image=uparrow)

        else:
            lbl100.configure(image=Tick)
            button8.place(x=150, y=210)
def Exit():
    window.destroy()

uparrow=PhotoImage(file="../../TkinterProjects/General Exercises/uparrow.png")
downarrow=PhotoImage(file="../../TkinterProjects/General Exercises/downarrow.png")
Tick=PhotoImage(file="../../TkinterProjects/General Exercises/correct.png")
Dice=PhotoImage(file="../../TkinterProjects/General Exercises/die.png")


lbl1 = ttk.Label(window, text=' GUESS THE NUMBER !!!', cursor="dot" , font=( 'Arial',20, 'bold'))
lbl1.pack()
lbl2 = ttk.Label(window, text=' in this game you will try to find a secret number ', font=( 'Arial',10, 'bold'))
lbl2.pack()
lbl3 = ttk.Label(window, text=' that is randomly chosen every round ', font=( 'Arial',10, 'bold'))
lbl3.pack()
lbl4 = ttk.Label(window, text=' Try to guess it with the least possible tries! ', font=( 'Arial',10, 'bold'))
lbl4.pack()
txt1 = Entry(window, width=10, fg='red', bg='white', font=('Arial', 15), cursor="dot", relief='solid')
txt1.place(x=125 , y=180)
button7 = ttk.Button(window, text='Exit!', cursor="dot", command=Exit)
button7.place(x=250 , y=180)
button8 = ttk.Button(window, image=Dice, cursor="dot",command=start)
button8.place(x=150 , y=210)




Difficulty=StringVar()

rad1 = ttk.Radiobutton(window,text='̴̧̲̬̔̇̓͠͝Ȩ̵̹́z̵̧̪̮̤̐̉̓͝ỹ̶̝͉̜́ ̴͍̩̈́̈́̿̓͋m̷̭̦͗͒͊̃̽͜ö̵̧̢̠͊̀ḓ̶͂̐̇̓è̷͕̖͉͑ ',value="Easy", variable=Difficulty)
rad1.place(x=20 , y=110)

rad2 = ttk.Radiobutton(window,text='Medium',value="Medium", variable=Difficulty)
rad2.place(x=100 , y=110)

rad3 = ttk.Radiobutton(window,text='H̸̡̧̧̟̙̣͉͉͎͓̤̣̘͙̲̀͛́̓͆̽̿̋̍͛̋̐̐͂͗̌͌̀̈̌̍̚͝á̵̧̨̢̢̢̢̛̛͔͉̱͉̹͕̮̰̖͈̻̙͚̱̳͓͔̖͈͕̐̇́̍͌̌͑́́̽͑̌̿̿̀̀̋̽̕͠͝ͅȑ̴̢̡̢̧̨̨̗̝͍̤͎̭̯̝̲̳̙͙͎̤̳̫̝͎̭͚̖̟̤̗̜̑̀̀͋̾͊͛̍̑̆̅̚d̶̨͍̦͇̠͉̗͉̺̪̹̪͈̗͙͚͎̞͎̞͙̫̊̀͐̈͆͐̊̎̈́̈̂͆̈́́̄̓̿̀͘͘͘͠͠͝ ̵̨̡̛̙̦̥̮̯̦̯̣̬̼͍̳̬͚̠̲̗̱̭͍͇̫͚̤̻̖̎̇̓̏̏̃͛͋̀͐̃́͊͂̉̔̽̍̿͝͝͝͝ͅm̵̡̗͍͖̰̭̳̬̰̼̆͌̎͒̉̾̒̆̑̅͛͆͌̒̃̑̔͋͗͑̚͜ơ̵̢̢͍̠̞̥̩̩̳͈̞̰͓͖͇͖̯͈̣̹͍̮̐́̇̎̿̽̊̉̉͑̀̈́̈́͂̇̈̆̍́͐͆͒̈́͘̚͜͝͝͠ͅͅd̸̡̢̛̛̥̤̠̹̣̗̩̱͔̖͙͚͓̺̪̼̳̠͙͈̼͍̠̜̰̪̍͒͒̓̿̿̉̄̉̎̔́͊̾͒̎̓̍̋̌͊́́͘͜͠͝͠ę̵͇̳̪̰̭̺͓͕̱̯̣̐̂͋̉͗̏̆̿͌͛͘͝ͅ',value="hard", variable=Difficulty)
rad3.place(x=200 , y=110)




window.bind("<Return>", Game)




lbl100 = ttk.Label(window, text='', font=( 'Arial',20, 'bold'))
lbl100.place(x=40, y=215)


window.mainloop()