# zipfile, jsonモジュール
import zipfile
import json

# matplotlibモジュール
import matplotlib.pyplot as plt

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

# 散布図の作成
plt.figure()
plt.xlim(0, 2000)  # x軸
plt.ylim(1500, 0)  # y軸

for i in range(2):
    # 関節
    # 配列には3つおきにX,Y,信頼度が格納されている。
    X1 = data["people"][i]["pose_keypoints_2d"][2 * 3]
    Y1 = data["people"][i]["pose_keypoints_2d"][2 * 3 + 1]
    X2 = data["people"][i]["pose_keypoints_2d"][5 * 3]
    Y2 = data["people"][i]["pose_keypoints_2d"][5 * 3 + 1]
    # 各関節の座標をplot
    plt.scatter(X1, Y1, c="black")
    plt.scatter(X2, Y2, c="black")

# 表示
plt.show()
