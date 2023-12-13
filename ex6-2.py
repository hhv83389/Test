# zipfile, jsonモジュール
import zipfile
import json

# tkinterモジュール
import tkinter as tk

InputZipFile = "kabeposter.zip"  # 入力ファイル

# ファイルの読み込み
# zipファイル
with zipfile.ZipFile(InputZipFile, "r") as zip_file:
    InputFiles = zip_file.namelist()
    for InputFile in InputFiles:
        if InputFile.endswith("00_keypoints.json"):  # 0フレームのみ
            # jsonファイル
            with zip_file.open(InputFile, "r") as f:
                data = json.load(f)

# ウィンドウの作成
root = tk.Tk()
root.geometry("1200x800")  # サイズ

# キャンバスの作成
canvas = tk.Canvas(root, width=1200, height=800, bg="white")
canvas.place(x=0, y=0)

r = 5  # 半径
t = 1 / 2  # 倍率

# 2人の肩のラインの描画
# 人
for i in range(2):
    # 関節
    X1 = data["people"][i]["pose_keypoints_2d"][2 * 3] * t
    Y1 = data["people"][i]["pose_keypoints_2d"][2 * 3 + 1] * t
    X2 = data["people"][i]["pose_keypoints_2d"][5 * 3] * t
    Y2 = data["people"][i]["pose_keypoints_2d"][5 * 3 + 1] * t

    # 点の描画
    canvas.create_oval(X1 - r, Y1 - r, X1 + r, Y1 + r, fill="black")
    canvas.create_oval(X2 - r, Y2 - r, X2 + r, Y2 + r, fill="black")
    canvas.create_line(X1, Y1, X2, Y2)


# ウィンドウの表示
root.mainloop()
