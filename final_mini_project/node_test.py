import unittest
from node import Node

class NodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_node_init(self):
        n1 = Node()
        self.assertEqual(n1.key, None)
        self.assertEqual(n1.children, {})

        n2 = Node("a")
        self.assertEqual(n2.key, "a")
        self.assertEqual(n2.children, {})

        n3 = Node("b")
        n3.children["a"] = Node("a")
        self.assertEqual(n3.key, "b")
        self.assertNotEqual(n3.children, {})
        self.assertEqual(n3.children["a"].key, "a")

    def test_node_has_children(self):
        n1 = Node()
        self.assertEqual(n1.key, None)
        self.assertEqual(n1.children, {})
        self.assertEqual(n1.has_children(), False)

        n2 = Node("b")
        n2.children["a"] = Node("a")
        self.assertEqual(n2.key, "b")
        self.assertNotEqual(n2.children, {})
        self.assertEqual(n2.children["a"].key, "a")
        self.assertEqual(n2.has_children(), True)

    def test_node_get_child(self):
        n1 = Node()
        self.assertEqual(n1.get_child("a"), None)
        self.assertEqual(n1.has_children(), False)

        n2 = Node("a")
        n1.children["a"] = n2
        self.assertEqual(n1.get_child("a"), n2)
        self.assertEqual(n1.has_children(), True)

    def test_node_add_child(self):
        n1 = Node("a")
        self.assertEqual(n1.has_children(), False)

        n1.add_child("b")
        self.assertEqual(n1.get_child("b").key, "b")
        self.assertEqual(n1.has_children(), True)

