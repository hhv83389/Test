# zipfile, jsonモジュール
import zipfile
import json

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

# 2人の鼻と首の座標の表示
# 人
for i in range(2):
    print(i + 1, "人目：")

    # 鼻 or 首
    for j in range(2):
        if j == 0:
            print("鼻")
        else:
            print("首")

        # 座標と信頼度
        X = data["people"][i]["pose_keypoints_2d"][j * 3]
        Y = data["people"][i]["pose_keypoints_2d"][j * 3 + 1]
        S = data["people"][i]["pose_keypoints_2d"][j * 3 + 2]

        # 出力
        print("X =", X)
        print("Y =", Y)
        print("S =", S)
