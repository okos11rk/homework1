print("задание 2")
print()
word=(input("введите слово:"))
a=word.count("а")
e=word.count("e")
i=word.count("i")
u=word.count("u")
y=word.count("y")
if a ==0:
    print("a = False")
if e ==0:
    print("e = False")
if i ==0:
    print("i = False")
if u ==0:
    print("u = False")
if y ==0:
    print("y = False")
print(f"Гласных: {a+e+i+u+y}")
print(f"Соглассных:.")