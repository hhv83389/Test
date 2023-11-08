import numpy as np  # 配列モジュール


# 整数判定する（整数のときのみTrueを返す）関数
def intjudge(string):
    if string.isdigit() == True:  # 正の整数
        return True
    elif (string.startswith("-") and string[1:].isdigit()) == True:  # 負の整数
        return True
    else:
        return False


# 整数の配列
Nlist = np.empty((0,), dtype=int)

# データの読み込み
InputFile = "data.txt"  # 入力ファイル
with open(InputFile, "r") as f:
    for line in f.readlines():
        line = line.strip()  # 改行文字の削除
        if intjudge(line) == True:  # 整数判定
            Nlist = np.append(Nlist, int(line))  # 配列に挿入

# 配列の出力
# print(Nlist)

# 和を求める
sum = 0  # 初期化
for i in range(len(Nlist)):
    sum += Nlist[i]

# 和の出力
print(sum)
