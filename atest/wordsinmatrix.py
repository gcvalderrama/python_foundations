import unittest


def get_pos(x, y, cols, rows):
    result = list()
    result.append((x - 1, y - 1))
    result.append((x - 1, y))
    result.append((x - 1, y + 1))
    result.append((x, y - 1))
    result.append((x, y + 1))
    result.append((x + 1, y - 1))
    result.append((x + 1, y))
    result.append((x + 1, y + 1))
    return list(filter(lambda d: (0 <= d[0] < rows and 0 <= d[1] < cols), result))


def generate_index(valid_words):
    max_len = max([len(w) for w in valid_words])

    index = list()
    for i in range(max_len):
        target = list(filter(lambda c: len(c) > i, valid_words))
        index.append(set([c[i] for c in target]))

    return index


def detect(matrix, valid_words, result, rows, cols, x, y,
           state, prev_x, prev_y, max_len, index):

    state += matrix[x][y]
    if state in valid_words:
        result.append(state)

    if len(state) == max_len:
        return

    for point in get_pos(x, y, cols, rows):
        next_letter = matrix[point[0]][point[1]] in index[len(state)]
        if not (point[0] == prev_x and point[1] == prev_y) and next_letter:
            detect(matrix, valid_words, result, rows, cols,
                   point[0], point[1], state, x, y, max_len,
                   index)


def detect_valid_words(matrix, valid_words):
    if len(matrix) == 0 or len(valid_words) == 0:
        return []

    max_len = max([len(w) for w in valid_words])
    rows = len(matrix)
    cols = len(matrix[0])
    result = list()

    index = generate_index(valid_words)

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] in index[0]:
                detect(matrix, valid_words, result, rows, cols,
                       x, y, "", x, y, max_len, index)
    return result


class Test(unittest.TestCase):

    def test_get_pos(self):
        result = get_pos(0, 0, 4, 4)
        self.assertEqual([(0, 1), (1, 0), (1, 1)], result)

    def test_generate_index(self):
        index = generate_index(['help', 'test', 'semantic'])
        self.assertFalse({'h', 't', 's'} - index[0])
        self.assertFalse({'e'} - index[1])
        self.assertFalse({'l', 's', 'm'} - index[2])

    def test_case_empty(self):
        matrix = [[]]
        words = ['test', 'help']
        result = detect_valid_words(matrix, words)
        self.assertFalse(result)

    def test_words_case_empty(self):
        matrix = [['a', 'b']]
        words = []
        result = detect_valid_words(matrix, words)
        self.assertFalse(result)

    def test_case_words(self):

        matrix = [
            ['h', 'e', 'l', 'd'],
            ['a', 'e', 'l', 'f'],
            ['l', 'e', 'l', 'f'],
            ['l', 'e', 'l', 'p'],
        ]
        words = ['help', 'fle', 'held']
        result = detect_valid_words(matrix, words)
        self.assertEqual(3, len(set(result)))

    def test_case_words_geek(self):
        letters = ['GEEKSFORGEEKS',
                   'GEEKSQUIZGEEK',
                   'IDEQAPRACTICE'
                   ]
        matrix = [[c for c in word] for word in letters]
        words = ['GEEKS']
        result = detect_valid_words(matrix, words)
        self.assertEqual(1, len(set(result)))

    def test_case_words_geek_practice_apri(self):
        letters = ['GEEKSFORGEEKS',
                   'GEEKSQUIZGEEK',
                   'IDEQAPRACTICE'
                   ]
        matrix = [[c for c in word] for word in letters]
        words = ['GEEKS', 'PRACTICE', 'APRI']
        result = detect_valid_words(matrix, words)
        self.assertEqual(3, len(set(result)))

    def test_case_words_complex(self):
        letters = ['housefghijkmlopqrstuvwxyt',
                   'ebcdefghijkmlopqrrtuvwxye',
                   'lbcdefghijkmlopqystuvwxys',
                   'pbcdelghijkmlopqrstuvwxyt',
                   'abcdelghijkmlopqrstuvwxyz',
                   'abcdeaghijkmlopqrstuvwxyz',
                   'abcdefghijkmlopqrstuvwxyz'
                   ]
        matrix = [[c for c in word] for word in letters]
        words = ['house', 'help', 'test', 'try']
        result = detect_valid_words(matrix, words)
        self.assertEqual(len(words), len(set(result)))



if __name__ == "__main__":
    unittest.main()





