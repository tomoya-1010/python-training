"""
pythonには集合を表すset型がある。
listやtupleは同じオブジェクトを重複して追加することが可能で、
追加した際の順序を保持することが出来る。
一方、setは順序を保持せず、ユニークな値を持つ。
つまり、setに格納可能なオブジェクトはユニークなものに限られる。
つまりイミュータブルなものにかぎる。listは格納不可、tupleは格納可能。
"""

# setの初期化
s = {'A', 'B', 'C'}
print(s) # {'C', 'B', 'A'}
 
# 初期化時に重複があっても・・・
s = {'A', 'B', 'C', 'A'}
print(s) # {'C', 'B', 'A'}

s = {'A', (1, 2, 3)}
print(s)

l = ['a', 'b', 'c', 'd']
s = set (l)
print (s)

# setのイテレーション

data_set = {'a', 'b', 'c'}
for s in data_set : # for 変数 in set型オブジェクト: 処理
    print (s)

#setの要素追加
s = {1, 2, 3}
s.add(4)
s.add(5)
s.remove(2) #要素削除、指定した要素が無いとエラーになる
s.discard(100) #要素削除、指定した要素なくてもエラーにならない
print(s) # {1, 3, 4, 5}

