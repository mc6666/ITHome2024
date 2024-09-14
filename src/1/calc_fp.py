import tkinter as tk
from tkinter import ttk
from functools import partial

COLUMN_COUNT = 5   # 行數
FONT=('Arial', 16) # 字體
class App(tk.Tk):
    def __init__(self):
        # 呼叫 parent 的 __init__ 函數
        super().__init__() 
        
        # set window size
        self.geometry("")
        
        # set window title
        self.title('計算機')
              
        # create label
        self.label1 = tk.Label(self, text='輸入：', font=FONT)
        self.label1.grid(row=0, column=0)
        
        # create entry field
        self.equation = tk.StringVar() 
        self.expression_field = tk.Entry(self, textvariable=self.equation
        , font=FONT, borderwidth = 5) 
        self.expression_field.grid(row=0, column=1, columnspan=COLUMN_COUNT-1, ipadx=32)
        
        # create 0~9 buttons
        button_list = []
        for i in range(10):
            button_list.append(tk.Button(self, text=f' {i} ', 
                command=partial(self.button_click,i), 
                fg='black', bg='lightblue', height=1, width=8, font=FONT))
            grid_row, grid_column = divmod(i, COLUMN_COUNT)
            button_list[-1].grid(row=grid_row+1, column=grid_column) 
        
        # create '+', '-', '*', '/' buttons
        for j, text in enumerate(list('+-*/()=c')):
            button_list.append(tk.Button(self, text=f' {text} ', 
                command=partial(self.button_click,text), 
                fg='black', bg='lightgreen', height=1, width=8, font=FONT))
            grid_row2, grid_column = divmod(j, COLUMN_COUNT)
            button_list[-1].grid(row=grid_row+grid_row2+2, column=grid_column) 

        # error message
        self.message = tk.StringVar() 
        self.label_message = tk.Label(self, text='', textvariable = self.message)
        self.label_message.grid(row=grid_row+grid_row2+3, column=0, columnspan=COLUMN_COUNT)

    # button click event handler
    def button_click(self, num):
        if num == '=':
            # 計算
            try:
                # 顯示答案
                self.equation.set(str(eval(self.equation.get())))
            except Exception as e: # 錯誤處理
                self.message.set(repr(e)[:80])
        elif num == 'c':
            self.equation.set('') 
            self.message.set('') 
        else:
            self.expression_field.insert(tk.END, str(num))

if __name__ == "__main__":
    app = App()
    app.mainloop()