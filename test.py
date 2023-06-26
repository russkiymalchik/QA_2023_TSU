# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 00:16:28 2023

@author: ASUS
"""
import unittest
import WordSearch

class SolutionTests(unittest.TestCase):
    def setUp(self):
        self.solution = WordSearch.Solution()
        self.board = [['A', 'B', 'C', 'E'],
                      ['S', 'F', 'C', 'S'],
                      ['A', 'D', 'E', 'E']]

    def test_find_existing_word(self):
        result = self.solution.exist(self.board, 'ABCCED')
        print("Run test_find_existing_word")
        self.assertTrue(result)

    def test_find_non_existing_word(self):
        result = self.solution.exist(self.board, 'ABCB')
        print("Run test_find_non_existing_word")
        self.assertFalse(result)

    def test_board_contains_integer(self):
        board = [['A', '1', 'C', 'E'],
                ['S', 'F', 'C', 'S'],
                ['A', 'D', 'E', 'E']]
        result = self.solution.exist(board, 'A1CC')
        print("Run test_board_contains_integer")
        self.assertTrue(result)

    def test_board_contains_specialChar(self):
        board = [['A', '1', 'C', 'E'],
                ['S', 'F', '&', 'S'],
                ['A', 'D', 'E', 'E']]
        result = self.solution.exist(board, 'A1C&')
        print("Run test_board_contains_specialChar")
        self.assertTrue(result)

    def test_board_contains_doubleInput(self):
        board = [['A', '1', 'CC', 'E'],
                ['S', 'F', '&', 'S'],
                ['A', 'D', 'E', 'E']]
        result = self.solution.exist(board, 'A1CC&')
        print("Run test_board_contains_doubleInput")
        self.assertFalse(result)

    def test_wordsearchInput_lowercase(self):
        board = [['a', '1', 'C', 'E'],
                ['S', 'F', '&', 'S'],
                ['A', 'D', 'E', 'E']]
        result = self.solution.exist(board, 'a1c&')
        print("Run test_wordsearchInput_lowercase")
        self.assertFalse(result)

    def test_board_contains_lowercase(self):
        board = [['a', '1', 'C', 'E'],
                ['S', 'F', '&', 'S'],
                ['A', 'D', 'E', 'E']]
        result = self.solution.exist(board, 'a1C&')
        print("Run test_board_contains_lowercase")
        self.assertTrue(result)

    def test_empty_board(self):
        board = []

        result = self.solution.exist(board, 'ABCCED')
        print("Run test_empty_board")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()