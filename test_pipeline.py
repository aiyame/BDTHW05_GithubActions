import unittest
from pipeline import is_prime, primes, checksum, pipeline

class TestPipeline(unittest.TestCase):

    # Тест функции проверки простоты числа
    def test_is_prime(self):
        # Примеры простых чисел
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(29))

        # Примеры составных чисел
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))

    # Тест функции генерации списка простых чисел
    def test_primes(self):
        # Проверяем длину списка
        prime_numbers = primes(1000)
        self.assertEqual(len(prime_numbers), 1000)

        # Проверяем первые и последние числа
        self.assertTrue(is_prime(prime_numbers[0]))
        self.assertTrue(is_prime(prime_numbers[-1]))

    # Тест функции расчёта контрольной суммы
    def test_checksum(self):
        # Пример с известной контрольной суммой
        self.assertEqual(checksum([1]), 113)
        self.assertEqual(checksum([1, 2, 6, 24]), 6012369)  # Исправлено

    # Тест выполнения всех шагов
    def test_pipeline(self):
        # Проверяем, что pipeline выдаёт правильную контрольную сумму
        self.assertEqual(pipeline(), 7785816)

# Основной блок для запуска тестов
if __name__ == "__main__":
    unittest.main()
