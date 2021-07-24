# 処理 for 変数 リスト if リスト要素に対する条件

"リスト内包表記の基本例"

data_list = [5,3,7,4,10,9,6]
new_list = []
for num in data_list:
    new_num = num * 2 
    new_list.append (new_num)
print (new_list) # [5,3,7,4,10,9,6]

"リスト内包表記"
data_list = [5, 3, 7, 4, 10, 9, 6]
new_list = [num * 2 for num in data_list]
print(new_list) # [10, 6, 14, 8, 20, 18, 12]


#ある数値のリストが与えられていたとします。
#このリストに対し、
# ①各要素に対し、②偶数番目の要素を抜き出し、③2倍した結果」
# のリストを新たに作成することを考えてみます。

"リスト内包表記を使わない場合"
data_list = [5,3,4,7,10,9,6,596]
new_list = []
for num in data_list:
    if num % 2 == 0 :
        new_num = num * 2
        new_list.append(new_num)
print (new_list)

"リスト内包表記"
data_list = [5,3,4,7,9,10,6]
new_list = [num * 2 for num in data_list if num % 2 == 0 ]


