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
