class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])

        def recurse(word_index, i, j, visited):

            if word_index == len(word):
                return True

            if (
                not (0 <= i < n)
                or not (0 <= j < m)
                or (i, j) in visited
            ):
                return False

            if not word[word_index] == board[i][j]:
                return False

            visited.add((i, j))

            word_exists = (
                recurse(word_index + 1, i + 1, j, visited)
                or recurse(word_index + 1, i - 1, j, visited)
                or recurse(word_index + 1, i, j + 1, visited)
                or recurse(word_index + 1, i, j - 1, visited)
            )

            visited.remove((i, j))

            return word_exists

        for i in range(n):
            for j in range(m):
                if (recurse(0, i, j, set())):
                    return True
        return False

