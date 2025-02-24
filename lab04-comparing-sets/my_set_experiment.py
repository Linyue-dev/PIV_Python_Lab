from binary_search import binary_search
from time import time_ns


class WordList_NoOptimization:
    def __init__(self, filename):
        """Reads words from filename and stores them"""
        fh = open(filename, "r")
        self._list = [line for line in map(str.strip, fh)]
        fh.close()

    def __contains__(self, value) -> bool:
        """
        function that allows this class to use:

        all_words = WordList_NoOptimization("wordlist.txt")
        if word in all_words:
        """
        return value in self._list


class WordList_BinarySearch:
    def __init__(self, filename):
        """Reads words from filename and stores them"""


    def __contains__(self, value) -> bool:
        """
        function that allows this class to use:

        all_words = WordList_BinarySearch("wordlist.txt")
        if word in all_words:
        """


class WordList_WithHash:
    def __init__(self, filename):
        """Reads words from filename and stores them"""

    def _hash(self, key: str) -> int:
        """convert key into an integer"""

    def __contains__(self, value: str):
        """
        function that allows this class to use:

        all_words = WordList_WithHash("wordlist.txt")
        if word in all_words:
        """


# =============================================================================
# time it
# =============================================================================
if __name__ == "__main__":
    print(f"{"init":>10}   "
          f"{"search":>10}   "
          f"{"total":>10}   "
          "class")

    for search_class in (
            WordList_NoOptimization,
            WordList_BinarySearch,
            WordList_WithHash,
    ):
        fh_words_to_find = open("words-linux-cleaned-to-find.txt", "r")

        now_all = time_ns()
        all_words = search_class("words-linux-cleaned.txt")
        contained = 0
        setup_time = (time_ns() - now_all) / 1_000_000_000

        now_search_only = time_ns()
        for word in map(str.strip, fh_words_to_find):
            if word in all_words:
                contained += 1
        total_time = (time_ns() - now_all) / 1_000_000_000
        search_time = (time_ns() - now_search_only) / 1_000_000_000
        print(f"{setup_time:10.5f}   "
              f"{search_time:10.5f}   "
              f"{total_time:10.5f}   "
              f"{search_class.__name__}")
