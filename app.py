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

# Основной блок программы
if __name__ == "__main__":

    print(pipeline())
