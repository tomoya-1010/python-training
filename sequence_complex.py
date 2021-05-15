"""
x in s	シーケンスsに要素xが含まれている場合にTrueを返す
x not in s	シーケンスsに要素xが含まれていない場合にTrueを返す
s + t	2つのシーケンスsとtを結合
s * n または n * s	シーケンスs同士をn回結合
s[i]	0始まりのインデックスを指定してシーケンスsのi番目の要素を取得
s[i:j]	シーケンスsのi番目からj番目までのスライスを返す
s[i:j:k]	シーケンスsのi番目からj番目までのk毎のスライスを返す
len(s)	シーケンスsの長さ(=要素数)を返す
min(s)	シーケンスsの最小の要素を返す
max(s)	シーケンスsの最大の要素を返す
s.index(x)	シーケンスsの中で要素xが最初に出現するインデックスを返す
s.count(x)	シーケンスsの中で要素xが出現する回数を返す
"""

ls = [1,1,1,3,1,1,1]
k1 = ls.count(1)
k2 = ls.index(3)
print (k1)
print (k2)


list_data = ['a', 'b', 'c', 'd']
 
# 含まれているかどうかを判定する.包含判定
b1 = ' a ' in list_data # 文字列'a'がリストに含まれているかどうかを判定
print(b1) # True
 
b2 = 'x' in list_data # 文字列'x'がリストに含まれているかどうかを判定
print(b2) # False 
 
# 含まれていないかどうかを判定する
b3 = 'a' not in list_data # 文字列'a'がリストに含まれていないかどうかを判定
print(b3) # False 
 
b4 = 'x' not in list_data # 文字列'x'がリストに含まれていないかどうかを判定
print(b4) # True 


#スライス文
text = "ABCDEFG"
 
# 0番目から2番目の手前まで 
print(text[0:2]) # AB
 
# 開始インデックスの省略
print(text[:2]) # AB
 
# 2番目から最後まで
print(text[2:7]) # CDEFG
 
# 最後を省略 
print(text[2:]) # CDEFG
 
# 1つとばしで
print(text[0:7:2]) # ACEG


#要素数確認

# リストの場合
l = [1, 2, 3]
print(len(l)) # 3
 
# タプルの場合
t = ('a', 'b', 'c', 'd')
print(len(t)) # 4 
 
# 文字列の場合
text = "abcdefg"
print(len(text)) # 7
