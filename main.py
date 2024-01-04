# Задача на генераторы:
# Напишите генератор, который будет возвращать все четные числа в заданном диапазоне.
left, right = map(int, input().split())
print(list(i for i in range(left, right + 1) if i % 2 == 0))

# Задача на итераторы:
# Создайте итератор, который будет возвращать элементы последовательности Фибоначчи до определенного значения.
# Итератор должен останавливаться, когда очередное число превышает заданное значение.
class Fibonacci:
    def __init__(self, max_value):
        self.max_value = max_value
        self.first, self.second = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        next_value = self.first
        if next_value > self.max_value:
            raise StopIteration
        self.first, self.second = self.second, self.first + self.second
        return next_value

fibonacci_iter = Fibonacci(10)

# Задача на генераторы:
# Напишите генератор, который будет возвращать все простые числа в заданном диапазоне.
def gen_easy(num1, num2):
    for i in range(num1, num2 + 1):
        k = 0
        for j in range(2, i // 2 + 1):
            if (j % j == 0):
                k = k + 1
        if (k <= 0):
            print(f"{i} - простое число")
            yield i
print(list(gen_easy(1, 5)))

# Задача на итераторы:
# Создайте итератор, который будет возвращать элементы из двумерного списка построчно.
# Например, для списка [[1, 2], [3, 4], [5, 6]] итератор должен возвращать последовательность [1, 2, 3, 4, 5, 6].
class matrix_iterator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row_index = 0
        self.col_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.row_index >= len(self.matrix):
            raise StopIteration

        if self.col_index >= len(self.matrix[self.row_index]):
            self.row_index += 1
            self.col_index = 0
            return self.__next__()

        value = self.matrix[self.row_index][self.col_index]
        self.col_index += 1

        return value


matrix = [[1, 2], [3, 4], [5, 6]]
otvet = [element for element in matrix_iterator(matrix)]
print(otvet)

# Задача на генераторы:
# Напишите генератор, который будет возвращать все подстроки заданной строки.
# Например, для строки "hello", генератор должен возвращать последовательность "h", "he", "hel", "hell", "hello", "e", "el", "ell", "ello", "l", "ll", "llo", "l", "lo", "o".
def substrings_generator(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 1, length + 1):
            yield s[start:end]


for substring in substrings_generator("hello"):
    print(substring)

# Задача на итераторы:
# Создайте итератор, который будет возвращать элементы списка в обратном порядке.
class ReverseIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.sequence[self.index]


elements = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(elements)
for element in reverse_iterator:
    print(element)

# Задача на генераторы:
# Напишите генератор, который будет возвращать все перестановки заданного списка элементов. можно использовать функцию itertools.permutations
import itertools

def gen_perestanovka(elements):
    for comb in itertools.permutations(elements):
        yield comb

elements = [7, 8, 8]
for perm in gen_perestanovka(elements):
    print(perm)









# Многопоточка
# Вычисление факториала: Рассчитайте факториалы для набора чисел с использованием нескольких потоков или процессов.
import threading

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def thread_function(number):
    result = factorial(number)
    print(f"Факториал {number} = {result}")

def main(numbers):
    threads = []
    for number in numbers:
        thread = threading.Thread(target=thread_function, args=(number,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


numbers = [5, 7, 3]
main(numbers)

# Поиск простых чисел: Найдите все простые числа в определенном диапазоне, используя параллельные потоки или процессы для ускорения процесса.
import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end, primes):
    for number in range(start, end):
        if is_prime(number):
            primes.append(number)

def main(start, end, num_threads):
    threads = []
    primes = []
    range_per_thread = (end - start) // num_threads

    for i in range(num_threads):
        thread_start = start + i * range_per_thread
        thread_end = start + (i + 1) * range_per_thread if i != num_threads - 1 else end
        thread = threading.Thread(target=find_primes_in_range, args=(thread_start, thread_end, primes))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sorted(primes)


start = 1
end = 8
num_threads = 4
primes = main(start, end, num_threads)
print(primes)

# Скачивание файлов: Скачайте несколько файлов из интернета параллельно, чтобы уменьшить время загрузки.
#
# Генерация случайных чисел: Генерируйте большое количество случайных чисел параллельно для статистических вычислений.
import threading
import random

def generate_random_numbers(count, result, index):
    result[index] = [random.random() for _ in range(count)]

def parallel_random_number_generator(total_numbers, thread_count):
    numbers_per_thread = total_numbers // thread_count
    results = [None] * thread_count
    threads = []

    for i in range(thread_count):
        thread = threading.Thread(target=generate_random_numbers, args=(numbers_per_thread, results, i))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    all_numbers = [number for sublist in results for number in sublist]
    return all_numbers


total_numbers = 9
thread_count = 9
print(parallel_random_number_generator(total_numbers, thread_count))


# Производители и потребители (Producer-Consumer): Создайте несколько процессов-производителей, которые помещают элементы в общую очередь, и несколько процессов-потребителей, которые извлекают элементы из очереди. Используйте мьютексы или семафоры для синхронизации доступа к общей очереди.
#
# Чтение и запись в общий файл: Несколько процессов должны одновременно читать и записывать данные в общий файл. Для предотвращения конфликтов при доступе к файлу используйте блокировки.
#
# Параллельная сортировка данных: Разделите набор данных на части и отсортируйте каждую часть параллельно. Затем объедините отсортированные части.