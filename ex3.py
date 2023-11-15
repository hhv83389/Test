import zipfile  # zipfileモジュール

InputZipFile = "sample.zip"  # 入力ファイル

# 変数の初期化
sum = 0  # 合計

# ファイルの読み込み + 合計の計算
# zipファイルの読み込み
with zipfile.ZipFile(InputZipFile, "r") as zip_file:
    InputFiles = zip_file.namelist()  # zipファイル内のファイルの配列
    for InputFile in InputFiles:
        print(InputFile)
        if InputFile.startswith("sample/kitamura_") and InputFile.endswith(
            "_kgu.txt"
        ):  # 「_kgu.txt」をファイル名の最後に持つファイル
            file_number = int(InputFile.split("_")[1])  # ファイルの数値のみを抽出
            if file_number % 2 == 1:  # 奇数名のみ
                # print(file_number)
                # txtファイルの読み込み
                with zip_file.open(InputFile, "r") as f:
                    number = f.read()  # ファイル内の数値
                    sum += int(number)

# 出力
print(sum)
