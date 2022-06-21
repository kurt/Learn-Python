import unittest
from unittest.mock import MagicMock
from python_module import BasicClass

class TestAllMethods(unittest.TestCase):

    def test_upper(self):
        BCInst = BasicClass()
        self.assertEqual('foo'.upper(), 'FOO')
        BCInst._mainFunc()

    def testMock(self):
        BCInst = BasicClass()
        BCInst._initializeSerialPort = MagicMock(return_value=10)
        retVal = BCInst._initializeSerialPort()
        self.assertEqual(retVal,10)

if __name__ == '__main__':
    unittest.main()
