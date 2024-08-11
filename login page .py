from tkinter import *
root = Tk()
root.geometry("400x400")
root.configure(background="sky blue")
can = Canvas(root,bg="#D6EAF8",height=1000,width=800)
can.pack(padx=70,pady=200)
lable1 = Label(root,text="LOGIN",bg="#D6EAF8",font=("BOLD",15),fg="sky blue")
lable1.pack()
lable1.place(x=275,y=250)

lable2 = Label(root,text="USERNAME",bg="#D6EAF8",font=("BOLD",15),fg="sky blue")
lable2.place(x=205,y=370)

entry1 = Entry(root)
entry1.pack()

root.mainloop()