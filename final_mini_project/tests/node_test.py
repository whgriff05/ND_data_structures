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
