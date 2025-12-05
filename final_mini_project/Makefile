test:
	@$(MAKE) -sk test-all

test-all: test-node test-trie test-dictionary

test-node: node.py
	@echo Testing node...
	@python3 -m unittest node_test.py
	@echo

test-trie: trie.py
	@echo Testing trie...
	@python3 -m unittest trie_test.py
	@echo

test-dictionary: dictionary.py
	@echo Testing trie...
	@python3 -m unittest dictionary_test.py
	@echo

clean:
	@rm -rf __pycache__