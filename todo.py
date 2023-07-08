from tkinter import *
from tkinter import filedialog
import pickle
import os
task =[]
#fuctions
def addstuff():
    content=stuff.get()
    task.append(content)
    count=len(task)
    for i in task:
        if task.index(i)==count-1:
            display.insert(END,i)
    stuff.delete(0,END)

def remove():
    sel = display.curselection()
    for index in sel[::-1]:
        display.delete(index)
    #for item in display.curselection():
     #   a=int(item)
      #  task.pop(a)
      #  display.delete(display.curselection())

def save_list():
    filename=filedialog.asksaveasfilename( initialdir="C:\\Users\\Admin\\OneDrive\\Documents\\to-do-list\\to-do-list\\data\\",title="save list", filetype=(("Dat File",".dat"),("All files",".*")))
    if filename:
        if filename.endswith(".dat"):
            pass
        else:
            filename=f'{filename}.dat'
    items=display.get(0,END)
    outputfile=open(filename,'wb')
    pickle.dump(items,outputfile)
    display.delete(0,END)

def open_list():
    filename=filedialog.askopenfilename( initialdir="C:\\Users\\Admin\\OneDrive\\Documents\\to-do-list\\to-do-list\\data\\",title="open list", filetype=(("Dat File",".dat"),("All files",".*")))
    if filename:
        display.delete(0,END)
        inputfile=open(filename,'rb')
        item=pickle.load(inputfile)
        for i in item:
            display.insert(END,i)
    

def delete_list():
    display.delete(0,END)
    
#window
window=Tk()
window.title("to-do list")
window.geometry("500x500")
label=Label(window,text="TO DO LIST",font=("Arial",30)).pack()

#listbox
display = Listbox(window,font=('Helvetica', 12), height=12, width=500,selectmode="multiple")
display.place(x=0,y=50)

#scroll bar
scrollbar = Scrollbar(window)
scrollbar.pack(side = RIGHT, fill = BOTH)
display.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = display.yview)



#insert task
for i in task:
    display.insert(END,i)

#inputing tasks
stuff=Entry(window,font=("Arial"),width=37)
stuff.place(x=60,y=350)

mymenu=Menu(window)
window.config(menu=mymenu)
filemenu=Menu(mymenu,tearoff=False)
mymenu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Save list',command=save_list)
filemenu.add_command(label='Open list',command=open_list)
filemenu.add_separator()
filemenu.add_command(label='Clear list',command=delete_list)

#delete,quit and new
delete = Button(window, text = 'Quit',command = window.destroy,height= 5, width=25) 
delete.pack(anchor='s',side = 'right')
new = Button(window, text = 'Add',height= 5, width=25,command = addstuff) 
new.pack(anchor='sw',side='left')
remove = Button(window, text = 'Remove',height= 5, width=25, command = remove ) 
remove.pack(anchor='s',side='bottom')

window.mainloop()