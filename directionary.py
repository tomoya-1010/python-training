"""
directionary 
キーに対して値が設定された表のようなデータ構造のことであり、ハッシュと呼ばれることもある。
"""

#directionary型の初期化

dic = {'key1' : 110, 'key2' : 270, 'key3' : 350 } 
print(dic)
print (dic['key1'])
print (dic.get ('key1') ) # 上と同じ。getコマンドを使用
print (dic['key2'])


print(dic['key3'])
dic['key3'] = 35 #key3の上書き
print(dic['key3'])


#　組み込みのdict()
dic = dict()
dic['key1'] = 110
dic['key2'] = 270
dic['key3'] = 350

d1 = {'key1' : 110, 'key2' : 270, 'key3' : 350}
d2 = dict(d1)

d3 = {'k1' : 110, 'k2' : 270, 'k3' : 350, 'k4' : 985, 'k5' : 1092, 
      'k6' : 12428, 'k7' : 9021391}
d4 = dict(d3)



print (d2)

#dictionary の要素数
print (len(d2))
print (len(d4))

