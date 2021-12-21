# Дан номер года. Требуется определить количество дней в этом году, учитывая,
# что обычный год насчитывает 365 дней, а високосный –— 366 дней.#
# Високосным считается год, делящийся на 4, но не делящийся на 100,
# либо делящиеся на 400 (например, годы 700, 1400 и 1800 не являются високосными, а 1600 и 2000 –— являются).
# Формат входных данных: Вводится неотрицательное целое число— номер года.
# Формат выходных данных: Выведите количество дней в данном году.

year = int(input("Год: "))

# TODO: your code here
month = int(input("Введите номер месяца года : "))

if 1 <= month <= 2 or month == 12:
    print("зима")
elif 3 <= month <= 5:
    print("весна")
elif 6 <= month <= 8:
    print("лето")
else:
    print("осень")
