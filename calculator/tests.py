# tests.py

# Import the unittest module for testing
import unittest
# Import the Calculator class from the pkg.calculator module
from pkg.calculator import Calculator


# Define a test class that inherits from unittest.TestCase
class TestCalculator(unittest.TestCase):
    # Define a setUp method to initialize the test environment
    def setUp(self):
        # Create an instance of the Calculator class
        self.calculator = Calculator()

    # Define a test method for addition
    def test_addition(self):
        # Evaluate the expression "3 + 5"
        result = self.calculator.evaluate("3 + 5")
        # Assert that the result is equal to 8
        self.assertEqual(result, 8)

    # Define a test method for subtraction
    def test_subtraction(self):
        # Evaluate the expression "10 - 4"
        result = self.calculator.evaluate("10 - 4")
        # Assert that the result is equal to 6
        self.assertEqual(result, 6)

    # Define a test method for multiplication
    def test_multiplication(self):
        # Evaluate the expression "3 * 4"
        result = self.calculator.evaluate("3 * 4")
        # Assert that the result is equal to 12
        self.assertEqual(result, 12)

    # Define a test method for division
    def test_division(self):
        # Evaluate the expression "10 / 2"
        result = self.calculator.evaluate("10 / 2")
        # Assert that the result is equal to 5
        self.assertEqual(result, 5)

    # Define a test method for nested expressions
    def test_nested_expression(self):
        # Evaluate the expression "3 * 4 + 5"
        result = self.calculator.evaluate("3 * 4 + 5")
        # Assert that the result is equal to 17
        self.assertEqual(result, 17)

    # Define a test method for complex expressions
    def test_complex_expression(self):
        # Evaluate the expression "2 * 3 - 8 / 2 + 5"
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        # Assert that the result is equal to 7
        self.assertEqual(result, 7)

    # Define a test method for empty expressions
    def test_empty_expression(self):
        # Evaluate an empty expression
        result = self.calculator.evaluate("")
        # Assert that the result is None
        self.assertIsNone(result)

    # Define a test method for invalid operators
    def test_invalid_operator(self):
        # Assert that a ValueError is raised
        with self.assertRaises(ValueError):
            # Evaluate the expression "$ 3 5"
            self.calculator.evaluate("$ 3 5")

    # Define a test method for not enough operands
    def test_not_enough_operands(self):
        # Assert that a ValueError is raised
        with self.assertRaises(ValueError):
            # Evaluate the expression "+ 3"
            self.calculator.evaluate("+ 3")


# Check if the script is being run directly
if __name__ == "__main__":
    # Run the tests
    unittest.main()