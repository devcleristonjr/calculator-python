from tkinter import *
from tkinter import ttk

# cores
co1 = "#feffff"  # white/branca
co2 = "#38576b"
co3 = "#2ed175"
co4 = "#f52059"  # red
fundo = "#3b3b3b"

window = Tk()
window.title("Calculator")
window.geometry("235x318")
window.config(bg=co1)

# frames
ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_display = Frame(
    window,
    width=300,
    height=56,
    bg=co2,
    pady=0,
    padx=0,
    relief="flat",
)
frame_display.grid(row=1, column=0, sticky=NW)

frame_body = Frame(
    window,
    width=300,
    height=340,
    bg=fundo,
    pady=0,
    padx=0,
    relief="flat",
)
frame_body.grid(row=2, column=0, sticky=NW)

# label

app_display = Label(
    frame_display,
    text="123456789",
    width=16,
    height=2,
    padx=7,
    relief="flat",
    anchor="e",
    bd=0,
    justify=RIGHT,
    font=("Ivy 18 "),
    bg="#37474F",
    fg=co1,
)
app_display.place(x=0, y=0)

# buttons

b_1 = Button(frame_body,command = lambda: clear_display(), text="C", width=11, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_body,command = lambda: enter_value('%'), text="%", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_body,command = lambda: enter_value('/'), text="/", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)
 
b_4 = Button(frame_body,command = lambda: enter_value('7'), text="7", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_body,command = lambda: enter_value('8'), text="8", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_body,command = lambda: enter_value('9'), text="9", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_body,command = lambda: enter_value('*'), text="*", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)
 
b_8 = Button(frame_body,command = lambda: enter_value('4'), text="4", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_body,command = lambda: enter_value('5'), text="5", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_body,command = lambda: enter_value('6'), text="6", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_body,command = lambda: enter_value('-'), text="-", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)
 
b_12 = Button(frame_body,command = lambda: enter_value('1'), text="1", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_body,command = lambda: enter_value('2'), text="2", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_body,command = lambda: enter_value('3'), text="3", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_body,command = lambda: enter_value('+'), text="+", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)
 
b_16 = Button(frame_body,command = lambda: enter_value('0'), text="0", width=11, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_body,command = lambda: enter_value('.'), text=".", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_body,command = lambda: calcular(), text="=", width=5, height=2, bg=co4, fg=co1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


all_values = "" 
 
text_values = StringVar()

def enter_value(event):
    global all_values
    all_values = all_values + str(event)
    text_values.set(all_values)

app_scream = Label(frame_display,textvariable=text_values,width=16,height=2, padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=co1)
app_scream.place(x=0, y=0)

def calcular():
    global all_values
    result = str(eval(all_values))
    text_values.set(result)
    all_values = ""

    
def clear_display(): 
    global all_values
    all_values = "" 
    text_values.set("")



window.mainloop()