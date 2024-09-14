from tkinter import *

# 按鈕事件處理
def press(num): 
    global expression 
    expression_field.insert(END, str(num))

# create a GUI window 
app = Tk() 

# 表達式
equation = StringVar() 
expression_field = Entry(app, textvariable=equation) 
# 欄寬
expression_field.grid(columnspan=4, ipadx=70) 

# 建立按鈕
button1 = Button(app, text=' 1 ', fg='black', bg='lightblue', 
                command=lambda: press(1), height=1, width=7) 
button1.grid(row=2, column=0) 

# 監聽訊息 
app.mainloop() 