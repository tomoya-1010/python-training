"""
イミュータブルとは、後から値を変更できないオブジェクトのことである。
イミュータブルなオブジェクトには、以下種類がある。
・bool
・数値
・文字列
・タプル
・range
"""

#id関数 指定したオブジェクトに固有の番号を取得する

num = 100
tex = 'aaa'
dic = {'key' : 200}

print (id(num))
print (id(tex))
print (id(dic))
print (id(num))


#example 文字列型の同一性を確認できる。別のオブジェクトが生成されたことを確認できる。
text1 = "aaa"
text2 = text1
text3 = text1 + 'bbb'
 
print(id(text1))
print(id(text2)) # text1を参照しているためtext1と同じID
print(id(text3)) # text1とはIDが異なる
 
text1 = "bbb"
print(id(text1)) # もともとのIDとは異なる

