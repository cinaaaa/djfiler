"""
#   @2019
#
#   Write Test For Djfiler
#
#   Sina Farhadi
#
"""
import unittest
import json
import os
from djfiler import djfiler
from djfiler.core import namegen, founder

tests_dir = os.getcwd()+'/djfiler/tests'

# Test Name Generation
def test_namegen():
    """
    Test Name Generation
    """
    callback = namegen.generate_name()
    if len(callback) == 40: return True
    else: return False

# Test Finder
def test_finder(dest, key):
    """
    Test Finding File
    """
    xts = founder.findfile(dest ,key)
    data = json.loads(xts)
    if data['find']: return True
    else: return False

# Test Class Initialized
def test_class(dest):
    try:
        djfiler.Filer(dest, False)
        return True
    except:
        return False


class DjfilerTest(unittest.TestCase):
    """
    Test Functions in Core
    """
    def testNameGeneration(self):
        self.assertEqual(test_namegen(), True)

    def test_finder(self):
        self.assertEqual(test_finder(tests_dir, 'test'), True)

    def testclass(self):
        self.assertEqual(test_class(tests_dir), True)


if __name__ == '__main__':
    unittest.main()