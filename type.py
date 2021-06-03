#type関数は引数で指定したオブジェクトのクラスを返す。

class Sample ():
    pass

s = Sample()
s_type = type(s)
print(s_type)

class Sample1():
    """ 適当なクラス """
    pass
 
 
class Sample2(Sample1):
    """ Sample1を親とするクラス """
    pass
 
 
obj1 = Sample1() # Sample1型のオブジェクトを生成する
obj2 = Sample2() # Sample2型のオブジェクトを生成する
 
# Typeを使用した場合、Sample2型はSample1型とはみなされない
print(type(obj1) == Sample1) # True
print(type(obj1) == Sample2) # False
print(type(obj2) == Sample1) # False
print(type(obj2) == Sample2) # True 
 
# isinstanceを使用した場合、Sample2型はSample1型とみなされる
print(isinstance(obj1, Sample1)) # True
print(isinstance(obj1, Sample2)) # False
print(isinstance(obj2, Sample1)) # True
print(isinstance(obj2, Sample2)) # True