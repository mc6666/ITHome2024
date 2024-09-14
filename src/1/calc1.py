from tkinter import *

# 按鈕事件處理
def press(num): 
    global expression 
    expression_field.insert(END, str(num))

# 清除輸入列    
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

# 計算
def calc(): 
    try: 
        global expression 
        total = str(eval(equation.get())) 
        equation.set(total) 
        expression = str(total) 
    except: 
        equation.set(" error ") 
        expression = "" 

# create a GUI window 
app = Tk() 

# set the configuration of GUI window 
app.geometry("280x180") 

# 表達式
equation = StringVar() 
expression_field = Entry(app, textvariable=equation) 
# 欄寬
expression_field.grid(columnspan=4, ipadx=70) 

# 建立0~9按鈕
button1 = Button(app, text=' 1 ', fg='black', bg='lightblue', 
                command=lambda: press(1), height=1, width=7) 
button1.grid(row=2, column=0) 

button2 = Button(app, text=' 2 ', fg='black', bg='lightblue', 
                command=lambda: press(2), height=1, width=7) 
button2.grid(row=2, column=1) 

button3 = Button(app, text=' 3 ', fg='black', bg='lightblue', 
                command=lambda: press(3), height=1, width=7) 
button3.grid(row=2, column=2) 

button4 = Button(app, text=' 4 ', fg='black', bg='lightblue', 
                command=lambda: press(4), height=1, width=7) 
button4.grid(row=3, column=0) 

button5 = Button(app, text=' 5 ', fg='black', bg='lightblue', 
                command=lambda: press(5), height=1, width=7) 
button5.grid(row=3, column=1) 

button6 = Button(app, text=' 6 ', fg='black', bg='lightblue', 
                command=lambda: press(6), height=1, width=7) 
button6.grid(row=3, column=2) 

button7 = Button(app, text=' 7 ', fg='black', bg='lightblue', 
                command=lambda: press(7), height=1, width=7) 
button7.grid(row=4, column=0) 

button8 = Button(app, text=' 8 ', fg='black', bg='lightblue', 
                command=lambda: press(8), height=1, width=7) 
button8.grid(row=4, column=1) 

button9 = Button(app, text=' 9 ', fg='black', bg='lightblue', 
                command=lambda: press(9), height=1, width=7) 
button9.grid(row=4, column=2) 

button0 = Button(app, text=' 0 ', fg='black', bg='lightblue', 
                command=lambda: press(0), height=1, width=7) 
button0.grid(row=5, column=0) 

plus = Button(app, text=' + ', fg='black', bg='lightblue', 
            command=lambda: press("+"), height=1, width=7) 
plus.grid(row=2, column=3) 

# 建立【+-*/】按鈕
minus = Button(app, text=' - ', fg='black', bg='lightblue', 
            command=lambda: press("-"), height=1, width=7) 
minus.grid(row=3, column=3) 

multiply = Button(app, text=' * ', fg='black', bg='lightblue', 
                command=lambda: press("*"), height=1, width=7) 
multiply.grid(row=4, column=3) 

divide = Button(app, text=' / ', fg='black', bg='lightblue', 
                command=lambda: press("/"), height=1, width=7) 
divide.grid(row=5, column=3) 

equal = Button(app, text=' = ', fg='black', bg='lightblue', 
            command=calc, height=1, width=7) 
equal.grid(row=5, column=2) 

# 建立其他按鈕
clear1 = Button(app, text='Clear', fg='black', bg='lightblue', 
            command=clear, height=1, width=7) 
clear1.grid(row=5, column='1') 

Decimal= Button(app, text='.', fg='black', bg='lightblue', 
                command=lambda: press('.'), height=1, width=7) 
Decimal.grid(row=6, column=0) 


# start the GUI 
app.mainloop() 
