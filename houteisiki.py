import math
import tkinter as tk
import tkinter.messagebox as tmsg

#2次方程式を解く
def solve_x(a,b,c):
    x = []
    x_tmp = (-1*b + math.sqrt(b*b - 4*a*c)) / 2*a
    x.append(x_tmp)
    x_tmp = (-1*b - math.sqrt(b*b - 4*a*c)) / 2*a
    x.append(x_tmp)
    return x

#ボタンがクリックされたときの処理
def ButtonClick():
    a = editboxa.get()
    b = editboxb.get()
    c = editboxc.get()
    if int(a) == 0:
        tmsg.showinfo("error!", "x^2の係数が0です") 
    elif int(b)*int(b) - 4*int(a)*int(c) > 0:       # D > 0 → 実数解:2個
        if int(c) == 0:                                  #c=0 → x1=0
            tmsg.showinfo("x1=", "0")                    #分子=0となると、x=0と表示できないようです(*)
            tmsg.showinfo("x2=", solve_x(int(a),int(b),int(c))[1])
        else:
            tmsg.showinfo("x1=", solve_x(int(a),int(b),int(c))[0])
            tmsg.showinfo("x2=", solve_x(int(a),int(b),int(c))[1])
    elif int(b)*int(b) - 4*int(a)*int(c) == 0:      # D = 0 → 実数解:1個
        if int(b) == 0:
            if int(c) == 0:                              #b=0 かつ c=0 → x=0 
                tmsg.showinfo("x=", "0")                 #(*)
        else:
            tmsg.showinfo("x=", solve_x(int(a),int(b),int(c))[0])
    else:                                           # D < 0 → 実数解:0個
        tmsg.showinfo("error!", "実数解が存在しません")

#メインのプログラム
#ウィンドウを作る
root = tk.Tk()
root.geometry("320x320")
root.title("2次方程式の解を求める")

#ラベルを作る
label1 = tk.Label(root, text="ax^2 + bx + c = 0", font=("Helevetica", 30))
label1.place(x = 20, y = 20)
labela = tk.Label(root, text="a=", font=("Helevetica", 30))
labela.place(x = 100, y = 85)
labelb = tk.Label(root, text="b=", font=("Helevetica", 30))
labelb.place(x = 100, y = 130)
labelc = tk.Label(root, text="c=", font=("Helevetica", 30))
labelc.place(x = 100, y = 175)

#テキストボックスを作る
editboxa = tk.Entry(width = 3, font=("Helevetica", 30))
editboxa.place(x = 150, y = 85)
editboxb = tk.Entry(width = 3, font=("Helevetica", 30))
editboxb.place(x = 150, y = 130)
editboxc = tk.Entry(width = 3, font=("Helevetica", 30))
editboxc.place(x = 150, y = 175)

#ボタンを作る
button1 = tk.Button(root, text = "solve", font=("Helevetica", 30), command=ButtonClick)
button1.place(x = 100, y = 240)

#ウィンドウを表示する
root.mainloop()