"""Code Generation — 30 Python function problems with test assertions.

Each problem defines a function signature, description, and test code.
The model must produce a working Python function; the test code is
appended and executed to validate correctness.

Used for Axis 1: comparing off vs medium vs hard thinking modes.
"""

from __future__ import annotations

SUITE_NAME = "code_gen"
SCORE_TYPE = "code_pass"

QUESTIONS: list[dict[str, str]] = [
    # --- Easy (1-10) ---
    {
        "id": "code-01",
        "question": (
            "Write a Python function `fizzbuzz(n)` that returns a list of strings from 1 to n. "
            "For multiples of 3 return 'Fizz', for multiples of 5 return 'Buzz', "
            "for multiples of both return 'FizzBuzz', otherwise return the number as a string."
        ),
        "expected": "pass",
        "test_code": (
            "assert fizzbuzz(5) == ['1', '2', 'Fizz', '4', 'Buzz']\n"
            "assert fizzbuzz(15)[-1] == 'FizzBuzz'\n"
            "assert fizzbuzz(1) == ['1']\n"
            "assert len(fizzbuzz(100)) == 100\n"
        ),
    },
    {
        "id": "code-02",
        "question": (
            "Write a Python function `reverse_words(s)` that takes a string and returns "
            "a string with the words in reverse order. Words are separated by spaces."
        ),
        "expected": "pass",
        "test_code": (
            "assert reverse_words('hello world') == 'world hello'\n"
            "assert reverse_words('a') == 'a'\n"
            "assert reverse_words('the sky is blue') == 'blue is sky the'\n"
        ),
    },
    {
        "id": "code-03",
        "question": (
            "Write a Python function `is_palindrome(s)` that returns True if the string "
            "is a palindrome (ignoring case and non-alphanumeric characters), False otherwise."
        ),
        "expected": "pass",
        "test_code": (
            "assert is_palindrome('racecar') == True\n"
            "assert is_palindrome('A man, a plan, a canal: Panama') == True\n"
            "assert is_palindrome('hello') == False\n"
            "assert is_palindrome('') == True\n"
        ),
    },
    {
        "id": "code-04",
        "question": (
            "Write a Python function `flatten(lst)` that takes a nested list and returns "
            "a flat list. For example, flatten([1, [2, [3, 4], 5]]) should return [1, 2, 3, 4, 5]."
        ),
        "expected": "pass",
        "test_code": (
            "assert flatten([1, [2, [3, 4], 5]]) == [1, 2, 3, 4, 5]\n"
            "assert flatten([]) == []\n"
            "assert flatten([1, 2, 3]) == [1, 2, 3]\n"
            "assert flatten([[1], [2], [3]]) == [1, 2, 3]\n"
        ),
    },
    {
        "id": "code-05",
        "question": (
            "Write a Python function `two_sum(nums, target)` that returns a list of two "
            "indices such that the values at those indices add up to the target. "
            "Assume exactly one solution exists."
        ),
        "expected": "pass",
        "test_code": (
            "result = two_sum([2, 7, 11, 15], 9)\n"
            "assert sorted(result) == [0, 1]\n"
            "result = two_sum([3, 2, 4], 6)\n"
            "assert sorted(result) == [1, 2]\n"
        ),
    },
    {
        "id": "code-06",
        "question": (
            "Write a Python function `count_vowels(s)` that returns the number of vowels "
            "(a, e, i, o, u — case insensitive) in a string."
        ),
        "expected": "pass",
        "test_code": (
            "assert count_vowels('hello') == 2\n"
            "assert count_vowels('AEIOU') == 5\n"
            "assert count_vowels('xyz') == 0\n"
            "assert count_vowels('') == 0\n"
        ),
    },
    {
        "id": "code-07",
        "question": (
            "Write a Python function `max_profit(prices)` that takes a list of stock prices "
            "(one per day) and returns the maximum profit from buying and selling once. "
            "If no profit is possible, return 0."
        ),
        "expected": "pass",
        "test_code": (
            "assert max_profit([7, 1, 5, 3, 6, 4]) == 5\n"
            "assert max_profit([7, 6, 4, 3, 1]) == 0\n"
            "assert max_profit([1, 2]) == 1\n"
            "assert max_profit([]) == 0\n"
        ),
    },
    {
        "id": "code-08",
        "question": (
            "Write a Python function `remove_duplicates(lst)` that returns a new list "
            "with duplicates removed while preserving the original order."
        ),
        "expected": "pass",
        "test_code": (
            "assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]\n"
            "assert remove_duplicates([]) == []\n"
            "assert remove_duplicates([1]) == [1]\n"
            "assert remove_duplicates(['a', 'b', 'a']) == ['a', 'b']\n"
        ),
    },
    {
        "id": "code-09",
        "question": (
            "Write a Python function `caesar_cipher(text, shift)` that encrypts text "
            "using Caesar cipher. Only shift letters (a-z, A-Z), leave other characters unchanged."
        ),
        "expected": "pass",
        "test_code": (
            "assert caesar_cipher('abc', 1) == 'bcd'\n"
            "assert caesar_cipher('xyz', 3) == 'abc'\n"
            "assert caesar_cipher('Hello, World!', 13) == 'Uryyb, Jbeyq!'\n"
            "assert caesar_cipher('abc', 0) == 'abc'\n"
        ),
    },
    {
        "id": "code-10",
        "question": (
            "Write a Python function `chunk_list(lst, size)` that splits a list into "
            "chunks of the given size. The last chunk may be smaller."
        ),
        "expected": "pass",
        "test_code": (
            "assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]\n"
            "assert chunk_list([], 3) == []\n"
            "assert chunk_list([1, 2, 3], 5) == [[1, 2, 3]]\n"
            "assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]\n"
        ),
    },

    # --- Medium (11-20) ---
    {
        "id": "code-11",
        "question": (
            "Write a Python function `valid_parentheses(s)` that returns True if the "
            "string of parentheses '(', ')', '{', '}', '[', ']' is valid (properly opened "
            "and closed in the correct order)."
        ),
        "expected": "pass",
        "test_code": (
            "assert valid_parentheses('()[]{}') == True\n"
            "assert valid_parentheses('(]') == False\n"
            "assert valid_parentheses('([])') == True\n"
            "assert valid_parentheses('{[}]') == False\n"
            "assert valid_parentheses('') == True\n"
        ),
    },
    {
        "id": "code-12",
        "question": (
            "Write a Python function `merge_sorted(a, b)` that merges two sorted lists "
            "into a single sorted list without using the built-in sort."
        ),
        "expected": "pass",
        "test_code": (
            "assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]\n"
            "assert merge_sorted([], [1, 2]) == [1, 2]\n"
            "assert merge_sorted([1], []) == [1]\n"
            "assert merge_sorted([1, 1], [1, 1]) == [1, 1, 1, 1]\n"
        ),
    },
    {
        "id": "code-13",
        "question": (
            "Write a Python function `longest_common_prefix(strs)` that takes a list of "
            "strings and returns the longest common prefix among them."
        ),
        "expected": "pass",
        "test_code": (
            "assert longest_common_prefix(['flower', 'flow', 'flight']) == 'fl'\n"
            "assert longest_common_prefix(['dog', 'racecar', 'car']) == ''\n"
            "assert longest_common_prefix(['abc']) == 'abc'\n"
            "assert longest_common_prefix([]) == ''\n"
        ),
    },
    {
        "id": "code-14",
        "question": (
            "Write a Python function `matrix_transpose(matrix)` that returns the transpose "
            "of a 2D list (list of lists). Each inner list is a row."
        ),
        "expected": "pass",
        "test_code": (
            "assert matrix_transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]\n"
            "assert matrix_transpose([[1]]) == [[1]]\n"
            "assert matrix_transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]\n"
        ),
    },
    {
        "id": "code-15",
        "question": (
            "Write a Python function `group_anagrams(words)` that takes a list of strings "
            "and returns a list of groups, where each group contains words that are anagrams "
            "of each other. The order of groups and words within groups does not matter."
        ),
        "expected": "pass",
        "test_code": (
            "result = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])\n"
            "result_sorted = [sorted(g) for g in result]\n"
            "result_sorted.sort()\n"
            "assert result_sorted == [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]\n"
        ),
    },
    {
        "id": "code-16",
        "question": (
            "Write a Python function `spiral_order(matrix)` that returns all elements "
            "of a 2D matrix in spiral order (clockwise from the top-left corner)."
        ),
        "expected": "pass",
        "test_code": (
            "assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]\n"
            "assert spiral_order([[1]]) == [1]\n"
            "assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]\n"
        ),
    },
    {
        "id": "code-17",
        "question": (
            "Write a Python function `roman_to_int(s)` that converts a Roman numeral string "
            "to its integer value. Handle I, V, X, L, C, D, M and subtractive notation."
        ),
        "expected": "pass",
        "test_code": (
            "assert roman_to_int('III') == 3\n"
            "assert roman_to_int('IV') == 4\n"
            "assert roman_to_int('IX') == 9\n"
            "assert roman_to_int('LVIII') == 58\n"
            "assert roman_to_int('MCMXCIV') == 1994\n"
        ),
    },
    {
        "id": "code-18",
        "question": (
            "Write a Python function `find_missing(nums)` that takes a list of n distinct "
            "numbers in the range [0, n] and returns the one number missing from the range."
        ),
        "expected": "pass",
        "test_code": (
            "assert find_missing([3, 0, 1]) == 2\n"
            "assert find_missing([0, 1]) == 2\n"
            "assert find_missing([9,6,4,2,3,5,7,0,1]) == 8\n"
            "assert find_missing([0]) == 1\n"
        ),
    },
    {
        "id": "code-19",
        "question": (
            "Write a Python function `compress(s)` that performs basic string compression. "
            "For example, 'aabcccccaaa' becomes 'a2b1c5a3'. If the compressed string is not "
            "shorter than the original, return the original string."
        ),
        "expected": "pass",
        "test_code": (
            "assert compress('aabcccccaaa') == 'a2b1c5a3'\n"
            "assert compress('abc') == 'abc'\n"
            "assert compress('aaa') == 'a3'\n"
            "assert compress('') == ''\n"
        ),
    },
    {
        "id": "code-20",
        "question": (
            "Write a Python function `deep_get(d, keys, default=None)` that safely retrieves "
            "a nested value from a dictionary given a list of keys. Return default if any key is missing."
        ),
        "expected": "pass",
        "test_code": (
            "d = {'a': {'b': {'c': 42}}}\n"
            "assert deep_get(d, ['a', 'b', 'c']) == 42\n"
            "assert deep_get(d, ['a', 'x'], 'nope') == 'nope'\n"
            "assert deep_get(d, []) == d\n"
            "assert deep_get({}, ['a']) is None\n"
        ),
    },

    # --- Hard (21-30) ---
    {
        "id": "code-21",
        "question": (
            "Write a Python function `lru_cache_dict(capacity)` that returns an object with "
            "`get(key)` and `put(key, value)` methods implementing an LRU cache. "
            "`get` returns -1 if the key is not found. Both operations should be O(1)."
        ),
        "expected": "pass",
        "test_code": (
            "cache = lru_cache_dict(2)\n"
            "cache.put(1, 1)\n"
            "cache.put(2, 2)\n"
            "assert cache.get(1) == 1\n"
            "cache.put(3, 3)  # evicts key 2\n"
            "assert cache.get(2) == -1\n"
            "cache.put(4, 4)  # evicts key 1\n"
            "assert cache.get(1) == -1\n"
            "assert cache.get(3) == 3\n"
            "assert cache.get(4) == 4\n"
        ),
    },
    {
        "id": "code-22",
        "question": (
            "Write a Python function `eval_rpn(tokens)` that evaluates a list of tokens "
            "representing a Reverse Polish Notation expression. "
            "Tokens are strings of integers or operators (+, -, *, /). "
            "Division truncates toward zero."
        ),
        "expected": "pass",
        "test_code": (
            "assert eval_rpn(['2', '1', '+', '3', '*']) == 9\n"
            "assert eval_rpn(['4', '13', '5', '/', '+']) == 6\n"
            "assert eval_rpn(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']) == 22\n"
        ),
    },
    {
        "id": "code-23",
        "question": (
            "Write a Python function `min_window(s, t)` that finds the minimum window "
            "substring of s that contains all characters of t (including duplicates). "
            "Return '' if no such window exists."
        ),
        "expected": "pass",
        "test_code": (
            "assert min_window('ADOBECODEBANC', 'ABC') == 'BANC'\n"
            "assert min_window('a', 'a') == 'a'\n"
            "assert min_window('a', 'aa') == ''\n"
        ),
    },
    {
        "id": "code-24",
        "question": (
            "Write a Python function `longest_increasing_subseq(nums)` that returns "
            "the length of the longest strictly increasing subsequence."
        ),
        "expected": "pass",
        "test_code": (
            "assert longest_increasing_subseq([10, 9, 2, 5, 3, 7, 101, 18]) == 4\n"
            "assert longest_increasing_subseq([0, 1, 0, 3, 2, 3]) == 4\n"
            "assert longest_increasing_subseq([7, 7, 7, 7]) == 1\n"
            "assert longest_increasing_subseq([]) == 0\n"
        ),
    },
    {
        "id": "code-25",
        "question": (
            "Write a Python function `serialize(root)` and `deserialize(data)` for a "
            "binary tree. Use a simple Node class with `val`, `left`, `right`. "
            "The class should be: class Node: def __init__(self, val=0, left=None, right=None): "
            "self.val = val; self.left = left; self.right = right"
        ),
        "expected": "pass",
        "test_code": (
            "class Node:\n"
            "    def __init__(self, val=0, left=None, right=None):\n"
            "        self.val = val\n"
            "        self.left = left\n"
            "        self.right = right\n"
            "root = Node(1, Node(2), Node(3, Node(4), Node(5)))\n"
            "data = serialize(root)\n"
            "new_root = deserialize(data)\n"
            "assert new_root.val == 1\n"
            "assert new_root.left.val == 2\n"
            "assert new_root.right.val == 3\n"
            "assert new_root.right.left.val == 4\n"
            "assert new_root.right.right.val == 5\n"
        ),
    },
    {
        "id": "code-26",
        "question": (
            "Write a Python function `calc(expression)` that evaluates a simple math "
            "expression string with +, -, *, / and parentheses. Support integer and "
            "float operands. Follow standard operator precedence. Return a float."
        ),
        "expected": "pass",
        "test_code": (
            "assert abs(calc('3 + 4 * 2') - 11.0) < 1e-9\n"
            "assert abs(calc('(3 + 4) * 2') - 14.0) < 1e-9\n"
            "assert abs(calc('10 / 4') - 2.5) < 1e-9\n"
            "assert abs(calc('2 * (3 + (4 - 1))') - 12.0) < 1e-9\n"
        ),
    },
    {
        "id": "code-27",
        "question": (
            "Write a Python function `topo_sort(graph)` that performs topological sort "
            "on a DAG represented as a dict {node: [dependencies]}. "
            "Return a list of nodes in valid topological order."
        ),
        "expected": "pass",
        "test_code": (
            "graph = {'a': [], 'b': ['a'], 'c': ['a'], 'd': ['b', 'c']}\n"
            "result = topo_sort(graph)\n"
            "assert result.index('a') < result.index('b')\n"
            "assert result.index('a') < result.index('c')\n"
            "assert result.index('b') < result.index('d')\n"
            "assert result.index('c') < result.index('d')\n"
            "assert len(result) == 4\n"
        ),
    },
    {
        "id": "code-28",
        "question": (
            "Write a Python function `regex_match(text, pattern)` that implements "
            "simple regex matching with '.' (any single char) and '*' (zero or more of "
            "the preceding element). The match must cover the entire string."
        ),
        "expected": "pass",
        "test_code": (
            "assert regex_match('aa', 'a') == False\n"
            "assert regex_match('aa', 'a*') == True\n"
            "assert regex_match('ab', '.*') == True\n"
            "assert regex_match('aab', 'c*a*b') == True\n"
            "assert regex_match('mississippi', 'mis*is*p*.') == False\n"
        ),
    },
    {
        "id": "code-29",
        "question": (
            "Write a Python function `merge_intervals(intervals)` that takes a list of "
            "[start, end] intervals and returns a list of merged overlapping intervals, "
            "sorted by start time."
        ),
        "expected": "pass",
        "test_code": (
            "assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]\n"
            "assert merge_intervals([[1,4],[4,5]]) == [[1,5]]\n"
            "assert merge_intervals([[1,4],[0,4]]) == [[0,4]]\n"
            "assert merge_intervals([]) == []\n"
        ),
    },
    {
        "id": "code-30",
        "question": (
            "Write a Python function `word_break(s, word_dict)` that returns True if "
            "string s can be segmented into a space-separated sequence of dictionary words."
        ),
        "expected": "pass",
        "test_code": (
            "assert word_break('leetcode', ['leet', 'code']) == True\n"
            "assert word_break('applepenapple', ['apple', 'pen']) == True\n"
            "assert word_break('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']) == False\n"
            "assert word_break('', ['a']) == True\n"
        ),
    },
]
