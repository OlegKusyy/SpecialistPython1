# Дано целое число.
# Если оно делится на 3 без остатка - вывести "Foo",
# если делится на 5 - вывести "Bar",
# а если делится на 3 и на 5 - вывести "Foobar".
# Для всех остальных случаев не выводить ничего.

# TODO: your code here

digit = int(input("Введите целое число : "))

if digit % 5 == 0 and digit % 3 == 0:
    print("Foobar")
elif digit % 3 == 0:
    print("Foo")
else:
    print("Bar")
