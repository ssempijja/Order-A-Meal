import unittest
from app.meal import index
import json


class LoginTest(unittest.TestCase):
    def test_login(self):
        result = json.loads(index().decode())
        self.assertIn('we are here', result)
      


if __name__ == '__main__':
    unittest.main()