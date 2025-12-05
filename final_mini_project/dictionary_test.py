import unittest
from dictionary import Dictionary

class DictionaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_dictionary_init(self):
        d1 = Dictionary()
        self.assertEqual(d1.contents, {})

    def test_dictionary_contains(self):
        d1 = Dictionary()
        d1.contents["bus"] = 1

        self.assertEqual(list(d1.contents.keys())[0], "bus")
        self.assertEqual(d1.contents["bus"], 1)

        self.assertEqual("bus" in d1, True)
        self.assertEqual("busy" in d1, False)
        
    def test_dictionary_append(self):
        d1 = Dictionary()
        
        self.assertEqual("bus" in d1, False)
        self.assertEqual("rhombus" in d1, False)
        self.assertEqual("busy" in d1, False)

        self.assertEqual(d1.append("bus"), True)
        self.assertEqual("bus" in d1, True)
        self.assertEqual(d1.append("bus"), False)

        self.assertEqual(d1.append("rhombus"), True)
        self.assertEqual("rhombus" in d1, True)

        self.assertEqual(d1.append("busy"), True)
        self.assertEqual("busy" in d1, True)