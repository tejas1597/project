import pandas as pd
from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First')
        self.lbl2=Label(win, text='Second ')
        self.lbl3=Label(win, text='Third')
        self.lbl4=Label(win, text='Result1')
        self.lbl5=Label(win, text='Result2')
        self.lbl6=Label(win, text='Result3')

        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry(win,width='50',font=('Bold'))
        self.t5=Entry(win,width="50",font=('Bold'))
        self.t6=Entry(win,width="50",font=('Bold'))
        
        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=100, y=100)
        self.lbl3.place(x=100, y=150)
        self.lbl4.place(x=100, y=300)
        self.lbl5.place(x=100, y=350)
        self.lbl6.place(x=100, y=400)

        self.t1.place(x=200, y=50)
        self.t2.place(x=200, y=100)
        self.t3.place(x=200, y=150)
        self.t4.place(x=200, y=300)
        self.t5.place(x=200, y=350)
        self.t6.place(x=200, y=400)
        
        self.b1 = Button(win, text="Submit",bd=3,width=20,height=2,command=lambda:[self.add(),self.add1(),self.add2()])
        self.b1.place(x=100, y=200)
        self.btn1 = Button(win, text='Click')
        
    def add(self):
        self.t4.delete(0, 'end')
        rec = pd.read_csv(r"c:\\Users\HP\\Downloads\recommendations3.csv" )
        ante = set(rec['antecedents'])
        d = {}
        l =[]
        for i in ante:
            df = rec[rec['antecedents'] == i]
            d[i] = list(df['consequents'].unique())
        i = input("Enter what you want: ")
        self.t4.delete(0, 'end')
        result1=(d[i])
        self.t4.insert(END, str(result1))
    def add1(self):
        rec = pd.read_csv(r"c:\\Users\HP\\Downloads\recommendations3.csv" )
        #print(rec.head(20))
        ante = set(rec['antecedents'])
        d = {}
        l =[]
        for i in ante:
            df = rec[rec['antecedents'] == i]
            d[i] = list(df['consequents'].unique())
        i = input("Enter what you want: ")
    
        self.t5.delete(0, 'end')
        result2=(d[i])
        self.t5.insert(END, str(result2))
    def add2(self):
        rec = pd.read_csv(r"c:\\Users\HP\\Downloads\recommendations3.csv" )
        #print(rec.head(20))
        ante = set(rec['antecedents'])
        d = {}
        l =[]
        for i in ante:
            df = rec[rec['antecedents'] == i]
            d[i] = list(df['consequents'].unique())
        i = input("Enter what you want: ")
        self.t6.delete(0, 'end')
        result3=(d[i])
        self.t6.insert(END, str(result3))
        
window=Tk()
mywin=MyWindow(window)
window.title('E-Commerce Recommendations')
window.geometry("700x600+10+10")
window.mainloop()
