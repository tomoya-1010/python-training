"""
tuple型と言うシーケンスは、listとよく似ているが、
一度初期化したタプルの要素は変更できないと言う点が最も異なっている。
この性質のことをイミュータブルと言う。
"""

t1 = ()
print (t1)

# 要素がないタプル
t1 = ()
print(t1) # ()

# 要素がひとつの場合はカンマをつけないと、単一の値とみなされてしまう。
t2 = (1)
print(t2) # 1（単一の値扱い）
 
# 要素がひとつの場合はカンマをつける
t2 = (1,)
print(t2) # (1,)
 
# カンマ区切りで複数の要素をセットする
t3 = ('a', 'b', 'c')
print(t3) # ('a', 'b', 'c')

t = (1, 2, 3,)
print(t) # (1, 2, 3)

# リストを初期化
l = [1, 2, 3]
# リストからタプルを初期化（リストをタプルに変換）
t = tuple(l)
print(t)  # (1, 2, 3)

"""
listと比較すると、更新系の処理ができないため不便に感じるかもしれませんが、
あるリストの途中値を途中で変えさせないで安全に保持したいとき等に活躍します。
また、listと比較して（少しだけ）処理する際のスピードが速いです。
また、イミュータブルなのでハッシュ化することが可能。
"""