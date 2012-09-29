import fibonacci
import unittest

class TestFibonacciQueue(unittest.TestCase):

    def runTest(self):
        self.assertEqual(fibonacci.fibonacci_queue(0), 0)
        self.assertEqual(fibonacci.fibonacci_queue(1), 1)
        self.assertEqual(fibonacci.fibonacci_queue(2), 1)
        self.assertEqual(fibonacci.fibonacci_queue(8), 21)
        self.assertEqual(fibonacci.fibonacci_queue(-1), 1)
        self.assertEqual(fibonacci.fibonacci_queue(-2), -1)
        self.assertEqual(fibonacci.fibonacci_queue(-8), -21)

class TestFibonacciRecursive(unittest.TestCase):

    def runTest(self):
        self.assertEqual(fibonacci.fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci.fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci.fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci.fibonacci_recursive(8), 21)
        self.assertEqual(fibonacci.fibonacci_recursive(-1), 1)
        self.assertEqual(fibonacci.fibonacci_recursive(-2), -1)
        self.assertEqual(fibonacci.fibonacci_recursive(-8), -21)

class TestLucasQueue(unittest.TestCase):

    def runTest(self):
        self.assertEqual(fibonacci.lucas_queue(0), 2)
        self.assertEqual(fibonacci.lucas_queue(1), 1)
        self.assertEqual(fibonacci.lucas_queue(2), 3)
        self.assertEqual(fibonacci.lucas_queue(8), 47)
        self.assertEqual(fibonacci.lucas_queue(-1), -1)
        self.assertEqual(fibonacci.lucas_queue(-2), 3)
        self.assertEqual(fibonacci.lucas_queue(-8), 47)

class TestLucasRecursive(unittest.TestCase):

    def runTest(self):
        self.assertEqual(fibonacci.lucas_recursive(0), 2)
        self.assertEqual(fibonacci.lucas_recursive(1), 1)
        self.assertEqual(fibonacci.lucas_recursive(2), 3)
        self.assertEqual(fibonacci.lucas_recursive(8), 47)
        self.assertEqual(fibonacci.lucas_recursive(-1), -1)
        self.assertEqual(fibonacci.lucas_recursive(-2), 3)
        self.assertEqual(fibonacci.lucas_recursive(-8), 47)

        
if __name__ == '__main__':
    suite_fibonacci_queue = unittest.TestLoader().loadTestsFromTestCase(TestFibonacciQueue)
    suite_fibonacci_recursive = unittest.TestLoader().loadTestsFromTestCase(TestFibonacciRecursive)
    suite_lucas_queue = unittest.TestLoader().loadTestsFromTestCase(TestLucasQueue)
    suite_lucas_recursive = unittest.TestLoader().loadTestsFromTestCase(TestLucasRecursive)
    suite_all = unittest.TestSuite([suite_fibonacci_queue, suite_fibonacci_recursive, suite_lucas_queue, suite_lucas_recursive])
    unittest.TextTestRunner(verbosity=2).run(suite_all)
