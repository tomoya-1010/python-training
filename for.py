"for文"
"for　ループ内変数　in イテラブルオブジェクト：ループ内しょり"

#listのfor文
datas =  [ 'a', 'b', 'c' ]
for v in datas :
     print (v)

# listの各値が表示される

#for sentence of range

for v in range (1, 5, 2) :
    print (v)

#　一から２飛ばしで５未満まで出力

# for sentence of dictionary

dic = {'key1' : 110, 'key2' :270 , 'key3' : 350 }
for value in dic.values () :
    print (value)


#break

data_list = [1,2,3]
for data in data_list:
     print(data)
     if data > 1:
         break

# for-else

data_list2 =[]
for data in data_list2 :
    print (data)
else:
    print ('ループ処理が終わりました')

l = [0,2,1,10,698421]
for x in l :
    if x < 0:
        print ('I found negative number.')
        break
else:
    print ('I could not find negative number.')

m = [ 100000000 ]
for y in m :
    if y > 1000 :
        print ('you find what you want.')
        break
else : 
    print ('you cannot get what you want.')
    
