import unittest


class MyTestCase(unittest.TestCase):
    def test_string_function(self):
        self.assertEqual("morgan", 8)


if __name__ == '__main__':
    unittest.main()
