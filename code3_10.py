print("すべての質問にyまたはnで答えてください。")
has_money = input("お金に余裕はありますか？")
if has_money == "y":
    is_hungry = input("お腹がすごく空いていますか？＞＞")
    nomitai_kibunka = input("ビールを飲みたいですか？＞＞")
    if is_hungry == "y" and nomitai_kibunka == "y":
        print("焼肉はいかがですか？")
    elif is_hungry == "y":
        print("カレーはいかがですか？")
    elif nomitai_kibunka == "y":
        print("焼き鳥はいかがですか？")
    else:
        print("パスタはいかがですか？")

    is_snack = input("夜食は必要ですか？＞＞")
    if is_snack == "y":
        print("コンビニのチキンはいかがですか？")
    else:
        print("家で食べましょう")