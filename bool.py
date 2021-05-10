b1 = True
b2 = False
b3 = True

b4 = b1 or b2
print (b4)
b5 = b1 and b2
print(b5)
b6 = b1 and ( b2 and b3 ) #可読性を意識して括弧をつけるべきである
print(b6)

print(int(b1))
print(int(b2))

# none は Falseと評価される

val = None
if val :
    print('True')
else :
    print ('False')

