import unittest
from dictionary import Dictionary

class DictionaryTest(unittest.TestCase):
    Total = 3
    Points = 0

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        print()
        print(f"\tScore: {cls.Points}/{cls.Total}")
        print(f"\tStatus: {"Success" if cls.Points >= cls.Total else "Failure"}")

    def test_dictionary_init(self):
        d1 = Dictionary()
        self.assertEqual(d1.contents, {})

        DictionaryTest.Points += 1

    def test_dictionary_contains(self):
        d1 = Dictionary()
        d1.contents["bus"] = 1

        self.assertEqual(list(d1.contents.keys())[0], "bus")
        self.assertEqual(d1.contents["bus"], 1)

        self.assertEqual("bus" in d1, True)
        self.assertEqual("busy" in d1, False)

        DictionaryTest.Points += 1
        
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

        DictionaryTest.Points += 1