import sys
args = sys.argv
print (args)

# 引数なし　
# 出力　['args.py']
# 引数 hoge
# 出力　['args.py', 'hoge']
# 引数 hoge foo
# 出力　['args.py', 'hoge', 'foo']

"""
tomoyanakayama@Tomoyas-MacBook-Air paiza % python args.py
['args.py']
tomoyanakayama@Tomoyas-MacBook-Air paiza % python args.py hoge
['args.py', 'hoge']
tomoyanakayama@Tomoyas-MacBook-Air paiza % python args.py hoge foo
['args.py', 'hoge', 'foo']
tomoyanakayama@Tomoyas-MacBook-Air paiza % 
"""
