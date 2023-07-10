'''
79. Word Search
Given:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacentcells are horizontally 
or vertically neighboring. The same letter cell may not be used more than once.
Solution:
1) the idea is to recursively dive and iterate on words as well
2) in order to not stumble upon visited already nodes, track visited
3) 3 base cases, 1-> if next iter is not equal to next target char - stop, if stumble upon visited - stop , if reaches the word, stop and modify self.ans 
4) if not, continue on 4 dif positions, and if come back from recursion, remove the current element from visited 
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ans = False
        self.word = word
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    self.dfs(i, j, '', set(), 0)
        return self.ans

    def dfs(self, i, j, path, visited, next_character): 
        # base cases

        if next_character < len(self.word) and self.word[next_character] != self.board[i][j]:
            return 

        if (i, j) in visited:
            return

        path += self.board[i][j]

        if path == self.word:
            self.ans = True
            return

        visited.add((i, j))

        if i - 1 >= 0:
            self.dfs(i - 1, j, path, visited, next_character + 1)

        if j - 1 >= 0:
            self.dfs(i, j - 1, path,visited, next_character + 1)

        if i + 1 < len(self.board):
            self.dfs(i + 1, j, path, visited, next_character + 1)

        if j + 1 < len(self.board[0]):
            self.dfs(i, j + 1, path, visited, next_character + 1)

        visited.remove((i, j))
