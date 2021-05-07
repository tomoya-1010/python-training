print ("sample")

print ('サンプル文字列')
# サンプル文字列

x = 'text'
print (x) 
#文字列textが出力される

y = 'I read'
print (y)
#文字列I readが出力される

print(x, y)

print ('aaa', end ='')
print ('bbb')

print ('aaa', end ='と')
print ('bbb', end ='と')
print ('ccc')
#aaaとbbbとccc　と出力される

x1 = 'text'
x2 = 'mojiretsu'
x3 = 20210507
print ( x1 + ' ' + x2 )
print ( x1 + str(x3) + x2 )

#str関数は任意の変数を文字列化する関数と考えて良い

x1 = '18782'
x2 = '18782'

print ( x1 + ' ' + x2 )
print ( int(x1) + int(x2) )
#int関数は任意の文字列を変数化する関数と考えて良い
