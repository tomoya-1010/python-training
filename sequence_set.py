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


#setの集合演算

#union 和集合

s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
s = s1.union(s2) # s1とs2をunionする
print(s) # {'E', 'D', 'C', 'B', 'A'}
print(s1) # {'B', 'A', 'C'} 変更なし
s1.add('F')
s2.remove('C')
s = s1.union(s2)
print(s)

#Intersection(積集合)

s1 = {'A', 'B', 'C', '1', '2A'}
s2 = {'C', 'D', 'E', '2A'}
s = s1.intersection(s2)
print(s) # {'C'}

a1 = {'a','b','c'}
a2 = {'d','e','f','a'}
a3 = {'e', 'f'}
a1.add('k')

b = a1.union(a2)
c = b.intersection(a3)
print(b)
print(c)

#difference (差集合)

s1 = {'A', 'B', 'C'}
s2 = {'C', 'D', 'E'}
 # s1 - s2
s = s1.difference(s2)
print(s) # {'B', 'A'}
 # s2 - s1
s = s2.difference(s1)
print(s) # {'D', 'E'}

#包含判定 issubset

s1 = {'A', 'B'}
s2 = {'A', 'B', 'C'}
t = {'D'}
s1.add('D')
s2.add('D')
s2.remove('A')
s3 = s1.intersection(s2)
print(s3)
print(t)
print(t.issubset(s3))  #tはs3の部分集合であるのでtrue

#含んでいるかどうかを判定　superset

s1 = {'A', 'B', 'C', 'D'}
print(s1)
print(s2)
print(s1.issuperset(s2)) #s2はs1の部分集合、s2はs1に含まれるのでtrue

















