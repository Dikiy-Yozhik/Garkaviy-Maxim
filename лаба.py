print("Hello world")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(a, "-", b, "=", a-b)
print(a, "+", b, "=", a+b)
print(a, "/", b, "=", a/b)
print(a, "*", b, "=", a*b)
c = int(input("А введи еще число "))
for i in range(c):
    print("Goodbye")
    if i>0:
        break
