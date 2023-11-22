import tkinter as tk  # tkinterモジュール

# ウィンドウの作成
root = tk.Tk()
root.title("People")
root.geometry("600x400")  # サイズ

# キャンバスの作成
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.place(x=0, y=0)

# 顔の中心
X = 100  # X座標
Y = 100  # Y座標

r = 20  # 顔の半径
body = 50  # 胴体の長さ
limb = 40  # 腕・足の長さ

dx = 5  # 移動量

canvas.create_oval(X - r, Y - r, X + r, Y + r, tags="a")  # 顔
canvas.create_line(X, Y + r, X, Y + r + body, tags="a")  # 胴
canvas.create_line(X, Y + r + (body / 2), X - limb, Y + r, tags="a")  # 左腕
canvas.create_line(X, Y + r + (body / 2), X + limb, Y + r, tags="a")  # 右腕
canvas.create_line(X, Y + r + body, X - limb, Y + r + body + limb, tags="a")  # 左足
canvas.create_line(X, Y + r + body, X + limb, Y + r + body + limb, tags="a")  # 右足


# 移動関数
def move():
    canvas.move("a", dx, 0)  # "a"の図形をx+=5ずつ移動
    canvas.after(100, move)


# 関数の実行
move()

# ウィンドウの表示
root.mainloop()
