from cgitb import text
from tkinter import *
import pandas as pd

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
        "Cement",
        "Plastic"]
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

# *********************************************************


# *** DATA SAVEING ****************************************

def SaveData(grantotal):
    df = pd.DataFrame([[name.get(),address.get(),
                        phone1.get(),phone2.get(),
                        (item1.get(),rate1.get(),Weight1.get()),
                        (item2.get(),rate2.get(),Weight2.get()),
                        (item3.get(),rate3.get(),Weight3.get()),
                        (item4.get(),rate4.get(),Weight4.get()),
                        grantotal
                        ]])
    df.to_csv("customers.csv",mode='a',header=None,index=None)

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
    
    GrandTotal = (float(rate1.get()) * float(Weight1.get()))+(float(rate2.get()) * float(Weight2.get()))+(float(rate3.get()) * float(Weight3.get()))+(float(rate4.get()) * float(Weight4.get()))
    
    SaveData(GrandTotal)
    
# *********************************************************

# *** TOTAL BUTTON ****************************************

TotalButton = Button(window,text="Total",command=CalcTotal)
TotalButton.place(x=372,y=360)

# *********************************************************


window.resizable(False, False)
window.mainloop()
