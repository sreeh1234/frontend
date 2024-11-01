import sqlite3
con=sqlite3.connect("tkexam.db")
try:
    con.execute("create table userdata(Id int,Name text,Age int,gender text)")
except:
    print("table created")
        

import tkinter
win=tkinter.Tk()
win.title("example")
win.configure(bg="grey")
win.minsize(500,500)
win.maxsize(700,700)

def submit():
    # print(e1.get())
    # print(e2.get())
    # print(e3.get())
    
    if var1.get()==1:
        gender="male"
    else:
        gender="female"    
    con.execute("insert into userdata(Id,Name,Age,gender)values(?,?,?,?)",(e1.get(),e2.get(),e3.get(),gender))
    con.commit()

l1=tkinter.Label(win,text="Id")
l1.place(x=155,y=20)

l2=tkinter.Label(win,text="Name")
l2.place(x=128,y=50)

l3=tkinter.Label(win,text="Age")
l3.place(x=143,y=80)

r1=tkinter.Label(win,text="Gender")
r1.place(x=120,y=120)

e1=tkinter.Entry(win)
e1.place(x=190,y=20)

e2=tkinter.Entry(win)
e2.place(x=190,y=50)

e3=tkinter.Entry(win)
e3.place(x=190,y=80)

var1=tkinter.IntVar()

r1=tkinter.Radiobutton(win,text="Male",variable=var1,value=1)
r1.place(x=190,y=120)
r1=tkinter.Radiobutton(win,text="Female",variable=var1,value=2)
r1.place(x=276,y=120)

btn=tkinter.Button(win,text="Submit",background="blue",foreground="white",command=submit)
# btn.pack()
btn.place(x=225,y=180)


win.mainloop()
