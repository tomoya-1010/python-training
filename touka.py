"Pythonのオブジェクトが等価かどうかを評価する場合、==演算子を使用します。"

x = 3
y = 3
z = 7
k = x*y*z
l = y*x*z
 
b1 = (x == y)
b2 = (x == z)
b3 = (k == l)


print(b1) # True
print(b2) # False
print(b3)