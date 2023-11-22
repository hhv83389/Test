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

canvas.create_oval(X - r, Y - r, X + r, Y + r)  # 顔
canvas.create_line(X, Y + r, X, Y + r + body)  # 胴
canvas.create_line(X, Y + r + (body / 2), X - limb, Y + r)  # 左腕
canvas.create_line(X, Y + r + (body / 2), X + limb, Y + r)  # 右腕
canvas.create_line(X, Y + r + body, X - limb, Y + r + body + limb)  # 左足
canvas.create_line(X, Y + r + body, X + limb, Y + r + body + limb)  # 右足

# ウィンドウの表示
root.mainloop()
