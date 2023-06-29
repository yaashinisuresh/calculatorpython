from tkinter import *
from tkinter import ttk
st=""
root=Tk()
def press(n):
    global st
    if n=="C":
        txtexp.delete(0,END)
    elif n=="=":
        txtexp.delete(0, END)
        txtexp.insert(0,eval(st))
    else:
        st=txtexp.get()
        st=st+str(n)
        txtexp.delete(0,END)
        txtexp.insert(0,st)

root.title("MyClaculator")
txtexp=Entry(root)
txtexp.grid(row=1,columnspan=4)
btn0=Button(root,text=" 0 ",command=lambda:press(0))
btn0.grid(row=2,column=0)
btn1=Button(root,text=" 1 ",command=lambda:press(1))
btn1.grid(row=2,column=1)
btn2=Button(root,text=" 2 ",command=lambda:press(2))
btn2.grid(row=2,column=3)
btnplus=Button(root,text=" + ",command=lambda:press("+"))
btnplus.grid(row=2,column=4)

btn3=Button(root,text=" 3 ",command=lambda:press(3))
btn3.grid(row=3,column=0)
btn4=Button(root,text=" 4 ",command=lambda:press(4))
btn4.grid(row=3,column=1)
btn5=Button(root,text=" 5 ",command=lambda:press(5))
btn5.grid(row=3,column=3)
btnminus=Button(root,text=" - ",command=lambda:press("-"))
btnminus.grid(row=3,column=4)

btn6=Button(root,text=" 6 ",command=lambda:press(6))
btn6.grid(row=4,column=0)
btn7=Button(root,text=" 7 ",command=lambda:press(7))
btn7.grid(row=4,column=1)
btn8=Button(root,text=" 8 ",command=lambda:press(8))
btn8.grid(row=4,column=3)
btnmul=Button(root,text=" X ",command=lambda:press("*"))
btnmul.grid(row=4,column=4)

btn9=Button(root,text=" 9 ",command=lambda:press(9))
btn9.grid(row=5,column=0)
btnC=Button(root,text=" C ",command=lambda:press("C"))
btnC.grid(row=5,column=1)
btneql=Button(root,text=" = ",command=lambda:press("="))
btneql.grid(row=5,column=3)
btneql=Button(root,text=" / ",command=lambda:press("/"))
btneql.grid(row=5,column=4)
root.mainloop()