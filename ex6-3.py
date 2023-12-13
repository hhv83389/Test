# zipfile, jsonモジュール
import zipfile
import json

# tkinterモジュール
import tkinter as tk

InputZipFile = "kabeposter.zip"  # 入力ファイル

# ウィンドウの作成
root = tk.Tk()
root.geometry("1200x800")  # サイズ

# キャンバスの作成
canvas = tk.Canvas(root, width=1200, height=800, bg="white")
canvas.place(x=0, y=0)

r = 5  # 半径
t = 1 / 2  # 倍率

datas = []  # dataリスト

# ファイルの読み込み
# zipファイル
with zipfile.ZipFile(InputZipFile, "r") as zip_file:
    InputFiles = zip_file.namelist()
    for InputFile in InputFiles:
        if InputFile.endswith("_keypoints.json"):  # 0フレームのみ
            # jsonファイル
            with zip_file.open(InputFile, "r") as f:
                data = json.load(f)  # 座標
                datas.append(data)


def draw(frame):
    # すべてのデータを描画すれば終了
    if frame >= len(datas):
        return

    # 前のフレームの削除
    canvas.delete("all")

    # 骨格座標の描画
    for i in range(2):
        for j in range(25):
            # ドットを描く
            X = datas[frame]["people"][i]["pose_keypoints_2d"][j * 3] * t
            Y = datas[frame]["people"][i]["pose_keypoints_2d"][j * 3 + 1] * t
            # X座標が0の場合は何も表示しない。
            if X != 0:
                canvas.create_oval(
                    X - r,
                    Y - r,
                    X + r,
                    Y + r,
                    fill="black",
                    tag="all",
                )

        # 線で結ばれた頂点の集合
        connects = [
            (0, 1),
            (0, 15),
            (0, 16),
            (1, 2),
            (1, 5),
            (1, 8),
            (2, 3),
            (3, 4),
            (5, 6),
            (6, 7),
            (8, 9),
            (8, 12),
            (9, 10),
            (10, 11),
            (11, 22),
            (11, 24),
            (12, 13),
            (13, 14),
            (14, 19),
            (14, 21),
            (15, 17),
            (16, 18),
            (19, 20),
            (22, 23),
        ]

        # 線を描く
        for s, e in connects:
            X1 = datas[frame]["people"][i]["pose_keypoints_2d"][s * 3] * t
            Y1 = datas[frame]["people"][i]["pose_keypoints_2d"][s * 3 + 1] * t
            X2 = datas[frame]["people"][i]["pose_keypoints_2d"][e * 3] * t
            Y2 = datas[frame]["people"][i]["pose_keypoints_2d"][e * 3 + 1] * t

            # X座標が0の場合は何も表示しない。
            if X1 != 0 and X2 != 0:
                canvas.create_line(X1, Y1, X2, Y2, tag="all")

    root.after(50, draw, frame + 1)


# 関数
draw(0)

# ウィンドウの表示
root.mainloop()
