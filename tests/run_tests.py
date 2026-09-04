from src.test_loader import TestLoader
from src.test_runner import TestRunner
from src.test_suite import TestSuite

from tests.test_test_case import TestCaseTest
from tests.test_test_suite import TestSuiteTest
from tests.test_test_loader import TestLoaderTest


loader = TestLoader()

suite = TestSuite()

suite.add_test(loader.make_suite(TestCaseTest))
suite.add_test(loader.make_suite(TestSuiteTest))
suite.add_test(loader.make_suite(TestLoaderTest))


runner = TestRunner()
runner.run(suite)