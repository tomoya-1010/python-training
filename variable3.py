"""
numbersモジュールの説明
与えら得た変数が数値化どうかで真偽を返す。
int, float, coplexのいづれかを判定する際に、isinstance関数に指定する。

>>> isinstance(1, numbers.Number)
True
>>> isinstance(1.1, numbers.Number)
True
>>> isinstance(-1, numbers.Number)
True
>>> isinstance(5 + 3j, numbers.Number)
True
>>> isinstance(True, numbers.Number)
True
>>> isinstance('text', numbers.Number)
False

"""

"""
math , cmathモジュール
各種関数のモジュール
"""
import math
 
# 指数関数
val = math.exp(2)
print(val) # 7.38905609893065
# 対数関数
val = math.log(5)
print(val) # 1.6094379124341003
# 三角関数
val = math.sin(math.pi / 2)
print(val) # 1.0

"""
decimalモジュール
10進数の浮動小数点に対応している
"""

x = 0.1 * 3
print(x) # 0.30000000000000004
is_equal = (0.1 * 33 == 3.3)
print(is_equal) # False

from decimal import Decimal
x = Decimal('0.1')
print (x)
print (x * 3)

Decimal('0.3')
is_equal = (x * 33 == Decimal ('3.3'))
print (is_equal)


"""
fractionsモジュール
有理数つまり分数をサポートするモジュール
割り算と掛け算を繰り返すと、徐々に誤差が蓄積していく。
素手を軽減してくれる関数、約分とかも自動で行ってくれる。
"""

from fractions import Fraction
 
# 分数の定義
x = Fraction(3, 7)
print(x) # 3/7 
# 約分の確認
y = x * 7
print(y) # 3 
# 小数との演算
z = x + 0.1
print(z) # 0.5285714285714286









