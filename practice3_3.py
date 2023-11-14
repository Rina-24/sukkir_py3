# (1)変数isErrorがFalseかつ変数nが100未満の場合のみ、画面表示を行う
isError = False
n = 1
if isError == False and n < 100:
    print("正解です")

# (2)入力された数値について、偶数か奇数かを判定してその結果を表示する。
num = int(input("数字を入力してください"))
if num % 2 == 0:
    print("入力された数字は偶数です。")
elif num % 2 == 1:
    print("入力された数字は奇数です。")

else:
    print("整数を入力してください。")


# (3)入力された次の文字列に応じて、挨拶を表示する
greeting = input("挨拶をしてください。＞＞")
if greeting == "こんにちは" :
    print("ようこそ")
elif greeting == "景気は？":
    print("ぼちぼちです")
elif greeting == "さようなら":
    print("お元気で！")
else:
    print("どうしました？")

