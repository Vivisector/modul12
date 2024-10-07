import unittest
import logging
from runner import Runner

# настройка логирования
logging.basicConfig(
    level = logging.INFO,
    filemode= 'w',
    filename='runner_tests.log',
    encoding = 'utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            # Передаем в speed отрицательное значение, чтобы увидеть исключение
            obj = Runner('Usain', -10)
            obj.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            # logging.warning(f'"test_walk": Неверная скорость для Runner: {e}') # без логирования сообщения об ошибке
            logging.warning(f'"test_walk": Неверная скорость для Runner: {e}', exc_info=True) # c сообщением

    def test_run(self):
        try:
            # Передаем некорректный тип для name, чтобы увидеть исключение
            obj = Runner(False, 10)
            obj.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            # logging.warning(f'"test_run": Неверный тип данных для объекта Runner: {e}') # без логирования сообщения об ошибке
            logging.warning(f'"test_run": Неверный тип данных для объекта Runner: {e}', exc_info=True) # с сообщением