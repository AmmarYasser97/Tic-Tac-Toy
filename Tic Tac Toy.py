from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random  import randint


ActivePlayer=1
p1=[]   #what player 1 selected
p2=[]   #what player 2 selected

def set_name():
    global name1
    name1 = entry.get()
    entry.delete(0, END)
    global name2
    name2 = entry.get()
    entry.delete(0, END)

def Butclick(id):
    global ActivePlayer
    global p1
    global p2

    if(ActivePlayer == 1):
        SetLayout(id, 'X')
        p1.append(id)
        ActivePlayer=2
        root.title('X & O : Player 2')
    #    Autoplay()
    elif (ActivePlayer == 2):
        SetLayout(id, 'O')
        p2.append(id)
        ActivePlayer = 1
        root.title('X & O : Player 1')
    CheckWinner()

def SetLayout(id, text):
    if (id == 1):
        bu1.config(text=text)
        bu1.state(['disabled'])
    elif (id == 2):
        bu2.config(text=text)
        bu2.state(['disabled'])
    elif (id == 3):
        bu3.config(text=text)
        bu3.state(['disabled'])
    elif (id == 4):
        bu4.config(text=text)
        bu4.state(['disabled'])
    elif (id == 5):
        bu5.config(text=text)
        bu5.state(['disabled'])
    elif (id == 6):
        bu6.config(text=text)
        bu6.state(['disabled'])
    elif (id == 7):
        bu7.config(text=text)
        bu7.state(['disabled'])
    elif (id == 8):
        bu8.config(text=text)
        bu8.state(['disabled'])
    else:
        bu9.config(text=text)
        bu9.state(['disabled'])

def CheckWinner():
    winner=0

    if ((1 in p1)and(2 in p1)and(3 in p1)):
        winner = 1
    if ((1 in p2)and(2 in p2)and(3 in p2)):
        winner = 2
    if ((4 in p1)and(5 in p1)and(6 in p1)):
        winner = 1
    if ((4 in p2)and(5 in p2)and(6 in p2)):
        winner = 2
    if ((7 in p1)and(8 in p1)and(9 in p1)):
        winner = 1
    if ((7 in p2)and(8 in p2)and(9 in p2)):
        winner = 2
    if ((1 in p1)and(4 in p1)and(7 in p1)):
        winner = 1
    if ((1 in p2)and(4 in p2)and(7 in p2)):
        winner = 2
    if ((2 in p1)and(5 in p1)and(8 in p1)):
        winner = 1
    if ((2 in p2)and(5 in p2)and(8 in p2)):
        winner = 2
    if ((3 in p1)and(6 in p1)and(9 in p1)):
        winner = 1
    if ((3 in p2)and(6 in p2)and(9 in p2)):
        winner = 2
    if ((1 in p1)and(5 in p1)and(9 in p1)):
        winner = 1
    if ((1 in p2)and(5 in p2)and(9 in p2)):
        winner = 2
    if ((3 in p1)and(5 in p1)and(7 in p1)):
        winner = 1
    if ((3 in p2)and(5 in p2)and(7 in p2)):
        winner = 2

    if winner == 1:
        messagebox.showinfo('Winner.','Oh wow guess who win \n          MUBARAK '+ str(name1))
    if winner == 2:
        messagebox.showinfo('Winner.','Oh wow guess who win \n          MUBARAK '+ str(name2))
    if winner == 0 and len(p1) == 3 and len(p2) == 3:
        messagebox.showinfo('Winner','DEAD END !!')
        clinet_exit()

def Autoplay():
    global p1
    global p2
    EmbetyCell=[]
    for cell in range(1,10):
        if(not((cell in p1)or(cell in p2))):
            EmbetyCell.append(cell)
    Randindex=randint(0,len(EmbetyCell)-1)
    Butclick(Randindex)

def clinet_exit():
    if messagebox.askyesno("Quit", "Do you really wish to quit?"):
        exit()


root=Tk()
root.title('X & O : Player 1')

style=ttk.Style()
style.theme_use('xpnative')
style.configure('TButton', font=("Helvetica", 36, "bold"))
style.configure('info.TButton', font=("Helvetica", 12, 'normal'))

#add menu
#menubar = Menu(root)
#root.config(menu=menubar)

#file = Menu(menubar)
#file.add_command(lable='Exit', command=clinet_exit)
#menubar.add_cascade(lable='file', menu=file)

#add entry field
entry=ttk.Entry(root, width=40)
entry.grid(row=3, columnspan=2)

#lable to entry field
ttk.Label(root, text='Enter your name', font=("Helvetica", 14)).grid(row=3, column=0, padx=10, pady=10)

#make send button
button=ttk.Button(root, text='Send')
button.grid(row=3, column=1)
button.config(command=set_name)
button.configure(style='info.TButton')

#make quit button
quit_button=ttk.Button(root, text='Quit', command=clinet_exit, style='info.TButton')
quit_button.grid(row=3, column=2)


bu1=ttk.Button(root ,text=' ')
bu1.grid(row=0, column=0, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu1.config(command= lambda :Butclick(1))

bu2=ttk.Button(root ,text=' ')
bu2.grid(row=0, column=1, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu2.config(command= lambda :Butclick(2))

bu3=ttk.Button(root ,text=' ')
bu3.grid(row=0, column=2, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu3.config(command= lambda :Butclick(3))

bu4=ttk.Button(root ,text=' ')
bu4.grid(row=1, column=0, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu4.config(command= lambda :Butclick(4))

bu5=ttk.Button(root ,text=' ')
bu5.grid(row=1, column=1, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu5.config(command= lambda :Butclick(5))

bu6=ttk.Button(root ,text=' ')
bu6.grid(row=1, column=2, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu6.config(command= lambda :Butclick(6))

bu7=ttk.Button(root ,text=' ')
bu7.grid(row=2, column=0, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu7.config(command= lambda :Butclick(7))

bu8=ttk.Button(root ,text=' ')
bu8.grid(row=2, column=1, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu8.config(command= lambda :Butclick(8))

bu9=ttk.Button(root ,text=' ')
bu9.grid(row=2, column=2, sticky='snew', ipadx='40', ipady='40',padx='2', pady='2')
bu9.config(command= lambda :Butclick(9))

#messagebox.showwarning('Important.', 'DON\'T forget to enter players names' )

root.mainloop()