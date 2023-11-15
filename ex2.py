import json  # jsonモジュール

InputFile = "catalog.json"  # 入力ファイル

# データの読み込み
with open(InputFile, "r") as f:
    data = json.load(f)  # data配列に読み込み

# 変数の初期化
count = 0  # 個数
max_price = 0  # 最大値
min_price = float("inf")  # 最小値（float("inf")は無限大を表す）

# jacketの個数・最高値・最安値を求める
for i in range(len(data)):
    # jacketのみ
    if data[i]["name"] == "jacket":
        count += 1
        price = data[i]["price"]  # jacketの値段
        # 最高値の更新
        if max_price < price:
            max_price = price
        # 最安値の更新
        if min_price > price:
            min_price = price

# 出力
print("個数 :", count)
print("最高価格 :", max_price)
print("最低価格 :", min_price)
