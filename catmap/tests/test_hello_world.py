# pylint: disable=missing-module-docstring
import unittest


class DummyTest(unittest.TestCase): # pylint: disable=missing-class-docstring
    def test_hello_world(self):
        self.assertEqual(len("Hello World"), 11)


if __name__ == "__main__":
    unittest.main()
