import tkinter
win=tkinter.Tk()
win.title("batch-2pm")
win.configure(bg='black')
win.maxsize(600,600)
win.minsize(400,400)

def submit():
    print(e1.get())
    l3.config(text=e1.get())
    # f=open('tkex.py','a')
    # f.write(e1.get())
    if var1.get()==1:
        print('male')
    else:
        print('female')    

l1=tkinter.Label(win,text='sample win',bg="red")
l1.place(x=170,y=25)
l2=tkinter.Label(win,text="name",bg="black",fg="white")
l2.place(x=65,y=55)

e1=tkinter.Entry(win)
e1.place(x=130,y=55)

l4=tkinter.Label(win,text="Gender")
l4.place(x=65,y=95)
var1=tkinter.IntVar()

r1=tkinter.Radiobutton(win,text="male",variable=var1,value=1)
r1.place(x=145,y=95)
r1=tkinter.Radiobutton(win,text="female",variable=var1,value=2)
r1.place(x=235,y=95)


btn1=tkinter.Button(win,text="submit",bg='blue',fg='white',activebackground='blue',activeforeground='white',padx=10,pady=10,command=submit)
btn1.pack()

btn1.place(x=170,y=150)
l3=tkinter.Label(win)
l3.place(x=165,y=245)
win.mainloop()