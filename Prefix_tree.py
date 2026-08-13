class Trie:

    def __init__(self):
        self.child = [None] * 26
        self.eow = False

    def insert(self, word):

        curr = self

        for ch in word:

            idx = ord(ch) - ord('a')

            if curr.child[idx] is None:
                curr.child[idx] = Trie()

            curr = curr.child[idx]

        curr.eow = True

    def search(self, word):

        curr = self

        for ch in word:

            idx = ord(ch) - ord('a')

            if curr.child[idx] is None:
                return False

            curr = curr.child[idx]

        return curr.eow

    def startsWith(self, prefix):

        curr = self

        for ch in prefix:

            idx = ord(ch) - ord('a')

            if curr.child[idx] is None:
                return False

            curr = curr.child[idx]

        return True
