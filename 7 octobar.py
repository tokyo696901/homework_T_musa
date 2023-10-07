def sum_range(start, end):
    # Проверяем, если start больше end, меняем их местами
    if start > end:
        start, end = end, start
    
    # Инициализируем переменную для суммы
    total = 0
    
    # Суммируем числа от start до end
    for num in range(start, end + 1):
        total += num
    
    return total

# Пример использования функции
start = 5
end = 10
result = sum_range(start, end)
print(f"Сумма чисел от {start} до {end} равна {result}")

👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻homework2


import math

def square(side):
    # Вычисляем периметр квадрата
    perimeter = 4 * side
    
    # Вычисляем площадь квадрата
    area = side ** 2
    
    # Вычисляем диагональ квадрата используя теорему Пифагора
    diagonal = math.sqrt(2) * side
    
    # Возвращаем значения в виде кортежа
    return (perimeter, area, diagonal)

# Пример использования функции
side_length = 5
result = square(side_length)
print(f"Периметр: {result[0]}, Площадь: {result[1]}, Диагональ: {result[2]}")

👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻homework3

def bank(a, years):
    # Инициализируем начальную сумму вклада
    balance = a
    
    # Вычисляем и прибавляем проценты каждый год
    for _ in range(years):
        balance += balance * 0.10  # Увеличение суммы на 10% каждый год
    
    return balance

# Пример использования функции
initial_deposit = 1000  # Начальный вклад в рублях
investment_period = 5  # Количество лет
result = bank(initial_deposit, investment_period)
print(f"Через {investment_period} лет на счету будет {result:.2f} рублей")

👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻homework3

def bank(a, years):
    # Инициализируем начальную сумму вклада
    balance = a
    
    # Вычисляем и прибавляем проценты каждый год
    for _ in range(years):
        balance += balance * 0.10  # Увеличение суммы на 10% каждый год
    
    return balance

# Пример использования функции
initial_deposit = 1000  # Начальный вклад в рублях
investment_period = 5  # Количество лет
result = bank(initial_deposit, investment_period)
print(f"Через {investment_period} лет на счету будет {result:.2f} рублей")

👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻homework4

def encode_to_unicode(input_string):
    # Используем метод encode для кодирования строки в Unicode
    unicode_string = input_string.encode('unicode_escape').decode('utf-8')
    return unicode_string

# Пример использования функции
input_str = "Пример строки для кодирования"
encoded_str = encode_to_unicode(input_str)
print(encoded_str)

👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻homework5


check_even_odd = lambda x: "Четное" if x % 2 == 0 else "Нечетное"

# Пример использования анонимной функции
number = 7
result = check_even_odd(number)
print(f"{number} - {result}")

👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻homework6


# Функция логирования
def log(func):
    def wrapper(*args, **kwargs):
        # Получаем имя функции
        function_name = func.__name__
        # Выводим введенные значения и имя функции в консоль
        print(f"Вызвана функция {function_name} с аргументами {args}")
        # Вызываем функцию и сохраняем ее результат
        result = func(*args, **kwargs)
        # Выводим результат в консоль
        print(f"Результат функции {function_name}: {result}")
        return result
    return wrapper

# Декорируем функции калькулятора с функцией логирования
@log
def sum_numbers(*args):
    return sum(args)

@log
def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result

@log
def divide_numbers(*args):
    if len(args) < 2:
        return "Ошибка: необходимо минимум два аргумента для деления"
    result = args[0]
    for i in range(1, len(args)):
        if args[i] == 0:
            return "Ошибка: деление на ноль невозможно"
        result /= args[i]
    return result

@log
def subtract_numbers(*args):
    if len(args) < 2:
        return "Ошибка: необходимо минимум два аргумента для вычитания"
    result = args[0]
    for i in range(1, len(args)):
        result -= args[i]
    return result

# Пример использования функций калькулятора
print(sum_numbers(1, 2, 3))
print(multiply_numbers(2, 3, 4))
print(divide_numbers(10, 2))
print(subtract_numbers(10, 5, 3))
