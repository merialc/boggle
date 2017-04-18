import unittest
import boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    def test_Is_This_Thing_One(self):
        self.assertEqual(1, boggle.check())

def test_all_grid_neighbours(self):
    grid = boggle.make_grid(2, 2)
    neighbours = boggle.all_grid_neighbours(grid)
    self.assertEqual(len(neighbours), len(grid))
    for pos in grid:
        others = list(grid)  # creates a new list from the dictionary's keys
        others.remove(pos)
        self.assertListEqual(sorted(neighbours[pos]), sorted(others))

def test_converting_a_path_to_a_word(self):
    grid = boggle.make_grid(2, 2)
    oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
    twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
    self.assertEqual(oneLetterWord, grid[(0, 0)])
    self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])


def test_search_grid_for_words(self):
    grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
    twoLetterWord = 'AB'
    threeLetterWord = 'ABC'
    notThereWord = "EEE"
    dictionary = [twoLetterWord, threeLetterWord, notThereWord]

    foundWords = boggle.search(grid, dictionary)

    self.assertTrue(twoLetterWord in foundWords)
    self.assertTrue(threeLetterWord in foundWords)
    self.assertTrue(notThereWord not in foundWords)

def test_load_dictionary(self):
    dictionary = boggle.get_dictionary('/usr/share/dict/words')
    self.assertGreater(len(dictionary), 0)

