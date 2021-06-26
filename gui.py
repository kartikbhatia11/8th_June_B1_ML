import tkinter as tk

root = tk.Tk()
root.title('Calculas')
root.geometry('550x600')

string = '0'
exp = tk.StringVar(root)
exp.set(string)

tk.Entry(root,bg='light pink',textvariable=exp,justify='right',font=('calibre',18,'italic'),width=33).grid(row=0, column=0,columnspan=4,padx=5,pady=5,ipadx=54,ipady=54,sticky='w')



def press(a):
    global string
    if( a in '+*/-' and len(string)==0):
        exp.set("Operation Not allowed")
        return

    if (string[0]=='0' and a=='0'):
        return

    if (string[0]=='0' and a in '123456789'):
        string=a
        exp.set(string)
        return

    
    string = string+a
    exp.set(string)
    

def result():
    global string
    if(string[-1] in '+-*/'):
        string = '0'
        exp.set(string)
        return
    
    string = str(eval(string))
    exp.set(string)

def clear():
    global string
    string = '0'
    exp.set(string)

def bckspce():
    global string
    string = string[0:-1]
    if(len(string)==0):
        string = '0'
    exp.set(string)

tk.Button(root,text='Clear',justify='center',command=lambda:clear(),font=('calibre',14,'normal'),width=7).grid(row=1, column=0,columnspan=2,padx=3,pady=1,ipadx=88,ipady=20)
tk.Button(root,text='Bckscp  <--',justify='center',command=lambda:bckspce(),font=('calibre',14,'normal'),width=17).grid(row=1, column=2,columnspan=2,padx=3,pady=1,ipadx=34,ipady=20)



# 1st frame buttons
tk.Button(root,text='7',justify='center',command=lambda:press('7'),font=('calibre',14,'normal'),width=9).grid(row=2, column=0,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='8',justify='center',command=lambda:press('8'),font=('calibre',14,'normal'),width=9).grid(row=2, column=1,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='9',justify='center',command=lambda:press('9'),font=('calibre',14,'normal'),width=9).grid(row=2, column=2,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='+',justify='center',command=lambda:press('+'),font=('calibre',14,'normal'),width=9).grid(row=2, column=3,padx=1,pady=1,ipadx=8,ipady=20)

# 2nd frame buttons
tk.Button(root,text='4',justify='center',command=lambda:press('4'),font=('calibre',14,'normal'),width=9).grid(row=3, column=0,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='5',justify='center',command=lambda:press('5'),font=('calibre',14,'normal'),width=9).grid(row=3, column=1,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='6',justify='center',command=lambda:press('6'),font=('calibre',14,'normal'),width=9).grid(row=3, column=2,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='-',justify='center',command=lambda:press('-'),font=('calibre',14,'normal'),width=9).grid(row=3, column=3,padx=1,pady=1,ipadx=8,ipady=20)

# 3rd frame buttons
tk.Button(root,text='1',justify='center',command=lambda:press('1'),font=('calibre',14,'normal'),width=9).grid(row=4, column=0,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='2',justify='center',command=lambda:press('2'),font=('calibre',14,'normal'),width=9).grid(row=4, column=1,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='3',justify='center',command=lambda:press('3'),font=('calibre',14,'normal'),width=9).grid(row=4, column=2,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='*',justify='center',command=lambda:press('*'),font=('calibre',14,'normal'),width=9).grid(row=4, column=3,padx=1,pady=1,ipadx=8,ipady=20)

# 4th frame buttons
tk.Button(root,text='.',justify='center',command=lambda:press('.'),font=('calibre',14,'normal'),width=9).grid(row=5, column=0,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='0',justify='center',command=lambda:press('0'),font=('calibre',14,'normal'),width=9).grid(row=5, column=1,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='=',justify='center',command=lambda:result(),font=('calibre',14,'normal'),width=9).grid(row=5, column=2,padx=1,pady=1,ipadx=8,ipady=20)
tk.Button(root,text='/',justify='center',command=lambda:press('/'),font=('calibre',14,'normal'),width=9).grid(row=5, column=3,padx=1,pady=1,ipadx=8,ipady=20)

##l = ['', '789*', '456/', '123+','.0=-']
##
##for i in range(1,5):
##    for j in range(0,4):
##        tk.Button(root,text=l[i][j],justify='center',command=lambda:press()).grid(row=i, column=j,padx=3,pady=1,ipadx=49,ipady=20)


root.mainloop()
