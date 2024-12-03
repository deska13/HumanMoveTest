import logging
from unittest import TestCase, skipIf

from rt_with_exceptions import Runner

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="runner_tests.log",
)

logger = logging.getLogger(__name__)

class RunnerTest(TestCase):
    is_frozen = False

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner = Runner("John", -2)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logger.warning("Неверная скорость для Runner", exc_info=True)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner(False)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logger.info('"test_run" выполнен успешно')
        except:
            logger.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner_1 = Runner("John")
        runner_2 = Runner("Peter")
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    import unittest
    unittest.main()
