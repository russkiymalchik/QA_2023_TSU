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
        print("Run1")
        self.assertTrue(result)

    def test_find_non_existing_word(self):
        result = self.solution.exist(self.board, 'ABCB')
        print("Run2")
        self.assertFalse(result)

    def test_empty_board(self):
        board = []

        result = self.solution.exist(board, 'ABCCED')
        print("Run3")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()