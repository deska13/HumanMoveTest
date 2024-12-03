from suite_12_3 import test_cases
from unittest import TextTestRunner


test = TextTestRunner(verbosity=2)

test.run(test_cases)
