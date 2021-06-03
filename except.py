'''
Pythonの例外処理は、例外が発生する可能性がある箇所をtryブロックに囲んで、
exceptで例外を補足する。
'''

x = 1000
y = 0

try :
    z = x / y
    print (z)
except ZeroDivisionError :
    print ('割り算の結果に0が指定されました')

except ZeroDivisionError as e :
    print ('割り算の結果に0が指定されました')
    print (type(e), str(e))


    param = {'x' : 1000, 'z' : 0}
try:
    x = param['x']
    y = param['y']
    z = x / y
    print(z)
 
except KeyError as e: # 辞書に存在しない場合の例外を補足
    print('処理に必要なデータが存在しません')
 
except ZeroDivisionError as e: # 0除算を補足
    print('除算に0が指定されました')
 
except: # 全ての例外を補足
    print('原因不明のエラーが発生しました')





