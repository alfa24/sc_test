# coding=utf-8
from collections import deque


def sum_numbers(value):
    """ Вычисляет сумму всех чисел в списке """
    return sum(map(int, value))


def is_field_available(x, y, max_sum=25):
    """ Проверяет, что поле доступно для перемещения """
    if x <= 0 or y <= 0:
        return False

    current_sum = sum_numbers(str(x) + str(y))
    if current_sum > max_sum:
        return False

    return True


def calc_available_field(x, y, max_sum=25):
    """ Высчитывает количество доступных полей """
    dots = {}

    # Определяем очередь и помещаем туда стартовое поле
    queue = deque()
    queue.append((x, y))

    # Крайние точки карты
    min_x = x
    min_y = y
    max_x = x
    max_y = y

    # Количество доступных полей
    count = 0

    while len(queue) > 0:
        # Получаем ближайшие координаты
        x, y = queue.pop()
        dot_key = str(x) + '_' + str(y)

        # Если поле уже было обработано, то пропускаем
        if dot_key in dots:
            continue

        # высчитываем крайние точки
        if min_x > x:
            min_x = x
        if min_y > y:
            min_y = y
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y

        # Проверяем доступность поля
        is_available = is_field_available(x, y, max_sum=max_sum)

        # Запоминаем посещенные поля
        dots[dot_key] = {'available': is_available, 'x': x, 'y': y}

        # если недоступно, то следующий шаг
        if not is_available:
            continue

        count += 1

        # добавляем в очередь следующие доступные шаги
        queue.append((x - 1, y))
        queue.append((x + 1, y))
        queue.append((x, y - 1))
        queue.append((x, y + 1))

    return {
        "count": count,
        "dots": dots,
        "map": {'x1': min_x, 'y1': min_y, 'x2': max_x, 'y2': max_y}
    }


if __name__ == '__main__':
    x = int(input("Введите начальную координату X: "))
    y = int(input("Введите начальную координату Y: "))
    max_sum = int(input("Введите максимальную сумму цифр: "))

    result = calc_available_field(x, y, max_sum)

    print "Количество доступных полей для перемещения:", result["count"]
