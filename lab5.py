import math
import time
import matplotlib.pyplot as plt

# Начальные параметры
n = -1
one = -1
k = -1
timer = []
timer_rec = []
ans = 1
step = -1


# Функция для вычисления рекурсивного F(n)
def rec_f(x):
    global one
    if x == 1:
        return 1  # F(1) = 1
    else:
        one *= -1
        return one * ((3 * rec_f(x - 1)) - (2 * rec_g(x - 1)))


# Функция для вычисления рекурсивного G(n)
def rec_g(x):
    if x == 1:
        return 1  # G(1) = 1
    else:
        return rec_f(x - 1)  # G(n) = F(n-1)


# Функция для вычисления итеративного факториала
def iter_factor(n, fact_iter):
    for i in range(n, n + 1):  # Итерируем только один раз, используя предыдущее значение
        fact_iter[1] = fact_iter[0] * i
        fact_iter[0], fact_iter[1] = fact_iter[1], fact_iter[-1]
    return fact_iter[1]


# Итеративная версия функции F(n)
def it_f(n, fact_iter):
    global one
    if n == 1:
        return 1  # F(1) = 1
    for i in range(n, n + 1):
        one *= -1
        cata_g[1] = iter_factor(i - 1, fact_iter) + (2 * cata_g[0])
        cata_f[-1] = (one * ((3 * cata_f[1]) - (2 * cata_g[1])))
        cata_f[0], cata_f[1] = cata_f[1], cata_f[2]
        cata_g[0], cata_g[1] = cata_g[1], cata_g[2]
    return cata_f[-1]


# Ввод числа n и шага графика
while n < 1:
    print("Введите натуральное число от 1: ")
    n = int(input())
while step < 1:
    step = int(input("Введите шаг графика от 1: "))
graf = list(range(1, n + 1, step))

# Выбор режима работы программы (0 - рекурсия, 1 - итерация, 2 - оба)
while k not in [0, 1, 2]:
    print("Выберите режим работы: 0 - рекурсия, 1 - итерация, 2 - оба")
    k = int(input())

# Предупреждение о времени выполнения для больших значений n
if (n >= 33 and (k == 0 or k == 2)) or (n >= 5000 and (k == 1 or k == 2)):
    print("Работа программы может занять много времени. Вы хотите продолжить? (1 = да, 0 = нет)")
    ans = int(input())
    while ans not in [0, 1]:
        print("Некорректный ввод. Вы хотите продолжить? (1 = да, 0 = нет)")
        ans = int(input())

# Инициализация списков для факториалов и других переменных
fact_iter = [1] * 3
fact = [1] * 3
cata_f = [2] * 3
cata_g = [2] * 3

# Режим работы рекурсии
if k == 0 and ans == 1:
    for i in graf:
        start = time.time()
        res = rec_f(i)
        end = time.time()
        timer.append(end - start)
        print(f"n = {i} | Результат рекурсии: {res} | Время выполнения: {end - start} сек")

    # Построение графика для рекурсивной функции
    plt.plot(graf, timer, label='Рекурсия')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (сек)')
    plt.legend(loc=2)
    plt.show()

# Режим работы итерации
if k == 1 and ans == 1:
    for i in graf:
        start = time.time()
        result = it_f(i, fact_iter)
        end = time.time()
        timer.append(end - start)
        print(f"n = {i} | Результат итерации: {result} | Время выполнения: {end - start} сек")

    # Построение графика для итерационной функции
    plt.plot(graf, timer, label='Итерация')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (сек)')
    plt.legend(loc=2)
    plt.show()

# Режим работы для обоих методов
if k == 2 and ans == 1:
    for i in graf:
        start = time.time()
        result = it_f(i, fact_iter)
        end = time.time()
        timer.append(end - start)

        start_rec = time.time()
        res = rec_f(i)
        end_rec = time.time()
        timer_rec.append(end_rec - start_rec)

        print(
            f"n = {i} | Результат рекурсии: {res} | Результат итерации: {result} | Время рекурсии: {end_rec - start_rec} сек | Время итерации: {end - start} сек")

    # Построение графиков для обоих методов
    plt.plot(graf, timer, label='Итерация')
    plt.plot(graf, timer_rec, label='Рекурсия')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (сек)')
    plt.legend(loc=2)
    plt.show()
