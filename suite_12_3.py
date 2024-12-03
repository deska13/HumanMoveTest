
from tests_12_1 import RunnerTest
from tests_12_2 import TournamentTest
from unittest import TestSuite

test_cases = TestSuite()
test_cases.addTest(RunnerTest('test_walk'))
test_cases.addTest(RunnerTest('test_run'))
test_cases.addTest(RunnerTest('test_challenge'))
test_cases.addTest(TournamentTest('test_first'))
test_cases.addTest(TournamentTest('test_second'))
test_cases.addTest(TournamentTest('test_third'))
