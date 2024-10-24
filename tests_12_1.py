from unittest import TestCase

from runner import Runner


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("John")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("John")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner_1 = Runner("John")
        runner_2 = Runner("Peter")
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)
