import unittest
from trie import Trie
from node import Node

class TrieTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_trie_init(self):
        t1 = Trie()
        self.assertEqual(type(t1.head), type(Node()))
        self.assertEqual(t1.head.key, "*")

    def test_trie_contains(self):
        t1 = Trie()
        t1.head.add_child("b")
        t1.head.get_child("b").add_child("u")
        t1.head.get_child("b").get_child("u").add_child("s")
        t1.head.get_child("b").get_child("u").get_child("s").add_child(0)

        self.assertEqual(t1.head.key, "*")
        self.assertEqual(t1.head.get_child("b").key, "b")
        self.assertEqual(t1.head.get_child("b").get_child("u").key, "u")
        self.assertEqual(t1.head.get_child("b").get_child("u").get_child("s").key, "s")
        self.assertEqual(t1.head.get_child("b").get_child("u").get_child("s").get_child(0).key, 0)       

        self.assertEqual("bus" in t1, True)
        self.assertEqual("busy" in t1, False)

    def test_trie_append(self):
        t1 = Trie()
        
        self.assertEqual("bus" in t1, False)
        self.assertEqual("rhombus" in t1, False)
        self.assertEqual("busy" in t1, False)

        self.assertEqual(t1.append("bus"), True)
        self.assertEqual("bus" in t1, True)
        self.assertEqual(t1.append("bus"), False)

        self.assertEqual(t1.append("rhombus"), True)
        self.assertEqual("rhombus" in t1, True)

        self.assertEqual(t1.append("busy"), True)
        self.assertEqual("busy" in t1, True)

