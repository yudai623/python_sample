# 引用元
[#63「【Python講座】２次方程式の解を自動で求めるプログラムを作ろう！（前編）」](https://ameblo.jp/n2r2010/entry-12725002112.html)

[#65「【Python講座】２次方程式の解を自動で求めるプログラムを作ろう！（後編）」](https://ameblo.jp/n2r2010/entry-12725021509.html)
# 改変部分について
## ①判別式Dについて
```bash
def eval_Discriminant(a,b,c):
    D = b*b - 4*a*c
    return D
```
引用元では上記のように判別式Dを定義していたが、その通りに行うと、
```bash
elif eval_Discriminant(int(a),int(b),int(c)) > 0:
elif eval_Discriminant(int(a),int(b),int(c)) = 0:
elif eval_Discriminant(int(a),int(b),int(c)) < 0:
```
の部分で、def内でintは使えず計算できないというエラーメッセージが表示されたため、
```bash
elif int(b)*int(b) - 4*int(a)*int(c) > 0:
elif int(b)*int(b) - 4*int(a)*int(c) = 0:
```
のように、判別式を定義せず、直接計算させることにして対処した。また、
```bash
elif int(b)*int(b) - 4*int(a)*int(c) < 0:
```
については、
```bash
else
```
でも同じ意味となるため、より短く済む**else**を用いた。
## ②x=0を解に持つ場合について
x=0を解に持つとき、0という文字が表示されなかったため、判別式と係数の情報から、x=0を解に持つ場合、0という文字を表示するようにして対処した。
```bash
    elif int(b)*int(b) - 4*int(a)*int(c) > 0:
        if int(c) == 0:
            tmsg.showinfo("x1=", "0")
            tmsg.showinfo("x2=", solve_x(int(a),int(b),int(c))[1])
```
```bash
    elif int(b)*int(b) - 4*int(a)*int(c) == 0:
        if int(b) == 0:
            if int(c) == 0:
                tmsg.showinfo("x=", "0")
```
## ③ウィンドウの表示について
引用元ではターミナルに計算結果を表示していたが、より使いやすくするため、「いちばんやさしいPython入門教室」を参考に、ウィンドウを作りそこに表示させた。
```bash
#ボタンがクリックされたときの処理
def ButtonClick():
    a = editboxa.get()
    b = editboxb.get()
    c = editboxc.get()

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
```
