import random
from typing import List

# Функция проверки простоты числа
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


# Функция генерации списка простых чисел
def primes(count: int) -> List[int]:
    primes_list = []
    num = 2
    while len(primes_list) < count:
        if is_prime(num):
            primes_list.append(num)
        num += 1
    return primes_list

# Функция расчёта контрольной суммы
def checksum(numbers: List[int]) -> int:
    chk_sum = 0
    for number in numbers:
        chk_sum += number
        chk_sum *= 113
        chk_sum %= 10_000_007
    return chk_sum

# Функция выполнения всех шагов
def pipeline() -> int:
    # 1. Генерация списка из 1000 простых чисел
    prime_numbers = primes(1000)

    # 2. Перемешивание списка с seed 100s
    random.seed(100)
    random.shuffle(prime_numbers)

    # 3. Вычисление контрольной суммы
    result = checksum(prime_numbers)

    return result


# Основной блок программы
if __name__ == "__main__":

    print(pipeline())
