#数値型の変数

num = 5
print (num)

"""
int型の変数・・・integer、つまり整数を表す
桁数の制限がない。
"""
bin_val = 0b0101
print (bin_val)

oct_val = 0o165
print (oct_val)

hex_val = 0xfaa
print (hex_val)


"""
float型
精度はマシンに依存するが、基本的に53bit
"""
x = 0.0012
print (x)

y = 1.2e-10
print(y)

"""
complex型・・・複素数を表す。
実数部分と虚数部分はともにfloat型。
"""
# 複素数を定義
c1 = 2 + 3j
print (c1)
c2 = complex(5, 6)
print (c2)
# 実部と虚部を出力
print (c1.real)
print (c2.imag)

#足し算結果を変数に代入する
x = 10
y = 20
z1 = x + y
print (z1)
#変数に演算結果を直接代入する
z2 = 10 - 20
print (z2)
#掛け算結果を表示する
print (10 * 20)
#割り算の結果を変数に代入する
z3 = x / y
print (z3)


int (2.4444)

# 四則演算
x = 16
y = 3
val = x + y
print(val) # 19
 
val = x - y
print(val) # 13
 
val = x * y
print(val) # 48
 
val = x / y
print(val) # 5.333333333333333
 
val = x // y
print(val) # 5
val = x % y
print(val) # 1
 
val = int(x / y)
print(val) # 5
 
val = float(x)
print(val) # 16.0
 
# 複素数
val = 3 + 5j
print(val.conjugate()) # (3-5j)
 
# 乗数
val = pow(2, 3)
print(val) # 8
 
val = 2 ** 3
print(val) # 8





