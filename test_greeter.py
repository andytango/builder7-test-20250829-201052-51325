```python
import unittest
from greeter import greet

class TestGreeter(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("Gophers"), "Hello, Gophers!")

if __name__ == '__main__':
    unittest.main()
