import unittest


class DummyTest(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(len("Hello World"), 11)


if __name__ == "__main__":
    unittest.main()
