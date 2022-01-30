from cgitb import text
from functools import total_ordering
from tkinter import *
from numpy import gradient
import pandas as pd
import datetime

window = Tk()

window.geometry("999x599")
window.configure(bg = "#ffffff")
# *** CANVAS **********************************************
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 599,
    width = 999,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

# *** BACKGROUD IMAGE *************************************
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500, 289,
    image=background_img)


# *** DATE TIME *******************************************

date_time = datetime.datetime.now()

# *********************************************************

# *** CUSTOMER INFO INPUTS ********************************

name = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
name.place(x=95, y=77, width=146, height=27)

address = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
address.place(x=338, y=77, width=146, height=27)

phone1 = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
phone1.place(x=579, y=77, width=146, height=27)

phone2 = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
phone2.place(x=821, y=77, width=146, height=27)

# *********************************************************

# *** DROP DOWN ITEMS *************************************
DropDownItems = ["Steel 1/2",
        "Steel 1/4",
        "Steel 3/8",
        "Steel 3/4",
        "Steel 5/16",
        'Steel 1"',
        'Steel 4NO',
        'Steel 8NO',
        'Steel 9NO',
        'Karachi Steel',
        "Plastic",
        "Cement",
        "Tiron",
        "Wending Wire",
        "Garder 7x4",
        "Garder 18LBS",
        "Garder 22LBS",
        "Garder 25LBS",
        ]
# *********************************************************

# *** DROP DOWNS ******************************************

item1 = StringVar()
# item1.set("Item 1")
DropDown1 = OptionMenu(window,item1,*DropDownItems)
DropDown1.place(x=38,y=200)

item2 = StringVar()
# item2.set("Item 2")
DropDown2 = OptionMenu(window,item2,*DropDownItems)
DropDown2.place(x=38,y=240)

item3 = StringVar()
# item3.set("Item 3")
DropDown3 = OptionMenu(window,item3,*DropDownItems)
DropDown3.place(x=38,y=280)

item4 = StringVar()
# item4.set("Item 4")
DropDown4 = OptionMenu(window,item4,*DropDownItems)
DropDown4.place(x=38,y=320)

item5 = StringVar()
# item4.set("Item 4")
DropDown5 = OptionMenu(window,item5,*DropDownItems)
DropDown5.place(x=38,y=360)

item6 = StringVar()
# item4.set("Item 4")
DropDown6 = OptionMenu(window,item6,*DropDownItems)
DropDown6.place(x=38,y=400)

item7 = StringVar()
# item4.set("Item 4")
DropDown7 = OptionMenu(window,item7,*DropDownItems)
DropDown7.place(x=38,y=440)

# *********************************************************

# *** RATE INPUTS *****************************************

rate1 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
rate1.place(x=263, y=202, width=82, height=23)
rate1.insert(0,0)

rate2 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
rate2.place(x=263, y=242, width=82, height=23)
rate2.insert(0,0)

rate3 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
rate3.place(x=263, y=282, width=82, height=23)
rate3.insert(0,0)

rate4 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
rate4.place(x=263, y=322, width=82, height=23)
rate4.insert(0,0)

rate5 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
rate5.place(x=263, y=362, width=82, height=23)
rate5.insert(0,0)

rate6 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
rate6.place(x=263, y=402, width=82, height=23)
rate6.insert(0,0)

rate7 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
rate7.place(x=263, y=442, width=82, height=23)
rate7.insert(0,0)

# *********************************************************

# *** WEIGHT INPUTS ***************************************

Weight1 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
Weight1.place(x=372, y=202, width=82, height=23)
Weight1.insert(0,0)

Weight2 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
Weight2.place(x=372, y=242, width=82, height=23)
Weight2.insert(0,0)

Weight3 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
Weight3.place(x=372, y=282, width=82, height=23)
Weight3.insert(0,0)

Weight4 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
Weight4.place(x=372, y=322, width=82, height=23)
Weight4.insert(0,0)

Weight5 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
Weight5.place(x=372, y=362, width=82, height=23)
Weight5.insert(0,0)

Weight6 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
Weight6.place(x=372, y=402, width=82, height=23)
Weight6.insert(0,0)

Weight7 = Entry(bd=0, bg="#ffffff", highlightthickness=0)
Weight7.place(x=372, y=442, width=82, height=23)
Weight7.insert(0,0)

# *********************************************************

# *** TOTAL FUNCTION  *************************************



def CalcTotal():
    total1 = Label(text= (float(rate1.get()) * float(Weight1.get()) ),padx=10,pady=3)
    total1.place(x=480,y=200)

    total2 = Label(text= (float(rate2.get()) * float(Weight2.get()) ),padx=10,pady=3)
    total2.place(x=480,y=240)

    total3 = Label(text= (float(rate3.get()) * float(Weight3.get()) ),padx=10,pady=3)
    total3.place(x=480,y=280)

    total4 = Label(text= (float(rate4.get()) * float(Weight4.get()) ),padx=10,pady=3)
    total4.place(x=480,y=320)

    total5 = Label(text= (float(rate5.get()) * float(Weight5.get()) ),padx=10,pady=3)
    total5.place(x=480,y=360)

    total6 = Label(text= (float(rate6.get()) * float(Weight6.get()) ),padx=10,pady=3)
    total6.place(x=480,y=400)

    total7 = Label(text= (float(rate7.get()) * float(Weight7.get()) ),padx=10,pady=3)
    total7.place(x=480,y=440)
    
    GrandTotal = (float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))

    Grand = Label(text=GrandTotal,padx=10,pady=3)
    Grand.place(x=477,y=535)

    
# *********************************************************

# *** TOTAL BUTTON ****************************************

TotalButton = Button(window,text="Total",command=CalcTotal,padx=10,pady=10)
TotalButton.place(x=368,y=530)

# *********************************************************

# *** PAYMENT INFO INPUTS *********************************

recived = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
recived.insert(0,0)
recived.place(x=653, y=197, width=178, height=27)

remaning = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
remaning.insert(0,0)
remaning.place(x=653, y=269, width=178, height=27)

dueDate = Entry(bd=0, bg="#C4C4C4", highlightthickness=0)
dueDate.place(x=653, y=339, width=178, height=27)


# *********************************************************

# *** DATA SAVEING ****************************************

def SaveData():
    total =((float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))),
    df = pd.DataFrame([[date_time, name.get(),address.get(),
                        phone1.get(),phone2.get(),
                        ((float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))+(float(rate5.get()) * float(Weight5.get()))+(float(rate6.get()) * float(Weight6.get()))+(float(rate7.get()) * float(Weight7.get()))),
                        recived.get(),remaning.get(),dueDate.get(),
                        (item1.get(),rate1.get(),Weight1.get()),
                        (item2.get(),rate2.get(),Weight2.get()),
                        (item3.get(),rate3.get(),Weight3.get()),
                        (item4.get(),rate4.get(),Weight4.get()),
                        (item5.get(),rate5.get(),Weight5.get()),
                        (item6.get(),rate6.get(),Weight6.get()),
                        (item7.get(),rate7.get(),Weight7.get()),
                        ]])
    df.to_csv("customers.csv",mode='a',header=None,index=None)

# *********************************************************


# *** SAVE BUTTON ****************************************

SaveButton = Button(window,text="Save Data",command=SaveData,padx=10,pady=10)
SaveButton.place(x=268,y=530)

# *********************************************************


window.resizable(False, False)
window.mainloop()
