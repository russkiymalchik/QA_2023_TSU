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

    def test_exist_returns_true_for_existing_word(self):
        word = 'ABCCED'
        result = self.solution.exist(self.board, word)
        print("Run1")
        self.assertTrue(result)

    def test_exist_returns_false_for_non_existing_word(self):
        word = 'ABCB'
        result = self.solution.exist(self.board, word)
        print("Run2")
        self.assertFalse(result)

    def test_exist_returns_false_for_empty_board(self):
        board = []
        word = 'ABCCED'
        result = self.solution.exist(board, word)
        print("Run3")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()